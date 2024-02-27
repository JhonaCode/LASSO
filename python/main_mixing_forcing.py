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

import forcings.read_sam_forcing as rs

#from    Parameters_forcing_iop import *
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

#Mean of days with diurnal profiles
#import  diurnal_days as d_days 

#hours colors
#import  hour_color as h_color 


#To load the variable  in the datafile
#from    variabletoload_go   import *

import   metpy.calc
from     metpy.units import units


namef ='lsf_cases'
pyf='/dados/bamc/jhonatan.aguirre/git_repositories/LASSO/python'
folder='%s/%s'%(pyf,namef)


label       ='testeeeeee_lsf'
ex1         ='medium_lsf'
ex2         ='large_lsf'


#SND

#exp1
#########
time1,z1,pressure1,p01,T1,q1,u1_sn,v1_sn,w1_sn=rs.read(folder,'/snd_'+ex1)
#exp2
#########
time2,z2,pressure2,p02,T2,q2,u2_sn,v2_sn,w2_sn=rs.read(folder,'/snd_'+ex2)


#########
size=(T1.shape[1],T2.shape[1])

#print(size)

#############LSF

#exp1
#########
tls1,zls1,pressurels1,p01,tpls1,qls1,uls1,vls1,wls1=rs.read(folder,'/lsf_'+ex1)

#exp2
#########
tls2,zls2,pressurels2,p02,tpls2,qls2,uls2,vls2,wls2=rs.read(folder,'/lsf_'+ex2)

########SND
tsf1,sst1,shf1,lhf1,tau1=rs.read_1d(folder,'/sfc_'+ex1)
tsf2,sst2,shf2,lhf2,tau2=rs.read_1d(folder,'/sfc_'+ex2)


#Large size sounding
may=np.argmax(size)


if may==0:

  itrT1 =    T1[0,:]
  itrq1 =    q1[0,:]
  itru1 = u1_sn[0,:]
  itrv1 = v1_sn[0,:]
  itrw1 = w1_sn[0,:]
  z_all = z1

  itrT2=np.interp(z1[may,:],z2[0],   T2[0,:])
  itrq2=np.interp(z1[may,:],z2[0],   q2[0,:])
  itru2=np.interp(z1[may,:],z2[0],u2_sn[0,:])
  itrv2=np.interp(z1[may,:],z2[0],v2_sn[0,:])
  itrw2=np.interp(z1[may,:],z2[0],w2_sn[0,:])



if may==1:

  itrT2=   T2[0,:]
  itrq2=   q2[0,:]
  itru2=u2_sn[0,:]
  itrv2=v2_sn[0,:]
  itrw2=w2_sn[0,:]
  z_all=z2

  itrT1=np.interp(z2[may,:],z1[0],   T1[0,:])
  itrq1=np.interp(z2[may,:],z1[0],   q1[0,:])
  itru1=np.interp(z2[may,:],z1[0],u1_sn[0,:])
  itrv1=np.interp(z2[may,:],z1[0],v1_sn[0,:])
  itrw1=np.interp(z2[may,:],z1[0],w1_sn[0,:])



#SND
time     =time1
theta_inv=itrT1
q_sam    =itrq1
u        =itru1
v        =itrv1
w        =itrw1

#LSF
tls     = tls1
theta_ls=tpls1
q_ls    = qls1
u_ls    = uls1
v_ls    = vls1
w_ls    = wls1

zls  =zls1

#SFC    
tsf   = tsf1
T_skin =sst1 
SH     =shf1
LH     =lhf1
Tau    =tau1


p0=p01




# To created the time at the first day of the year 
it=0.5
ft=1.25
time_lsf=np.linspace(it,ft,len(tsf))

it=0.5
ft=1.5
time=np.linspace(it,ft,len(time))




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


for k in range(0,len(time)): 

    file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(time[k],size[may],p0))

    #for i in range(0,size[may],10):
    for i in range(0,size[may]):

        file11.write("%f\t%f\t%f\t%f\t%f\t%f\n"%(z_all[0,i],pp,theta_inv[i],q_sam[i],u[i],v[i])) 


for k in range(0,len(time_lsf)): 

    file22.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(time_lsf[k],len(zls[0,:]),p0))

    for i in range(0,len(zls[0,:])):

        file22.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(zls[k,i],pp,theta_ls[k,i],q_ls[k,i],u_ls[k,i],v_ls[k,i],w_ls[k,i])) 

for k in range(0,len(time_lsf)): 

    file33.write("%f\t%f\t%f\t%f\t%f\n"%(time_lsf[k],T_skin[k],SH[k],LH[k],Tau[k])) 


file11.close()
file22.close()
file33.close()


#plt.plot(theta_inv[:],z_all[0,:])
#plt.plot(T1[0,:],z1[0,:])
#plt.show()
