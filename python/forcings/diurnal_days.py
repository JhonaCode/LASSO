import  numpy       as     np

#Python standard library datetime  module
import  datetime    as dt

import  data_own    as down

import  figure_own  as fown

import  matplotlib          as mpl

import  matplotlib.pyplot   as plt

#from    files_direction import file_fig 

#Calculate necessary varibles to use as 
#foncing in SAM, usint METPY
import  calculate_variables_forcing as cal_var 

from    plotparameters import *

import   metpy.calc

from     metpy.units import units



def color_hours(hour):

    line=[1,0]
    color='k'
    
    if    hour==0:
    
        line=[3,2,1,2]
        color='magenta'
    
    if    hour==3:
    
        line=[2,2,1,2]
        color='cyan'
    
    
    if    hour==6:
    
        line=[2, 1]

    elif  hour==9:
    
        line=[1,2,1,2]
        color='m'
    
    elif  hour==12:
    
        line=[2,1,1,3]
        color='tab:brown'
    
    elif  hour==15:
    
        line=[2,1,5,3]
        color='tab:purple'
    
    elif  hour==18:
    
        line=[4,2,1,2]
        color='y'
    
    elif  hour==21:
    
        line=[1,2,4,2]
        color='c'
    	
    return line,color

#Level max

lmax	=4.0

class forz:

    def __init__(self,T_mean,theta,theta_inv,q,t_ls,q_ls,s_ls,u,v,w,\
                omega_mean,T_skin_mean,SH_mean,LH_mean,prec_mean,z,pa,\
                pressure,time,data,lev,h,number_days):  


        self.T          =   T_mean
        self.theta      =   theta 
        self.theta_inv  =   theta_inv
        self.q          =   q
        self.t_ls       =   t_ls
        self.q_ls       =   q_ls
        self.s_ls       =   s_ls
        self.u          =   u
        self.v          =   v
        self.w          =   w
        self.omega      =   omega_mean
        self.T_skin     =   T_skin_mean
        self.sh         =   SH_mean
        self.lh         =   LH_mean
        self.prec       =   prec_mean
        self.z          =   z
        self.pa         =   pa
        self.p          =   pressure
        self.time       =   time
        self.data       =   data
        self.lev        =   lev 

        #forcing data each 20 minutes  
        #Define o tempo  dos dados num dia(Tem dados a cada 20 minutos)
        #A unidade e dias!
        hfinal=number_days+h[1]/24.0

        self.time_sec=np.linspace(0,hfinal,len(SH_mean),endpoint=False)


def forcing_case(exp,exp_days,h,number_days,wt):

    q        =   diurnal_main_days_lat_lon(exp,'q'    ,exp_days,h[0],h[1])
    T        =   diurnal_main_days_lat_lon(exp,'T'    ,exp_days,h[0],h[1])
    u        =   diurnal_main_days_lat_lon(exp,'u'    ,exp_days,h[0],h[1])
    v        =   diurnal_main_days_lat_lon(exp,'v'    ,exp_days,h[0],h[1])
    omega    =   diurnal_main_days_lat_lon(exp,'omega',exp_days,h[0],h[1])
    
    q_adv_h  =   diurnal_main_days_lat_lon(exp,'divq',exp_days,h[0],h[1])
    T_adv_h  =   diurnal_main_days_lat_lon(exp,'divT',exp_days,h[0],h[1])
    s_adv_h  =   diurnal_main_days_lat_lon(exp,'divs',exp_days,h[0],h[1])
    
    T_skin   =   diurnal_main_days_lat_lon(exp,'Tg'     ,exp_days,h[0] ,h[1])
    SH       =   diurnal_main_days_lat_lon(exp,'shflx'   ,exp_days,h[0],h[1])
    LH       =   diurnal_main_days_lat_lon(exp,'lhflx'   ,exp_days,h[0],h[1])
    prec     =   diurnal_main_days_lat_lon(exp,'prec_srf',exp_days,h[0],h[1])

    time= exp[0].tsec
    data= exp[0].data
    lev = exp[0].lev[::-1]


    T_mean,theta,theta_inv,q,t_ls,q_ls,s_ls,u,v,w,\
    omega_mean,T_skin_mean,SH_mean,LH_mean,prec_mean,z,pa\
    =cal_var.variables_metpy_mean_scm(time,lev,q_adv_h,T_adv_h,s_adv_h,T,q,u,v,omega,prec,SH,LH,T_skin,wt)

    #SAM NEED in this units
    pressure =units.Quantity(pa,'Pa').to('mbar').magnitude
    q_sam    =units.Quantity(q ,'kg/kg').to('g/kg').magnitude 


    var=forz(T_mean,theta,theta_inv,q_sam,t_ls,q_ls,s_ls,u,v,w,\
             omega_mean,T_skin_mean,SH_mean,LH_mean,prec_mean,z,pa,\
             pressure,time,data,lev,h,number_days)

            
    return var       
            

def velw_sfc_flx(u, v, w):
#    """Surface momentum flux [m^2/s^2]"""
    u_star = 0.28 # [m/s]

    U_mag = np.linalg.norm([u, v, w], axis=0)

    return -u_star**2.0 * np.array([u/U_mag, v/U_mag, w/U_mag])

def diurnal_main_days(exp,var,days,hi,hf,hours,color,explabel,show): 

    #counter for the days and files  
    k=0

    #number of times in a day 

    idi     = dt.datetime(2014, days[k][2] ,days[k][0], hi) 

    idf     = dt.datetime(2014, days[k][3] ,days[k][1], hf)

    ni,nf   = down.data_n(idi,idf,exp[k].data[:])

    #number of times
    nt      =  nf-ni 

    #number of levels
    nl      =  exp[k].lev[:].shape[0]

    cont        =   np.zeros(len(exp))
    

    mean=[]
    time=[]
    lev =[]


    for ex in exp:


        idi     = dt.datetime(2014, days[k][2] ,days[k][0], hi) 
        idf     = dt.datetime(2014, days[k][3] ,days[k][1], hf)
        
        ni,nf   = down.data_n(idi,idf,ex.data[:])
        
        time.append(ex.data[ni:nf])
        lev.append(ex.lev[0:nl])
        
        if var=='T':
            dvar=2
            mean.append(ex.T[ni:nf,0:nl])
        elif var=='q':
            dvar=2
            mean.append(ex.q[ni:nf,0:nl])
        elif var=='omega':
            dvar=2
            mean.append(ex.omega[ni:nf,0:nl])
        
        elif var=='q1':
            dvar=2
            mean.append(ex.q1[ni:nf,0:nl])
        elif var=='q2':
            dvar=2
            mean.append(ex.q2[ni:nf,0:nl])
        elif var=='u':
            dvar=2
            mean.append(ex.u[ni:nf,0:nl])
        elif var=='v':
            dvar=2
            mean.append(ex.v[ni:nf,0:nl])
        
        elif var=='T_adv_h':
            dvar=2
            mean.append(ex.T_adv_h[ni:nf,0:nl])
        
        elif var=='q_adv_h':
            dvar=2
            mean.append(ex.q_adv_h[ni:nf,0:nl])
        elif var=='s_adv_h':
            dvar=2
            mean.append(ex.s_adv_h[ni:nf,0:nl])
        
        elif var=='T_skin':
            dvar=1
            mean.append(ex.T_skin[ni:nf])
        
        elif var=='prec_srf':
            dvar=1
            mean.append(ex.prec_srf[ni:nf])
        
        elif var=='SH':
            dvar=1
            mean.append(ex.SH[ni:nf])
        elif var=='LH':
            dvar=1
            mean.append(ex.LH[ni:nf])
        
        elif var=='dTdt':
            dvar=2
            mean.append(ex.dTdt[ni:nf,0:nl])
        
        elif var=='dqdt':
            dvar=2
            mean.append(ex.dqdt[ni:nf,0:nl])
        k+=1

    #if var==2:
    #    ax=shade_plot(mean,lev,time,hours,'red',explabel)
    #else:
    #    ax=shade_plot_1d(mean,time,'red',explabel)

    return mean 

def diurnal_main_weight(exp,var,days,hi,hf,hours,color,explabel,show): 

    #counter for the days and files  
    k=0

    #number of times in a day 

    idi     = dt.datetime(2014, days[k][2] ,days[k][0], hi) 

    idf     = dt.datetime(2014, days[k][3] ,days[k][1], hf)

    ni,nf   = down.data_n(idi,idf,exp[0].data[:])

    #number of times
    nt      =  nf-ni 

    #number of levels
    nl      =  exp[k].lev[:].shape[0]

    cont        =   np.zeros(len(exp))
    

    mean=[]
    time=[]
    lev =[]


    for ex in exp:

        idi     = dt.datetime(2014, days[k][2] ,days[k][0], hi) 
        idf     = dt.datetime(2014, days[k][3] ,days[k][1], hf)
        
        ni,nf   = down.data_n(idi,idf,ex.data[:])
        
        time.append(ex.data[ni:nf])
        lev.append(ex.lev[0:nl])

        if var=='T':
            dvar=2
            mean.append(ex.T[ni:nf,0:nl])
        elif var=='q':
            dvar=2
            mean.append(ex.q[ni:nf,0:nl])
        elif var=='omega':
            dvar=2
            mean.append(ex.omega[ni:nf,0:nl])
        
        elif var=='q1':
            dvar=2
            mean.append(ex.q1[ni:nf,0:nl])
        elif var=='q2':
            dvar=2
            mean.append(ex.q2[ni:nf,0:nl])
        elif var=='u':
            dvar=2
            mean.append(ex.u[ni:nf,0:nl])
        elif var=='v':
            dvar=2
            mean.append(ex.v[ni:nf,0:nl])
        
        elif var=='T_adv_h':
            dvar=2
            mean.append(ex.T_adv_h[ni:nf,0:nl])
        
        elif var=='q_adv_h':
            dvar=2
            mean.append(ex.q_adv_h[ni:nf,0:nl])
        elif var=='s_adv_h':
            dvar=2
            mean.append(ex.s_adv_h[ni:nf,0:nl])
        
        elif var=='T_skin':
            dvar=1
            mean.append(ex.T_skin[ni:nf])
        
        elif var=='prec_srf':
            dvar=1
            mean.append(ex.prec_srf[ni:nf])
        
        elif var=='SH':
            dvar=1
            mean.append(ex.SH[ni:nf])
        elif var=='LH':
            dvar=1
            mean.append(ex.LH[ni:nf])
        
        elif var=='dTdt':
            dvar=2
            mean.append(ex.dTdt[ni:nf,0:nl])
        
        elif var=='dqdt':
            dvar=2
            mean.append(ex.dqdt[ni:nf,0:nl])
        k+=1

    #if var==2:
    #    ax=shade_plot(mean,lev,time,hours,'red',explabel)
    #else:
    #    ax=shade_plot_1d(mean,time,'red',explabel)

    return mean 

def diurnal_main_days_lat_lon_wchange(exp,exp_label,var,days,hi,hf,hours,color,explabel,show): 

    #counter for the days and files  
    k=0

    mean=[]
    time=[]
    lev =[]


    for ex in exp:


        idi     = dt.datetime(2014, days[k][2] ,days[k][0], hi, 0) 
        idf     = dt.datetime(2014, days[k][3] ,days[k][1], hf, 20)
        
        ni,nf   = down.data_n(idi,idf,ex.data[:])
        
        time.append(ex.data[ni:nf])
        lev.append(ex.lev[:].shape[0])
        
        if var=='T':
            dvar=4
            mean.append(ex.T[ni:nf,::-1,0,0])
        elif var=='q':
            dvar=4
            mean.append(ex.q[ni:nf,::-1,0,0])
        elif var=='omega':
            dvar=4
            #mean.append(ex.omega[ni:nf,::-1,0,0])
            #the omega wiil be the 
            #omega for a specific day, 
            #to show how the subsidence control
            #the shallow deep
            if exp_label[k]=='mar_10': 
                mean=ex.omega[ni:nf,::-1,0,0]
        
        elif var=='q1':
            dvar=4
            mean.append(ex.q1[ni:nf,::-1,0,0])
        elif var=='q2':
            dvar=4
            mean.append(ex.q2[ni:nf,::-1,0,0])
        elif var=='u':
            dvar=4
            mean.append(ex.u[ni:nf,::-1,0,0])
        elif var=='v':
            dvar=4
            mean.append(ex.v[ni:nf,::-1,0,0])
        elif var=='divT':
            dvar=4
            mean.append(ex.divT[ni:nf,::-1,0,0])
        
        elif var=='divq':
            dvar=4
            mean.append(ex.divq[ni:nf,::-1,0,0])
        elif var=='divs':
            dvar=4
            mean.append(ex.divs[ni:nf,::-1,0,0])
        
        elif var=='Tg':
            dvar=3
            mean.append(ex.Tg[ni:nf,0,0])
        
        elif var=='prec_srf':
            dvar=3
            mean.append(ex.prec_srf[ni:nf,0,0])
        
        elif var=='shflx':
            dvar=3
            mean.append(ex.shflx[ni:nf,0,0])
        elif var=='lhflx':
            dvar=3
            mean.append(ex.lhflx[ni:nf,0,0])
        
        elif var=='dTdt':
            dvar=4
            mean.append(ex.dTdt[ni:nf,::-1,0,0])
        
        elif var=='dqdt':
            dvar=4
            mean.append(ex.dqdt[ni:nf,::-1,0,0])
        k+=1

    #if var==2:
    #    ax=shade_plot(mean,lev,time,hours,'red',explabel)
    #else:
    #    ax=shade_plot_1d(mean,time,'red',explabel)

    return mean 

def diurnal_main_days_lat_lon(exp,var,days,hi,hf): 

    #counter for the days and files  
    k=0

    mean=[]
    time=[]
    lev =[]


    for ex in exp:

        
        idi     = dt.datetime(2014, days[k][2] ,days[k][0], hi, 0) 
        #idf     = dt.datetime(2014, days[k][3] ,days[k][1], hf, 59)
        idf     = dt.datetime(2014, days[k][3] ,days[k][1], hf, 00)
        
        ni,nf   = down.data_n(idi,idf,ex.data[:])
        
        #jprint(idi,idf,ni,nf)
        #print(len(ex.data[idi:idf]))
        #exit()
        
        time.append(ex.data[ni:nf])
        lev.append(ex.lev[:].shape[0])
        
        if var=='T':
            dvar=4
            mean.append(ex.T[ni:nf,::-1,0,0])
        elif var=='q':
            dvar=4
            mean.append(ex.q[ni:nf,::-1,0,0])
        
        elif var=='omega':
            dvar=4
            mean.append(ex.omega[ni:nf,::-1,0,0])
        
        elif var=='q1':
            dvar=4
            mean.append(ex.q1[ni:nf,::-1,0,0])
        elif var=='q2':
            dvar=4
            mean.append(ex.q2[ni:nf,::-1,0,0])
        elif var=='u':
            dvar=4
            mean.append(ex.u[ni:nf,::-1,0,0])
        elif var=='v':
            dvar=4
            mean.append(ex.v[ni:nf,::-1,0,0])
        
        elif var=='divT':
            dvar=4
            mean.append(ex.divT[ni:nf,::-1,0,0])
        
        elif var=='divq':
            dvar=4
            mean.append(ex.divq[ni:nf,::-1,0,0])
        
        elif var=='divs':
            dvar=4
            mean.append(ex.divs[ni:nf,::-1,0,0])
        
        elif var=='Tg':
            dvar=3
            mean.append(ex.Tg[ni:nf,0,0])
        
        elif var=='prec_srf':
            dvar=3
            mean.append(ex.prec_srf[ni:nf,0,0])
        
        elif var=='shflx':
            dvar=3
            mean.append(ex.shflx[ni:nf,0,0])
        
        elif var=='lhflx':
            dvar=3
            mean.append(ex.lhflx[ni:nf,0,0])
        
        elif var=='dTdt':
            dvar=4
            mean.append(ex.dTdt[ni:nf,::-1,0,0])
        
        elif var=='dqdt':
            dvar=4
            mean.append(ex.dqdt[ni:nf,::-1,0,0])
        k+=1

    #if var==2:
    #    ax=shade_plot(mean,lev,time,hours,'red',explabel)
    #else:
    #    ax=shade_plot_1d(mean,time,'red',explabel)

    return mean 

def shade_plot(data,y,time,hours,cor,label,**kw):

    fig =   plt.figure()
    ax  =   plt.axes()

    ####################################
    est =   np.mean(data, axis=0)
    sd  =   np.std(data, axis=0)

    cis =   (est - sd, est + sd)
    #cis =   (est - sd/1.0, est + sd/1.0)
    #cis =   (est*0.90, est*1.10)

    #hour to plot,
    #hours=[0,3,6,9,12]

    for k in range(0,len(time)): 

        for i in range(0,len(hours)): 

            if hours[i]==time[0][k].hour: 


                line,color=color_hours(hours[i])

                ax.fill_betweenx(y[k],cis[0][k,:],cis[1][k,:],alpha=0.5,color=color)# **kw)

                ax.plot(est[k],y[k],color=color)


    #plt.show()
    
    #ax.set_title("sns.tsplot")
    #ax.set_title("custom tsplot")

    return ax

def shade_plot_1d(data,time,cor,label,**kw):

    fig =   plt.figure()
    ax  =   plt.axes()

    ####################################
    est =   np.mean(data,axis=0)
    sd  =   np.std(data,axis=0)

    cis =   (est - sd, est + sd)
    #cis =   (est - sd/1.0, est + sd/1.0)
    #cis =   (est*0.90, est*1.10)

    #ax.fill_betweenx(time[0],cis[0][0],cis[1][0],alpha=0.5,color='red')# **kw)
    ax.plot(time[0],est,color='red')


    #plt.show()
    
    #ax.set_title("sns.tsplot")
    #ax.set_title("custom tsplot")

    return ax
