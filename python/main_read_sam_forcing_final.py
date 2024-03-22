#**************************
#Program to average the forcing variables 
#of specific shallow day, to created a
#a single forcing from sam output of LASSO.
##################################################
#The data from the SCM program was used as forcing. 
##################################################
#Note: The FORCING ARE CRETED IN UTC HOUR
#Note: The plots are in local Manuaus time UTC-4
#Data:06-02-24
#Created by: Jhonatan Aguirre
#**************************
#python 3.9
#
#paste: scm_lsf

import  os,sys

import  inspect

import  numpy as np

import  matplotlib as mpl
import  matplotlib.pyplot as plt
import  matplotlib.ticker as ticker

#Python standard library datetime  module
import  datetime    as dt

import  forcings.read_sam_forcing as rs

#from   Parameters_forcing_iop import *
#       To change the plot parameter 
from   	forcings.plotparameters 	import 	*
#To find data in the array
import  forcings.data_own        as down
#Calculate necessary varibles to use as 
#foncing in SAM, usint METPY
from    forcings.calculate_variables_forcing import *

################################################################ 
#sys.path.append('..')

from    Parameters_dict import *
# to defined fig out direction 
#from    files_direction import *

from    files_direction import *


from scipy.interpolate import griddata, RegularGridInterpolator


#Mean of days with diurnal profiles
#import  diurnal_days as d_days 

#hours colors
#import  hour_color as h_color 


#To load the variable  in the datafile
#from    variabletoload_go   import *

import   metpy.calc
from     metpy.units import units

# to work without display
plt.switch_backend('agg')


namef ='lsf_cases'
pyf   ='/dados/bamc/jhonatan.aguirre/git_repositories/LASSO/python'
folder='%s/%s'%(pyf,namef)

#"""
label       ='todos_lsf_final'

exp          =  [
                 '20150606',###18'c)06-06-2015'
                 "20150609",###35
                 "20150801",###36
                 "20150801",###37
                 '20150627',###3 -c)18-05-2016
                 '20160518',###6 -f)18-05-2016
                 '20160625',###19'n)25-06-2016'
                 '20160818',###20'o)18-08-2016'
                 "20160830",###38
                 "20160610",###39
                 "20160720",###40
                 "20160716",###41
                 "20160619",###42
                 '20180522',###7 g)22-05-2018
                 '20181001',###4 -d)01-10-2018
                 '20180606',###5 -e)06-06-2018
                 '20180707',###8 h)07-07-2018
                 '20180917',###9 i)17-09-2018
                 '20180901',###11k)01-09-2018
                 '20180916',###12l)16-09-2018
                 '20180514',###16p)14-05-2018
                 '20180709',###17q)09-07-2018
                 '20180911',###21'a)01-09-2018'
                 '20180619',###24'e)19-06-2018'
                 '20180914',###26'g)14-09-2018'
                 '20181002',###28'i)02-10-2018'
                 '20180712',###29'j)12-07-2018'
                 '20180710',###32'm)10-07-2018'
                 '20180618',###33'p)18-06-2018'
                 '20180705',###34'q)05-07-2018'
                 "20180711",###43
                 "20180523",###45
                 "20180811",###46
                 '20190612',###22'b)12-06-2019'
                 '20190517',###23'd)17-05-2019'
                 '20190805',###25'f)05-08-2019'
                 '20190404',###10j)04-04-2019
                 '20190709',###1 -a)09-07-2019
                 '20190704',###2 -b)04-07-2019
                 '20190701',###13m)01-07-2019
                 '20190617',###14n)17-06-2019
                 '20190626',###15o)26-06-2019
                 '20190901',###27'h)01-09-2019'
                 '20190707',###30'k)07-07-2019'
                 '20190714',###31'l)14-07-2019'
                 "20190804",###44
                 ]
#"""

"""
label       ='small_lsf_final'
exp          =  [
                 '20190709',###a)09-07-2019
                 '20190704',###b)04-07-2019
                 '20150627',###c)18-05-2016
                 '20181001',###d)01-10-2018
                 '20180606',###e)06-06-2018
                 '20160518',###f)18-05-2016
                 '20180522',###g)22-05-2018
                 '20180707',###h)07-07-2018
                 '20180917',###i)17-09-2018
                 '20190404',###j)04-04-2019
                 '20180901',###k)01-09-2018
                 '20180916',###l)16-09-2018
                 '20190701',###m)01-07-2019
                 '20190617',###n)17-06-2019
                 '20190626',###o)26-06-2019
                 '20180514',###p)14-05-2018
                 '20180709',###q)09-07-2018
                ]  
"""
"""
label       ='medium_lsf_final'
exp          =  [
                 '20150606',###'c)06-06-2015'
                 '20160625',###'n)25-06-2016'
                 '20160818',###'o)18-08-2016'
                 '20180911',###'a)01-09-2018'
                 '20180619',###'e)19-06-2018'
                 '20180914',###'g)14-09-2018'
                 '20181002',###'i)02-10-2018'
                 '20180712',###'j)12-07-2018'
                 '20180710',###'m)10-07-2018'
                 '20180618',###'p)18-06-2018'
                 '20180705',###'q)05-07-2018'
                 '20190901',###'h)01-09-2019'
                 '20190805',###'f)05-08-2019'
                 '20190612',###'b)12-06-2019'
                 '20190517',###'d)17-05-2019'
                 '20190707',###'k)07-07-2019'
                 '20190714',###'l)14-07-2019'
                ]  
"""

"""
label        =  'large_lsf_final'

exp          =  [
                 "20150609",
                 "20150801",
                 "20150801",
                 "20160830",
                 "20160610",
                 "20160720",
                 "20160716",
                 "20160619",
                 "20180711",
                 "20190804",
                 "20180523",
                 "20180811",
                ]  
"""


#snd
T_all=[]
q_all=[]
u_all=[]
v_all=[]
w_all=[]


size    =[]
z_all   =[]


for ex in exp:

    path1='%s/lasso_sam_%s/config'%(computer,ex)

    time,z,pressure,p0,T,q,u_sn,v_sn,w_sn=rs.read(path1,'snd_f')
    
    size.append(T.shape[1])

    z_all.append(z)
    T_all.append(T)
    q_all.append(q)
    u_all.append(u_sn)
    v_all.append(v_sn)
    w_all.append(w_sn)


#Large size sounding
may=np.argmax(size)

#f=0
#for i in range(0,size[may],10):
#
#    print(f,i,size[may],int(size[may]/10)-1)
#
#    f+=1
#
#exit()
T_t=[]
q_t=[]
u_t=[]
v_t=[]
w_t=[]

for i in range (len(exp)):

    if (z_all[may].shape[1]>z_all[i].shape[1]):

        print(z_all[may].shape[1],z_all[i].shape[1],'snd')

        itrT=np.interp(z_all[may][0],z_all[i][0],T_all[i][0,:])
        itrq=np.interp(z_all[may][0],z_all[i][0],q_all[i][0,:])
        itru=np.interp(z_all[may][0],z_all[i][0],u_all[i][0,:])
        itrv=np.interp(z_all[may][0],z_all[i][0],v_all[i][0,:])
        itrw=np.interp(z_all[may][0],z_all[i][0],w_all[i][0,:])

    else:

        itrT=T_all[i][0,:]
        itrq=q_all[i][0,:]
        itru=u_all[i][0,:]
        itrv=v_all[i][0,:]
        itrw=w_all[i][0,:]

    #print(itrT.shape,'shpa')

    T_t.append( itrT )
    q_t.append( itrq )
    u_t.append( itru )
    v_t.append( itrv )
    w_t.append( itrw )


#plt.plot(T_t[0][:],z_all[may][0,:],'r+')
#plt.plot(T_all[0][0,:],z_all[0][0,:]  ,'g*')
#plt.show()
#exit()

#sfc
tsf_2i=[]
sst_2i=[]
shf_2i=[]
lhf_2i=[]
tau_2i=[]

#lsf
zls_2i =[]
tls_2i =[]
tpls_2i=[]
qls_2i =[]
uls_2i =[]
vls_2i =[]
wls_2i =[]


size_lsf=[]
size_sfc=[]

for ex in exp:

    path1='%s/lasso_sam_%s/config'%(computer,ex)
    
    tls,zls,pressurels,p0,tpls,qls,uls,vls,wls=rs.read(path1,'lsf_f')

    size_lsf.append([tls.shape[0],tls[0]])

    zls_2i.append(zls)
    tls_2i.append(tls)
    tpls_2i.append(tpls)
    qls_2i.append(qls)
    uls_2i.append(uls)
    vls_2i.append(vls)
    wls_2i.append(wls)

    tsf,sst,shf,lhf,tau=rs.read_1d(path1,'sfc_f')


    size_sfc.append([tsf.shape[0],tsf[0]])

    tsf_2i.append(tsf)
    sst_2i.append(sst)
    shf_2i.append(shf)
    lhf_2i.append(lhf)
    tau_2i.append(tau)


mls     =np.argmax(size_lsf,axis=0)[0]

X1, Y1  =np.meshgrid(tls_2i[mls]-size_lsf[mls][1]+0.5,zls_2i[mls][0,:])


#print(X1[0,:])
#print(X1[0,:].shape[0])
#print(X1[0,:].shape[0],X1[0,:]+0.5)
#time_lsf=tls_2i[mls]-size_lsf[mls][1]+0.5
#print(time_lsf)
#print(tls_2i[mls])
#exit()
#exit()
#

tpls_all=[]
qls_all =[]
uls_all =[]
vls_all =[]
wls_all =[]

#for ex in exp:
for i in range (len(exp)):

    if (tls_2i[i].shape<tls_2i[mls].shape):

        print(tls_2i[i].shape,tls_2i[mls].shape,'lsf')

        interp_tpls =RegularGridInterpolator((tls_2i[i]-size_lsf[i][1]+0.5,zls_2i[i][0,:]), tpls_2i[i],method='cubic',bounds_error=False)
        interp_qls = RegularGridInterpolator((tls_2i[i]-size_lsf[i][1]+0.5,zls_2i[i][0,:]) , qls_2i[i],method='cubic',bounds_error=False)
        interp_uls = RegularGridInterpolator((tls_2i[i]-size_lsf[i][1]+0.5,zls_2i[i][0,:]) , uls_2i[i],method='cubic',bounds_error=False)
        interp_vls = RegularGridInterpolator((tls_2i[i]-size_lsf[i][1]+0.5,zls_2i[i][0,:]) , vls_2i[i],method='cubic',bounds_error=False)
        interp_wls = RegularGridInterpolator((tls_2i[i]-size_lsf[i][1]+0.5,zls_2i[i][0,:]) , wls_2i[i],method='cubic',bounds_error=False)

        tpls_1=interp_tpls((X1,Y1)).T
        qls_1=interp_qls( (X1,Y1)).T
        uls_1=interp_uls( (X1,Y1)).T
        vls_1=interp_vls( (X1,Y1)).T
        wls_1=interp_wls( (X1,Y1)).T

    else:

        tpls_1=tpls_2i[i]
        qls_1 = qls_2i[i] 
        uls_1 = uls_2i[i] 
        vls_1 = vls_2i[i] 
        wls_1 = wls_2i[i] 

    tpls_all.append(tpls_1)
    qls_all.append( qls_1)
    uls_all.append( uls_1)
    vls_all.append( vls_1)
    wls_all.append( wls_1)

#
#print(tpls_2i[0].shape)
#print(tpls_2i[mls].shape)
#print(tls_2i[0]-size_lsf[0][1])
#tls_2i[0]-size_lsf[0][1]

#plt.plot(tls_2i[0]  -size_lsf[0][1]+0.5  , tpls_2i[0][:,8] ,'*r')
#plt.plot(tls_2i[mls]-size_lsf[mls][1]+0.5,tpls_all[0][:,8] ,'+b')
#plt.show()

#print(var1.shape)
#exit()
#
###################################
###################################


#Large size sounding
msf=np.argmax(size_sfc,axis=0)[0]

sst_all=[]
shf_all=[]
lhf_all=[]
tau_all=[]


for i in range (len(exp)):

    if(tsf_2i[i].shape[0]<tsf_2i[msf].shape[0]):

        print(tsf_2i[i].shape[0],tsf_2i[msf].shape[0],'sfc')

        itrssf=np.interp(tsf_2i[msf]-size_sfc[msf][1]+0.5,tsf_2i[i]-size_sfc[i][1]+0.5,sst_2i[i][:])
        itrshf=np.interp(tsf_2i[msf]-size_sfc[msf][1]+0.5,tsf_2i[i]-size_sfc[i][1]+0.5,shf_2i[i][:])
        itrlhf=np.interp(tsf_2i[msf]-size_sfc[msf][1]+0.5,tsf_2i[i]-size_sfc[i][1]+0.5,lhf_2i[i][:])
        itrtau=np.interp(tsf_2i[msf]-size_sfc[msf][1]+0.5,tsf_2i[i]-size_sfc[i][1]+0.5,tau_2i[i][:])

    else:

        itrssf=sst_2i[i][:]
        itrshf=shf_2i[i][:]
        itrlhf=lhf_2i[i][:]
        itrtau=tau_2i[i][:]

    sst_all.append(itrssf)
    shf_all.append(itrshf)
    lhf_all.append(itrlhf)
    tau_all.append(itrtau)


#plt.plot(tsf_2i[may]-size_sfc[may][1]+0.5,sst_all[0],'+g')
#plt.plot(tsf_2i[0]  -size_sfc[0][1]  +0.5,sst_2i[0] ,'*r')
#plt.show()
#
#exit()


# To created the time at the first day of the year 
#it=0.5
#ft=1.125
#time_lsf=np.linspace(it,ft,len(tsf_2i[may]))
#+0.5 para comecar as 6 da manha
time_lsf=tls_2i[mls]-size_lsf[mls][1]+0.5
                                     
                                     
#it=0.5                               
#ft=1.25
#time=np.linspace(it,ft,len(time))

time=tsf_2i[msf]-size_sfc[msf][1]+0.5


theta_ls= np.mean(tpls_all,axis=0)
q_ls    = np.mean(qls_all ,axis=0)
u_ls    = np.mean(uls_all ,axis=0)
v_ls    = np.mean(vls_all ,axis=0)
w_ls    = np.mean(wls_all ,axis=0)

theta_inv = np.mean(T_t,axis=0)
q_sam     = np.mean(q_t,axis=0)
u         = np.mean(u_t,axis=0)
v         = np.mean(v_t,axis=0)
w         = np.mean(w_t,axis=0)

T_skin_mean = np.mean(sst_all,axis=0)
SH_mean     = np.mean(shf_all,axis=0)
LH_mean     = np.mean(lhf_all,axis=0)
Tau_mean    = np.mean(tau_all,axis=0)


# Check if the directory exists
if not os.path.exists(folder):
    # If it doesn't exist, create it
    os.makedirs(folder)


file11= open('%s/snd_%s'%(folder,label)  ,'w+')
file22= open('%s/lsf_%s'%(folder,label)  ,'w+')
file33= open('%s/sfc_%s'%(folder,label)  ,'w+')

file11.write("z[m]\tp[mb]\ttp[K]\tq[g/kg]\tu[m/s]\tv[m/s]\n")
file22.write("z[m]\tp[mb]\ttls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
file33.write("day\t\tsst(K)\t\tH(W/m2)\t\tLE(W/m2)\tTAU(m2/s2) \n")

pp=-999.0000

tl=[0.5,1.25]

f=0
for i in range(0,size[may],10):
    print(f,i,size[may]/10+1,int(size[may])/10+1)
    f+=1

#Only have in the beginning and in the end
for k in range(0,2): 

    file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(tl[k],int(size[may])/10,p0))
    #file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(time[k],size[may],p0))

    for i in range(0,size[may],10):
    #for i in range(0,size[may],1):

        file11.write("%f\t%f\t%f\t%f\t%f\t%f\n"%(z_all[may][0,i],pp,theta_inv[i],q_sam[i],u[i],v[i])) 


for k in range(0,len(time_lsf)): 

    file22.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(time_lsf[k],len(zls_2i[mls][0,:]),p0))

    for i in range(0,len(zls_2i[mls][0,:])):

        file22.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(zls_2i[mls][k,i],pp,theta_ls[k,i],q_ls[k,i],u_ls[k,i],v_ls[k,i],w_ls[k,i])) 


for k in range(0,len(time_lsf)): 

    file33.write("%f\t%f\t%f\t%f\t%f\n"%(time_lsf[k],T_skin_mean[k],SH_mean[k],LH_mean[k],Tau_mean[k])) 


file11.close()
file22.close()
file33.close()


print("______________")
print("Forcing %s was created in \n %s"%(label,folder))
print("______________")
