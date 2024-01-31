"""
#Created by Jhonatan A. A. Manco
#Data:June 17/22
########## 
Correction:
#Data:Nov 16/23
variables_metpy_scm
line 318:::The forcing are for the mixing ration, nor for specific humidity 
           mr_u
line 396: The temperature must be the temperature in differents heighs no only 
          from the surface z_u[k,0] to z_u[k,i]
##########
"""

import  numpy as np
import  matplotlib as mpl
import  matplotlib.pyplot as plt

#import   metpy.calc as mpy 
import   metpy.calc

from    metpy.units import units
#       To change the plot parameter 

def variables_metpy(exp):

    maxit   = len(exp.time)
    maxlv   = len(exp.lev)
    #
    #
    #q           =   bomex._q_t(bomex._z)
    #q_ls        =   exp.dqdt
    q_ls        =   units.Quantity(exp.q_adv_h[:][:],'g/kg/hour')
    
    #Horizontal advection tendency humidity_mixing_ratio 
    q_ls        =   q_ls.to('kg/kg/s')
    
    #t_ls        =   exp.dTdt
    #Horizontal advection tendency of air temperature
    t_ls        =   units.Quantity(exp.T_adv_h[:][:],'kelvin/hour')
    
    t_ls        =   t_ls.to('kelvin/s')
    
    #Horizontal advection tendency of dry static energy 
    s_ls        =   units.Quantity(exp.s_adv_h[:][:],'kelvin/hour')
    
    s_ls        =   s_ls.to('kelvin/s')
    
    #theta       =   bomex.theta_l(bomex._z)
    T           =   exp.T
    
    Tu          =   units.Quantity(T[:][:],'kelvin')
    
    q           =   exp.q

    qu          =   units.Quantity(q[:][:],'g/kg')
    
    u           =   exp.u
    v           =   exp.v
    #w           =   bomex.w_subsidence(bomex._z)
    omega       =   units.Quantity(exp.omega[:],'mbar/hour')
    
    prec_srf    =   exp.prec_srf
    
    pressureu   =   units.Quantity(exp.lev[:], 'mbar')
    
    alt         =   units.Quantity(exp.alt[:],'m')
    
    z           =   np.zeros(maxlv)
    
    theta       =   metpy.calc.potential_temperature(pressureu, Tu)
    
    w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, mixing=0)
    
    
    #Sensible upwardheat flux 
    SH          =   exp.SH 
    #Latent upward heat flux 
    LH          =   exp.LH 
    #
    T_skin      =   units.Quantity(exp.T_skin[:],'degC')
    
    #z           =   metpy.calc.add_pressure_to_height(height, pressure)
    #zi          =   metpy.calc.pressure_to_height_std(pressureu) 
    
    
    
    pressureu   = pressureu.to('hPa')
    
    T_skin      = T_skin.to('kelvin')
    
    dayinit = 244#01 septembro 
    dayfin  = 284#maximum 283-dia 10 de outubro 
    
    #Lengh of the time array to search
    ndtp    = len(exp.time) 
    
    #Lengh of the time array to search
    ndlev   = len(exp.lev)-8 
    
    pressure= pressureu.magnitude
    
    #theta   = theta.magnitude
    
    q_ls    = q_ls.magnitude
    
    t_ls    = t_ls.magnitude
    
    s_ls    = s_ls.magnitude
    
    #w       = w.magnitude
    
    T_skin  = T_skin.magnitude
    
    g       = 9.81 *units('m/s^2')   # [m/s^2]
    R_d     = 287.0*units('J/kg/K')   # [J/kg/K]
    
    z       = np.zeros((ndtp,ndlev))*units('m')
    
    z[:,0]   =   alt    
    
    Tv  =   metpy.calc.virtual_temperature(Tu, qu).to('kg*K/kg')
    
    
    for k in range(0,ndtp):
    
        for i in range(1,ndlev):
    
            #z[k,i]   = metpy.calc.add_pressure_to_height(z[k,i-1], pressureu[i])
            z[k,i]   =    R_d*Tv[k,0]/g*np.log(pressureu[i-1]/pressureu[i])+z[k,i-1]    


    return theta,qu,t_ls,q_ls,u,v,w ,z

def velw_sfc_flx(u, v, w):
    #    """Surface momentum flux [m^2/s^2]"""
    #   print U_mag
        u_star = 0.28 # [m/s]
    
        U_mag = np.linalg.norm([u, v, w], axis=0)
    
        return -u_star**2. * np.array([u/U_mag, v/U_mag, w/U_mag])

def variables_metpy_mean(time,lev,q_adv_h,T_adv_h,s_adv_h,T,q,u,v,omega,prec_srf,SH,LH,T_skin):


    maxit   = len(time)

    maxlv   = len(lev)

    q_ls        =   units.Quantity(q_adv_h[:][:],'g/kg/hour')
    
    #Horizontal advection tendency humidity_mixing_ratio 
    q_ls        =   q_ls.to('kg/kg/s')
    
    t_ls        =   units.Quantity(T_adv_h[:][:],'kelvin/hour')
    
    t_ls        =   t_ls.to('kelvin/s')
    
    #Horizontal advection tendency of dry static energy 
    s_ls        =   units.Quantity(s_adv_h[:][:],'kelvin/hour')
    
    s_ls        =   s_ls.to('kelvin/s')

    
    Tu          =   units.Quantity(T[:][:],'kelvin')

    qu          =   units.Quantity(q[:][:],'g/kg')
    
    #w           =   bomex.w_subsidence(bomex._z)

    omega       =   units.Quantity(omega[:],'mbar/hour')
    
    pressureu   =   units.Quantity(lev[:], 'mbar')
    
    #alt         =   units.Quantity(alt[:],'m')

    z           =   np.zeros(maxlv)
    
    theta       =   metpy.calc.potential_temperature(pressureu, Tu)
    
    #w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, mixing=0)
    w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, qu)
    
    
    #Sensible upwardheat flux 
    SH          =   SH 
    #Latent upward heat flux 
    LH          =   LH 
    #
    T_skin      =   units.Quantity(T_skin[:],'degC')

    #z           =   metpy.calc.add_pressure_to_height(height, pressure)
    #zi          =   metpy.calc.pressure_to_height_std(pressureu) 
    
    
    pressureu   = pressureu.to('hPa')
    
    
    #Lengh of the time array to search
    ndtp    = len(time) 

    #Lengh of the time array to search
    ndlev   = len(lev) 

    pressure= pressureu.magnitude
    
    #theta   = theta.magnitude
    
    q_ls    = q_ls.magnitude
    
    t_ls    = t_ls.magnitude
    
    s_ls    = s_ls.magnitude
    
    T_skin      = T_skin.to('kelvin')

    #w      = w.magnitude
    #T_skin = T_skin.magnitude

    g       = 9.81 *units('m/s^2')   # [m/s^2]

    R_d     = 287.0*units('J/kg/K')   # [J/kg/K]
    
    z       = np.zeros((ndtp,ndlev))*units('m')
    
    z[:,0]  = 60*units('m')#alt    


    Tv      =   metpy.calc.virtual_temperature(Tu, qu).to('kg*K/kg')

    #Calcula ao contrario o z de cima para baixo
    #z       =   metpy.calc.add_pressure_to_height(z, pressureu)


    #For number of times of specific experiment
    for k in range(0,len(q[0])):

        for i in range(1,ndlev):

            #z[k,i]   = metpy.calc.add_pressure_to_height(z[k,i-1], pressureu[i])
            z[k,i]   =  R_d*Tv[0][k,0]/g*np.log(pressureu[i-1]/pressureu[i])+z[k,i-1]    

            #print z[k,i].magnitude 



    T_mean=np.mean(Tu,axis=0)
    theta_mean=np.mean(theta,axis=0)
    qu_mean=np.mean(qu,axis=0)
    t_ls_mean=np.mean(t_ls,axis=0)
    q_ls_mean=np.mean(q_ls,axis=0)
    s_ls_mean=np.mean(s_ls,axis=0)
    u_mean=np.mean(u,axis=0)
    v_mean=np.mean(v,axis=0)
    w_mean=np.mean(w,axis=0)
    omega_mean=np.mean(omega,axis=0)

    #data:30/04/2020
    #Modification on the potential temperature profile 
    #to put an inversion, this allows 
    #defined completely well a shallow 
    #convection without trazes of bouyance and 
    #cloud fraction above of threshold defined. 

    theta_inversion=np.zeros((len(theta_mean.magnitude),ndlev))
    theta_inversion[:,:]=theta_mean[:,:].magnitude



    for k in range(0,ndtp):

        c1=0
        c2=0

        for i in range(0,ndlev):

            #theta_inversion[k,i] = theta_mean[k,i].magnitude

            if z[k,i].magnitude>3000.0 and c1==0:

                y1  =   z[k,i].magnitude
                x1  =   theta_mean[k,i].magnitude
                c1  =   c1+1 

            if z[k,i].magnitude>4000.0 :

                if c2==0:
                    y2  =   z[k,i].magnitude
                    x2  =   theta_mean[k,i].magnitude
                    c2  =   c2+1 

                    mi=(x2-x1)/(y2-y1)

                #line equation, y-y0=m(x-x0)
                theta_inversion[k,i] = x2 + (4.0)*mi*(z[k,i].magnitude-y2)


    #return theta,qu,t_ls,q_ls,u,v,w ,z
    return T_mean,theta_mean,theta_inversion,qu_mean,t_ls_mean,q_ls_mean,s_ls_mean,u_mean,v_mean,w_mean,omega_mean,T_skin ,z,pressureu

def variables_metpy_scm(exp):


    #Lengh of the time array to search
    ndtp    = len(exp.tsec) 
    #Lengh of the time array to search
    ndlev   = len(exp.lev) 

    q_ls_u       =   units.Quantity(exp.divq[:,::-1,0,0],'kg/kg/s')

    t_ls_u        =   units.Quantity(exp.divT[:,::-1,0,0],'kelvin/s')
    
    #Horizontal advection tendency of dry static energy 
    s_ls_u        =   units.Quantity(exp.divs[:,::-1,0,0],'kelvin/s')
    
    T_u          =   units.Quantity(exp.T[:,::-1,0,0],'kelvin')

    mr_u         =   units.Quantity(exp.q[:,::-1,0,0],'kg/kg')
     #convert to specific humidity from mixing ratio
    q_u           =   mr_u/(1.0 + mr_u)


    q_u          =   q_u.to('g/kg')
    
    omega_u       =   units.Quantity(exp.omega[:,::-1,0,0],'Pa/s')

    u_u           =   units.Quantity(exp.u[:,::-1,0,0],'m/s')
    v_u           =   units.Quantity(exp.v[:,::-1,0,0],'m/s')
    prec_srf_u    =   units.Quantity(exp.prec_srf[:,0,0],'mm/hour')

    pressure_u   =   units.Quantity(exp.lev[::-1], 'Pa')
    
    
    theta_u       =   metpy.calc.potential_temperature(pressure_u, T_u)
    
    #w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, mixing=0)
    w_u           =   metpy.calc.vertical_velocity(omega_u, pressure_u, T_u, q_u)
    
    
    #Sensible upwardheat flux 
    SH          =   exp.shflx[:,0,0] 
    #Latent upward heat flux 
    LH          =   exp.lhflx[:,0,0]
    #
    Tg_u          =   units.Quantity(exp.Tg[:,0,0],'kelvin')

    #z           =   metpy.calc.add_pressure_to_height(height, pressure)
    #zi          =   metpy.calc.pressure_to_height_std(pressureu) 
    
    
    pressure= pressure_u.magnitude
    
    q   = q_u.magnitude

    T   = T_u.magnitude

    theta   = theta_u.magnitude
    
    q_ls    = q_ls_u.magnitude
    
    t_ls    = t_ls_u.magnitude
    
    s_ls    = s_ls_u.magnitude

    u       = u_u.magnitude
    v       = v_u.magnitude
    w       = w_u.magnitude
    omega   = omega_u.magnitude

    Tg      = Tg_u.magnitude
    
    g       = 9.81 *units('m/s^2')   # [m/s^2]

    R_d     = 287.0*units('J/kg/K')   # [J/kg/K]
    
    
    #level function of time
    z_u       = np.zeros((ndtp,ndlev))*units('m')
    z_u[0]  = 60*units('m')#alt    

    Tv_u      =   metpy.calc.virtual_temperature(T_u, q_u).to('kg*K/kg')

    z=z_u.magnitude

    #Calcula ao contrario o z de cima para baixo
    #z       =   metpy.calc.add_pressure_to_height(z, pressureu)

    #For number of times of specific experiment
    #used the first time to make the z
    #if all z in function of time are necessery 
    # it too cost 

    #for k in range(0,1):
    for k in range(0,ndtp):
        for i in range(1,ndlev):

            #z_u[k,i]   = metpy.calc.add_pressure_to_height(z_u[k,i-1], pressure_u[i])
            z_u[k,i]   =  R_d*Tv_u[k,i]/g*np.log(pressure_u[i-1]/pressure_u[i])+z_u[k,i-1]    
        

    return T,theta,q,t_ls,q_ls,s_ls,u,v,w,omega,Tg ,z,pressure,SH,LH


def variables_metpy_mean_scm(time,lev,q_adv_h,T_adv_h,s_adv_h,T,q,u,v,omega,prec_srf,SH,LH,T_skin,wt):


    maxit   = len(time)
    maxlv   = len(lev)

    q_ls        =   units.Quantity(q_adv_h[:][:],'kg/kg/s')
    
    t_ls        =   units.Quantity(T_adv_h[:][:],'kelvin/s')
    
    #Horizontal advection tendency of dry static energy 
    s_ls        =   units.Quantity(s_adv_h[:][:],'kelvin/s')
    
    Tu          =   units.Quantity(T[:][:],'kelvin')

    qu          =   units.Quantity(q[:][:],'kg/kg')

    omega       =   units.Quantity(omega[:],'Pa/s')
    
    pressureu   =   units.Quantity(lev[:], 'Pa')
    
    z           =   np.zeros(maxlv)
    
    theta       =   metpy.calc.potential_temperature(pressureu, Tu)
    
    #w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, mixing=0)
    w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, qu)
    
    
    #Sensible upwardheat flux 
    SH          =   SH 
    #Latent upward heat flux 
    LH          =   LH 
    #
    T_skin      =   units.Quantity(T_skin[:],'kelvin')

    #z           =   metpy.calc.add_pressure_to_height(height, pressure)
    #zi          =   metpy.calc.pressure_to_height_std(pressureu) 
    
    
    def velw_sfc_flx(u, v, w):
    #    """Surface momentum flux [m^2/s^2]"""
    #   print U_mag
        u_star = 0.28 # [m/s]
    
        U_mag = np.linalg.norm([u, v, w], axis=0)
    
        return -u_star**2. * np.array([u/U_mag, v/U_mag, w/U_mag])
    
    
    #Lengh of the time array to search
    ndtp    = len(time) 

    #Lengh of the time array to search
    ndlev   = len(lev) 

    pressure= pressureu.magnitude
    
    #theta   = theta.magnitude
    
    q_ls    = q_ls.magnitude
    
    t_ls    = t_ls.magnitude
    
    s_ls    = s_ls.magnitude
    
    #w      = w.magnitude
    #T_skin = T_skin.magnitude

    g       = 9.81 *units('m/s^2')   # [m/s^2]

    R_d     = 287.0*units('J/kg/K')   # [J/kg/K]
    
    z       = np.zeros((ndtp,ndlev))*units('m')
    
    z[:,0]  = 60*units('m')#alt    



    Tv      =   metpy.calc.virtual_temperature(Tu, qu).to('kg*K/kg')


    #Calcula ao contrario o z de cima para baixo
    #z       =   metpy.calc.add_pressure_to_height(z, pressureu)


    #For number of times of specific experiment
    for k in range(0,len(q[0])):

        for i in range(1,ndlev):

            #z[k,i]   = metpy.calc.add_pressure_to_height(z[k,i-1], pressureu[i])
            z[k,i]   =  R_d*Tv[0][k,0]/g*np.log(pressureu[i-1]/pressureu[i])+z[k,i-1]    

            #print z[k,i].magnitude 

    z       =z.magnitude

    #mean
    #T_mean=np.mean(Tu,axis=0)
    #theta_mean=np.mean(theta,axis=0)
    #qu_mean=np.mean(qu,axis=0)
    #t_ls_mean=np.mean(t_ls,axis=0)
    #q_ls_mean=np.mean(q_ls,axis=0)
    #s_ls_mean=np.mean(s_ls,axis=0)
    #u_mean=np.mean(u,axis=0)
    #v_mean=np.mean(v,axis=0)
    #w_mean=np.mean(w,axis=0)
    #omega_mean=np.mean(omega,axis=0)

    #T_skin_mean =   np.mean(T_skin,axis=0).magnitude 
    #SH_mean     =   np.mean(SH,axis=0)
    #LH_mean     =   np.mean(LH,axis=0)
    #prec_mean   =   np.mean(prec_srf,axis=0)
    #print(theta_mean)

    #cases_iop1=8
    #c1=8

    #cases_iop1=23
    #c2=23

    #weight=0.5

    #weight=1.0
    #c1=31.0
    #c2=31.0
    #wt=[   
    #       weight/c1,weight/c1,weight/c1,weight/c1,weight/c1,
    #       weight/c1,weight/c1,weight/c1,
    #       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
    #       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
    #       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
    #       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
    #       weight/c2,weight/c2,weight/c2
    #    ]

    #c1=9.0
    #weight =1.0

    #wt=[   
    #       weight/c1,weight/c1,weight/c1,weight/c1,
    #       weight/c1,weight/c1,weight/c1,weight/c1,
    #       weight/c1,
    #    ]

#    weight=1.0
#    c2=23.0
#    wt=[   
#           weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#           weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#           weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#           weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#           weight/c2,weight/c2,weight/c2
#        ]
#
    #weight =1.0
    #c1=15.0
    #wt=[   
    #       weight/c1,weight/c1,weight/c1,weight/c1,weight/c1,
    #       weight/c1,weight/c1,weight/c1,weight/c1,weight/c1,
    #       weight/c1,weight/c1,weight/c1,weight/c1,weight/c1,
    #    ]

    #weight =1.0
    #c1=7.0
    #wt=[   
    #       weight/c1,weight/c1,weight/c1,weight/c1,weight/c1,
    #       weight/c1,weight/c1        ]


    #weighted average
    T_mean      =np.average(Tu      ,axis=0,weights=wt)
    theta_mean  =np.average(theta   ,axis=0,weights=wt)
    qu_mean     =np.average(qu      ,axis=0,weights=wt)
    t_ls_mean   =np.average(t_ls    ,axis=0,weights=wt)
    q_ls_mean   =np.average(q_ls    ,axis=0,weights=wt)
    s_ls_mean   =np.average(s_ls    ,axis=0,weights=wt)
    u_mean      =np.average(u       ,axis=0,weights=wt)
    v_mean      =np.average(v       ,axis=0,weights=wt)
    w_mean      =np.average(w       ,axis=0,weights=wt)
    omega_mean  =np.average(omega   ,axis=0,weights=wt)
    T_skin_mean =np.average(T_skin  ,axis=0,weights=wt) 
    SH_mean     =np.average(SH      ,axis=0,weights=wt)
    LH_mean     =np.average(LH      ,axis=0,weights=wt)
    prec_mean   =np.average(prec_srf,axis=0,weights=wt)


    #print(theta_mean)
    #exit()
    #data:30/04/2020
    #Modification on the potential temperature profile 
    #to put an inversion, this allows 
    #defined completely well a shallow 
    #convection without trazes of bouyance and 
    #cloud fraction above of threshold defined. 

    #theta_inversion=np.zeros((len(theta_mean.magnitude),ndlev))
    #theta_inversion[:,:]=theta_mean[:,:].magnitude
 
    #average acaba con a magnitude das medias 
    theta_inversion=np.zeros((len(theta_mean),ndlev))
    theta_inversion[:,:]=theta_mean[:,:]


    for k in range(0,ndtp):

        c1=0
        c2=0

        for i in range(0,ndlev):

            #theta_inversion[k,i] = theta_mean[k,i].magnitude

            if z[k,i]>3000.0  and c1==0:

                y1  =   z[k,i]
                #x1  =   theta_mean[k,i].magnitude
                x1  =   theta_mean[k,i]
                c1  =   c1+1 

            if z[k,i]>=4500.0 :

                if c2==0:
                    y2  =   z[k,i]
                    #x2  =   theta_mean[k,i].magnitude
                    x2  =   theta_mean[k,i]
                    c2  =   c2+1 

                    mi=(x2-x1)/(y2-y1)

                #line equation, y-y0=m(x-x0)
                theta_inversion[k,i] = x2 + (2.0)*mi*(z[k,i]-y2)


    #return theta,qu,t_ls,q_ls,u,v,w ,z
    return T_mean,theta_mean,theta_inversion,qu_mean,t_ls_mean,q_ls_mean,s_ls_mean,u_mean,v_mean,w_mean,omega_mean,T_skin_mean,SH_mean,LH_mean,prec_mean ,z,pressure


def variables_metpy_mean_scm_wchange(time,lev,q_adv_h,T_adv_h,s_adv_h,T,q,u,v,omega,prec_srf,SH,LH,T_skin):


    maxit   = len(time)
    maxlv   = len(lev)

    q_ls        =   units.Quantity(q_adv_h[:][:],'kg/kg/s')
    
    t_ls        =   units.Quantity(T_adv_h[:][:],'kelvin/s')
    
    #Horizontal advection tendency of dry static energy 
    s_ls        =   units.Quantity(s_adv_h[:][:],'kelvin/s')
    
    Tu          =   units.Quantity(T[:][:],'kelvin')

    qu          =   units.Quantity(q[:][:],'kg/kg')

    qu          =   qu.to('g/kg')
    
    omega       =   units.Quantity(omega[:],'Pa/s')
    
    pressureu   =   units.Quantity(lev[:], 'Pa')
    
    z           =   np.zeros(maxlv)
    
    theta       =   metpy.calc.potential_temperature(pressureu, Tu)
    
    #w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, mixing=0)
    w           =   metpy.calc.vertical_velocity(omega, pressureu, Tu, qu)
    
    
    #Sensible upwardheat flux 
    SH          =   SH 
    #Latent upward heat flux 
    LH          =   LH 
    #
    T_skin      =   units.Quantity(T_skin[:],'kelvin')

    #z           =   metpy.calc.add_pressure_to_height(height, pressure)
    #zi          =   metpy.calc.pressure_to_height_std(pressureu) 
    
    
    def velw_sfc_flx(u, v, w):
    #    """Surface momentum flux [m^2/s^2]"""
    #   print U_mag
        u_star = 0.28 # [m/s]
    
        U_mag = np.linalg.norm([u, v, w], axis=0)
    
        return -u_star**2. * np.array([u/U_mag, v/U_mag, w/U_mag])
    
    pressureu   = pressureu.to('hPa')
    
    
    #Lengh of the time array to search
    ndtp    = len(time) 

    #Lengh of the time array to search
    ndlev   = len(lev) 

    pressure= pressureu.magnitude
    
    #theta   = theta.magnitude
    
    q_ls    = q_ls.magnitude
    
    t_ls    = t_ls.magnitude
    
    s_ls    = s_ls.magnitude
    
    #w      = w.magnitude
    #T_skin = T_skin.magnitude

    g       = 9.81 *units('m/s^2')   # [m/s^2]

    R_d     = 287.0*units('J/kg/K')   # [J/kg/K]
    
    z       = np.zeros((ndtp,ndlev))*units('m')
    
    z[:,0]  = 60*units('m')#alt    


    Tv      =   metpy.calc.virtual_temperature(Tu, qu).to('kg*K/kg')

    #Calcula ao contrario o z de cima para baixo
    #z       =   metpy.calc.add_pressure_to_height(z, pressureu)


    #For number of times of specific experiment
    for k in range(0,len(q[0])):

        for i in range(1,ndlev):

            #z[k,i]   = metpy.calc.add_pressure_to_height(z[k,i-1], pressureu[i])
            z[k,i]   =  R_d*Tv[0][k,0]/g*np.log(pressureu[i-1]/pressureu[i])+z[k,i-1]    

            #print z[k,i].magnitude 



    T_mean=np.mean(Tu,axis=0)
    theta_mean=np.mean(theta,axis=0)
    qu_mean=np.mean(qu,axis=0)
    t_ls_mean=np.mean(t_ls,axis=0)
    q_ls_mean=np.mean(q_ls,axis=0)
    s_ls_mean=np.mean(s_ls,axis=0)
    u_mean=np.mean(u,axis=0)
    v_mean=np.mean(v,axis=0)
    w_mean=np.mean(w,axis=0)
    #omega_mean=np.mean(omega,axis=0)

    #data:30/04/2020
    #Modification on the potential temperature profile 
    #to put an inversion, this allows 
    #defined completely well a shallow 
    #convection without trazes of bouyance and 
    #cloud fraction above of threshold defined. 

    theta_inversion=np.zeros((len(theta_mean.magnitude),ndlev))
    theta_inversion[:,:]=theta_mean[:,:].magnitude


    for k in range(0,ndtp):

        c1=0
        c2=0

        for i in range(0,ndlev):

            #theta_inversion[k,i] = theta_mean[k,i].magnitude

            if z[k,i].magnitude>3000.0 and c1==0:

                y1  =   z[k,i].magnitude
                x1  =   theta_mean[k,i].magnitude
                c1  =   c1+1 

            if z[k,i].magnitude>4000.0 :

                if c2==0:
                    y2  =   z[k,i].magnitude
                    x2  =   theta_mean[k,i].magnitude
                    c2  =   c2+1 

                    mi=(x2-x1)/(y2-y1)

                #line equation, y-y0=m(x-x0)
                theta_inversion[k,i] = x2 + (4.0)*mi*(z[k,i].magnitude-y2)


    #return theta,qu,t_ls,q_ls,u,v,w ,z
    return T_mean,theta_mean,theta_inversion,qu_mean,t_ls_mean,q_ls_mean,s_ls_mean,u_mean,v_mean,w_mean,omega,T_skin ,z,pressureu
