#**************************
#Program to average the forcing variables 
#of specific shallow day, to created a
#a single forcing.
##################################################
#The data from the SCM program was used as forcing. 
##################################################
#Note: The FORCING ARE CRETED IN UTC HOUR
#Note: The plots are in local Manuaus time UTC-4
#Data:01-02-23
#Created by: Jhonatan Aguirre
#**************************
#python 2.7
#
#paste: scm_lsf

import  os,sys
import  inspect

import  numpy as np
import  matplotlib as mpl
import  matplotlib.pyplot as plt

import matplotlib.ticker as ticker

#       To change the plot parameter 
from   	plotparameters 		import 	*

#To load the variable  in the datafile
from    variabletoload_go   import *

from    datetime import timedelta as dt, datetime

from    Parameters_forcing_iop import *

import   metpy.calc

from     metpy.units import units

#To find data in the array
import  data_own        as down

#Python standard library datetime  module
import  datetime    as dt

#Calculate necessary varibles to use as 
#foncing in SAM, usint METPY
from    calculate_variables_forcing import *

#Mean of days with diurnal profiles
import  diurnal_days as d_days 

#hours colors
import  hour_color as h_color 

from datetime import datetime

today = dt.datetime.today()

ano=2014

#hour
#UTC_HOUR  MANAUS_HOUR 
#    00       20 
#    04       24 
#    08       4 
#    12       8 
#    16       12 
#    20       16 
#    22       18 
#    24       20 
#    04       24 
#    08       4 


#The number of day must be mach with 
# exp_days.... if not the time delta 
# between the hour will be different

#the number of the days of the forcing
#beings 0

##############################
number_days=1


#0 hours from de fist day to 0 hours of next day  
#h=[0,20]

h=[0,20]
folder='scm_lsf'

#days Cloud Mask classification
#exp       =   [scm_iop1,scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2]
#exp_days  =   [(10,11,3,3),(3,4,9,9),(11,12,9,9),(1,2,10,10),(4,5,10,10),(8,9,10,10)]
#explabel  =   ['Sh_CA_masked_scm']

#days IOP1
#exp       =   [scm_iop1,scm_iop1,scm_iop1]
#exp_days  =   [(6,7,3,3),(15,16,3,3),(18,19,3,3)]
#explabel  =   ['Sh_IOP1_CA_scm_pure']


#days composite  IOP1
#exp       =   [scm_iop1,scm_iop1,scm_iop1,scm_iop1,scm_iop1,scm_iop1,scm_iop1,scm_iop1]
#exp_days  =   [(27,28,2,2),(6,7,3,3),(9,10,3,3),(10,11,3,3),(15,16,3,3),(16,17,3,3),(17,18,3,3),(18,19,3,3)]
#
##name of the composite
#explabel  =   ['shca_iop1_sam']
#label_nc  =   ['shca_iop1_scam']
#
##number of cases
#c1=8.0
#weight =1.0
##Weght function to do the average 
#wt=[   
#       weight/c1,weight/c1,weight/c1,weight/c1,
#       weight/c1,weight/c1,weight/c1,weight/c1,
#    ]


###days IOP2
#exp       =   [scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
#               scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
#               scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
#               scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
#               scm_iop2,scm_iop2
#              ]
#exp_days  =   [(2,3,9,9)  ,(3,4,9,9)  ,(4,5,9,9)   ,(9,10,9,9) ,(11,12,9,9),
#               (14,15,9,9),(15,16,9,9),(16,17,9,9) ,(19,20,9,9),(20,21,9,9),
#               (21,22,9,9),(22,23,9,9),(23,24,9,9) ,(26,27,9,9),(27,28,9,9),
#               (29,30,9,9),(1,2,10,10),(3,4,10,10) ,(5,6,10,10),(7,8,10,10),
#               (8,9,10,10),(9,10,10,10)
#               ]
#explabel  =   ['shca_iop2_sam']
#label_nc  =   ['shca_iop2_scam']
#
#weight=1.0
#c2=22.0
#wt=[   
#       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
#       weight/c2,weight/c2
#    ]

###################################################3
###################################################3
###################################################3
"""

#explabel  =   ['shca_sam_2day']
#label_nc  =   ['shca_scam_2day']
#weight=1.0
#c1=29.0
#c2=29.0

explabel  =   ['shca_sam' ]
label_nc  =   ['shca_scam']
weight    =    1.0
c1        =   30.0
c2        =   30.0
cases='d) ShCa'
legen=True


#explabel  =   ['shca_wg_sam_2days']
#label_nc  =   ['shca_wg_scam_2days']
#weight=0.5
#c1=8.0
#c2=21.0

####days IOP1_IOP2
exp       =   [
                scm_iop1,scm_iop1,scm_iop1,scm_iop1,scm_iop1,
                scm_iop1,scm_iop1,scm_iop1,
                scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
                scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
                scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
                scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
                scm_iop2,scm_iop2
               ]

#exp_days  =   [(27,1,2,3) ,(6,8,3,3)   ,(9,11,3, 3) ,(10,12,3,3) ,(15,17,3,3),
#               (16,18,3,3),(17,19,3,3) ,(18,20,3,3) ,
#               (2 ,4 ,9,9),(3 ,5 ,9,9) ,(4 ,6 ,9,9) ,(9,11,9,9)  ,(11,13,9,9),
#               (14,16,9,9),(15,17,9,9) ,(16,18,9,9) ,(19,21,9,9) ,(20,22,9,9),
#               (21,23,9,9),(22,24,9,9) ,(23,25,9,9) ,(26,28,9,9) ,(27,29,9,9),
#               (29,1,9,10),(1,3,10,10) ,(3,5,10,10) ,(5,7,10,10) ,(7 ,9,10,10),
#               (8,10,10,10)#,(9,11,10,10)
#               ]
#

exp_days  =   [(27,28,2,2),(6,7,3,3)   ,(9,10,3, 3) ,(10,11,3,3) ,(15,16,3,3),
               (16,17,3,3),(17,18,3,3) ,(18,19,3,3) ,
               (2 ,3 ,9,9),(3 ,4 ,9,9) ,(4 ,5 ,9,9) ,(9,10,9,9)  ,(11,12,9,9),
               (14,15,9,9),(15,16,9,9) ,(16,17,9,9) ,(19,20,9,9) ,(20,21,9,9),
               (21,22,9,9),(22,23,9,9) ,(23,24,9,9) ,(26,27,9,9) ,(27,28,9,9),
               (29,30,9,9),(1,2,10,10) ,(3,4,10,10) ,(5,6,10,10) ,(7,8,10,10),
               (8,9,10,10),(9,10,10,10)
               ]

#exp_days  =   [(27,27,2,2),(6,6,3,3)   ,(9,9,3, 3)  ,(10,10,3,3) ,(15,15,3,3),
#               (16,16,3,3),(17,17,3,3) ,(18,18,3,3) ,
#               (2 ,2 ,9,9),(3 ,3 ,9,9) ,(4 ,4 ,9,9) ,(9,9,9,9)  ,(11,11,9,9),
#               (14,14,9,9),(15,15,9,9) ,(16,16,9,9) ,(19,19,9,9) ,(20,20,9,9),
#               (21,21,9,9),(22,22,9,9) ,(23,23,9,9) ,(26,26,9,9) ,(27,27,9,9),
#               (29,29,9,9),(1,1,10,10) ,(3,3,10,10) ,(5,5,10,10) ,(7,7,10,10),
#               (8,8,10,10),(9,9,10,10)
#               ]
#

wt=[   
       weight/c1,weight/c1,weight/c1,weight/c1,weight/c1,
       weight/c1,weight/c1,weight/c1,
       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
       weight/c2,weight/c2,weight/c2,weight/c2,weight/c2,
       weight/c2,weight/c2          
]
"""

##days large chuva unicamente shallow
#exp       =   [scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2]
#exp_days  =   [(9,10,9,9),(19,20,9,9),(20,21,9,9),(26,27,9,9),(5,6,10,10)]
#explabel  =   ['shca_large_rain_iop2_sam']
#label_nc  =   ['shca_large_rain_iop2_scam']
#
#weight=1.0
#c1    =5.0
#wt=[   
#       weight/c1,weight/c1,weight/c1,weight/c1,
#       weight/c1
#    ]


#exp       =   [scm_iop1,scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2]
##exp_days  =   [(6,7,3,3),(9,10,9,9),(19,20,9,9),(20,21,9,9),(26,27,9,9),(5,6,10,10)]
#exp_days  =   [(6,8,3,3),(9,11,9,9),(19,21,9,9),(20,22,9,9),(26,28,9,9),(5,7,10,10)]
#explabel  =   ['shca_large_rain_iop12_sam']
#label_nc  =   ['shca_large_rain_iop12_scam']
#
#weight=1.0
#c1    =6.0
#wt=[   
#       weight/c1,weight/c1,weight/c1,weight/c1,
#       weight/c1,weight/c1
#    ]



###days large not rain
#exp       =   [scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2]
#exp_days  =   [(3,4,9,9),(15,16,9,9),(22,23,9,9),(29,30,9,9),(1,2,10,10)]
#explabel  =   ['shca_large_nr_sam']
#label_nc  =   ['ShCa_large_nr_scam']
#
#weight=1.0
#c1=5.0
#wt=[   
#       weight/c1,weight/c1,weight/c1,
#       weight/c1,weight/c1
#    ]

#"""

##days large all 
exp       =   [scm_iop1,scm_iop1,scm_iop1,scm_iop2,scm_iop2,scm_iop2,scm_iop2,
                scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2]
exp_days  =   [(27,28,2,2),(6,7,3,3),(10,11,3,3),(9,10,9,9),(19,20,9,9),(20,21,9,9),(5,6,10,10),
               ( 3, 4,9,9),(15,16,9,9),(22,23,9,9),(26,27,9,9),(29,30,9,9),(1,2,10,10)]
#exp_days  =   [(27,1,2,3),(6,8,3,3),(10,12,3,3),(9,11,9,9),(19,21,9,9),(20,22,9,9),(5,7,10,10),
#               ( 3,5,9,9),(15,17,9,9),(22,24,9,9),(26,28,9,9),(29,1,9,10),(1,3,10,10)]
explabel  =   ['shca_large_all_sam']
label_nc  =   ['shca_large_all_scam']
cases='c) Large'
legen=True
#
weight=1.0
c1    =13.0
wt=[   
       weight/c1,weight/c1,weight/c1,weight/c1,
       weight/c1,weight/c1,weight/c1,weight/c1,
       weight/c1,weight/c1,weight/c1,
       weight/c1,weight/c1
    ]

#"""

"""
####days medium
exp       =   [
                scm_iop1,scm_iop1,scm_iop1,
                scm_iop2,scm_iop2,scm_iop2,
                scm_iop2,scm_iop2,scm_iop2,
              ]

exp_days  =   [(9,10,3,3),(17,18,3,3),(15,16,3,3),
               (2,3,9,9),(14,15,9,9),(21,22,9,9),
               (27,28,9,9),(7,8,10,10),(8,9,10,10)]
#exp_days  =   [(9,11,3,3),(17,19,3,3),(15,17,3,3),
#               (2,4,9,9),(14,16,9,9),(21,23,9,9),
#               (27,29,9,9),(7,9,10,10),(8,10,10,10)]
explabel  =   ['shca_medium_sam']
label_nc  =   ['shca_medium_scam']
cases='b) Medium'
legen=False

weight=1.0
c1=9.0
wt=[   
       weight/c1,weight/c1,weight/c1,
       weight/c1,weight/c1,weight/c1,
       weight/c1,weight/c1,weight/c1
       ]

"""
"""
#days small
exp       =   [scm_iop1,scm_iop1,scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2]
#exp       =   [scm_iop1,scm_iop1,scm_iop2,scm_iop2,scm_iop2,scm_iop2,scm_iop2]
exp_days  =   [(18,19,3,3),(16,17,3,3),(4,5,9,9),(11,12,9,9),(16,17,9,9),(23,24,9,9),(3,4,10,10),(9,10,10,10)]
#exp_days  =   [(18,20,3,3),(16,18,3,3),(4,6,9,9),(11,13,9,9),(16,18,9,9),(23,25,9,9),(3,5,10,10)]
explabel  =   ['shca_small_sam_1days']
label_nc  =   ['shca_small_scam_1days']
cases='a) Small'
legen=False

weight=1.0
c1=8.0
wt=[   
       weight/c1,weight/c1,weight/c1,weight/c1,weight/c1,
       weight/c1,weight/c1,weight/c1
    ]
"""


color     =   [ 'navy']
cor1      =   [ 'red' ]
cor2      =   [ 'navy']


lim	      =   [0,0.025,0,4]


time= exp[0].tsec
data= exp[0].data
lev = exp[0].lev[::-1]


q        =   d_days.diurnal_main_days_lat_lon(exp,'q'    ,exp_days,h[0],h[1])
T        =   d_days.diurnal_main_days_lat_lon(exp,'T'    ,exp_days,h[0],h[1])
u        =   d_days.diurnal_main_days_lat_lon(exp,'u'    ,exp_days,h[0],h[1])
v        =   d_days.diurnal_main_days_lat_lon(exp,'v'    ,exp_days,h[0],h[1])
omega    =   d_days.diurnal_main_days_lat_lon(exp,'omega',exp_days,h[0],h[1])

q_adv_h  =   d_days.diurnal_main_days_lat_lon(exp,'divq',exp_days,h[0],h[1])
T_adv_h  =   d_days.diurnal_main_days_lat_lon(exp,'divT',exp_days,h[0],h[1])
s_adv_h  =   d_days.diurnal_main_days_lat_lon(exp,'divs',exp_days,h[0],h[1])

T_skin   =   d_days.diurnal_main_days_lat_lon(exp,'Tg'     ,exp_days,h[0] ,h[1])
SH       =   d_days.diurnal_main_days_lat_lon(exp,'shflx'   ,exp_days,h[0],h[1])
LH       =   d_days.diurnal_main_days_lat_lon(exp,'lhflx'   ,exp_days,h[0],h[1])
prec     =   d_days.diurnal_main_days_lat_lon(exp,'prec_srf',exp_days,h[0],h[1])


################################
#T_mean =   np.mean(T,axis=0) 
#q_mean =   np.mean(q,axis=0) 
#fig   = plt.figure()
#ax   = plt.axes()
#ax.plot(q_mean[0,:],exp[0].lev[:],'r')
#ax.plot(q_mean[0,:],exp[0].lev[:],'b*')
#plt.axis([275,320,0,5000])


T_mean,theta,theta_inv,q,t_ls,q_ls,s_ls,u,v,w,\
omega_mean,T_skin_mean,SH_mean,LH_mean,prec_mean,z,pa\
=variables_metpy_mean_scm(time,lev,q_adv_h,T_adv_h,s_adv_h,T,q,u,v,omega,prec,SH,LH,T_skin,wt)


#SAM NEED in this units
pressure =units.Quantity(pa,'Pa').to('mbar').magnitude
q_sam    =units.Quantity(q ,'kg/kg').to('g/kg').magnitude 


################################
#fig   = plt.figure()
#ax   = plt.axes()
#
#ax.plot(theta[1,:],z[1,:],'r')
#ax.plot(theta_inv[1,:],z[1,:],'b')
#
#plt.axis([275,320,0,5000])
#plt.show()
#exit()

label=explabel[0]

file11= open('%s/snd_%s'%(folder,label)  ,'w+')
file22= open('%s/lsf_%s_h'%(folder,label),'w+')
file23= open('%s/lsf_%s_p'%(folder,label),'w+')
file33= open('%s/sfc_%s'%(folder,label)  ,'w+')

file11.write("z[m]\tp[mb]\ttp[K]\tq[g/kg]\tu[m/s]\tv[m/s]\n")
file22.write("z[m]\tp[mb]\tsls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
file23.write("z[m]\tp[mb]\ttls(h)[K/s] \tqls[kg/kg/s]\tu[m/s]\tv[m/s]\tw[m/s]\n")
file33.write("day\t\tsst(K)\t\tH(W/m2)\t\tLE(W/m2)\tTAU(m2/s2) \n")

def velw_sfc_flx(u, v, w):
#    """Surface momentum flux [m^2/s^2]"""
#   print U_mag
    u_star = 0.28 # [m/s]

    U_mag = np.linalg.norm([u, v, w], axis=0)

    return -u_star**2.0 * np.array([u/U_mag, v/U_mag, w/U_mag])


#forcing data each 20 minutes  
#Define o tempo  dos dados num dia(Tem dados a cada 20 minutos)
#A unidade e dias!


#Initial day
#idi = dt.datetime(2022, 1, 1, h[0])
#idf = dt.datetime(2022, 1, number_days+1, h[1])


hfinal=number_days+h[1]/24.0
#time_sec=np.linspace(0,hfinal,len(SH_mean))
time_sec=np.linspace(0,hfinal,len(SH_mean),endpoint=False)

#print(time_sec) 
#exit()

#para trasformar em minutos 
#time_sec=time_sec*24*60
#print len(time_sec)
#exit()
#para definir em horas 
#time_sec=np.linspace(0,24,73)
#para transforar em minutos

ndtp =len(time_sec)
ndlev=len(lev)

time=time_sec

#NOTE:the forcing was created in local time, MANAUS -4UTC
###Manaus time
##h =[0,3,6,9,12,15,17,20,23,02]
#time=[0.0,0.125,0.25,0.375,0.5,0.625,0.75,0.875,1.0]

#NOTE:the forcing was created in UTC TIME
###UTC time
##h =[0 ,3 ,6,9,12,15,18,21,24,3]
##to UTC-4
##h =[20,23,2,5,8 ,11,14,17,20,23]



for k in range(0,len(time_sec)-1): 

    #if(time[k]>=dayinit and time[k]<=dayfin):

    file11.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(time[k],ndlev,pressure[0]))
    file22.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(time[k],ndlev,pressure[0]))
    file23.write("%f\t%d\t%f\tday\tlevels\tpres0\n"%(time[k],ndlev,pressure[0]))

    Tau         =   velw_sfc_flx(u[k,0],v[k,0],w[k,0]) 


    file33.write("%f\t%f\t%f\t%f\t%f\n"%(time[k],T_skin_mean[k],SH_mean[k],LH_mean[k],Tau[0])) 

    for i in range(0,ndlev):

        file11.write("%f\t%f\t%f\t%f\t%f\t%f\n"%(z[k,i],pressure[i],theta_inv[k,i],q_sam[k,i],u[k,i],v[k,i])) 
        file22.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(z[k,i],pressure[i],s_ls[k,i],q_ls[k,i],u[k,i],v[k,i],w[k,i])) 
        file23.write("%f\t%f\t%e\t%e\t%f\t%f\t%f\n"%(z[k,i],pressure[i],t_ls[k,i],q_ls[k,i],u[k,i],v[k,i],w[k,i])) 

file11.close()
file22.close()
file23.close()
file33.close()


## Writing NetCDF files to scam 
#
## Open a new NetCDF file to write the data to. For format, you can choose from
## 'NETCDF3_CLASSIC', 'NETCDF3_64BIT', 'NETCDF4_CLASSIC', and 'NETCDF4'


nc_out              = Dataset('%s/%s.nc'%(folder,label_nc[0]), 'w', format='NETCDF4')
nc_out.description  = " FORCING TO REPRESENT A COMPOSITE OF  \
PURE SHALLOW CONVECTION COLECTED IN THE OBSERTATIONAL CAMPAIGN \
GOAMAZON THROUGHT THE IOP1 AND IOP2. THE DATA IS REPRESENTED IN THE FIRST DAY OF 2014"


nc_out.history = "Created " + today.strftime("%d/%m/%y")
nc_out.author = "Jhonatan A. A manco"


time_nc = nc_out.createVariable('bdate', 'i4',())
nc_out.variables['bdate'][:] =  20140101 

# we can create the new dimension
## Even though we know the size, we are going to set the size to unknown
nc_out.createDimension('lon', 1)
nc_out.createDimension('lat', 1)

dtime =len(time_sec)
dlev=len(lev)
nc_out.createDimension('lev',dlev )
nc_out.createDimension('time', dtime)

##########################################
#time_nc = nc_out.createVariable('time', 'f4',('time',))
#
### Assign the dimension data to the new NetCDF file.
#nc_out.variables['time'][:] = time[:]


tsec_nc = nc_out.createVariable('tsec', 'f4',('time',))
tsec_nc.setncatts({'long_name': u"Time in seconds after 0Z on base date",\
                    'units': u"s",\
                    'statistic': u'none'})


nc_out.variables['tsec'][:] = time_sec[:]

##############################

lon_nc = nc_out.createVariable('lon', 'f4', ('lon'))
lon_nc.setncatts({'long_name': u"Longitude",\
                    'units': u"degrees",\
                    'var_desc': u"Longitude of ARM SITE MANACAPURU AMAZONAS",\
                    'statistic': u'none'})

nc_out.variables['lon'][:] = -60.00

##############################

lat_nc = nc_out.createVariable('lat', 'f4', ('lat'))
lat_nc.setncatts({'long_name': u"Latitude",\
                    'units': u"degrees",\
                    'var_desc': u"latidude of ARM SITE MANACAPURU AMAZONAS",\
                    'statistic': u'none'})

nc_out.variables['lat'][:] = -3.15


##############################

p_nc = nc_out.createVariable('lev', 'f4', ('lev',))
p_nc.setncatts({'long_name': u"Pressure",\
                    'units': u"Pa", 'level_desc': u'Surface',\
                    'var_desc': u"pressure from varanal analysis",\
                    'statistic': u'none'})

nc_out.variables['lev'][:] = pa[::-1]


##############################

sh_nc = nc_out.createVariable('shflx', 'f4', ('time','lat','lon'))
sh_nc.setncatts({'long_name': u"Surface sensible heat flux",\
                    'units': u"W/m2", 'level_desc': u'Surface',\
                    'var_desc': u"Surface Sensible heat flux from varanal analysis",\
                    'statistic': u'none\nM'})


sh_3d=np.zeros([SH_mean.shape[0],1,1])

sh_3d[:,0,0]=SH_mean[:]


nc_out.variables['shflx'][:] = sh_3d[:,0,0]


##############################
lh_nc = nc_out.createVariable('lhflx', 'f4', ('time','lat','lon'))
lh_nc.setncatts({'long_name': u"Surface latent heat flux",\
                    'units': u"W/m2", 'level_desc': u'Surface',\
                    'var_desc': u"Surface Latent  heat flux from varanal analysis",\
                    'statistic': u'none\nM'})
#nc_out.variables['lhflx'][:] = LH_mean[:]

lh_3d=np.zeros([LH_mean.shape[0],1,1])

lh_3d[:,0,0]=LH_mean[:]

nc_out.variables['lhflx'][:] = lh_3d[:]

##############################
phis_nc = nc_out.createVariable('phis', 'f4', ('lon','lat',))
phis_nc.setncatts({'long_name': u"Surface geopotential",\
                    'units': u"m2/s2", 'level_desc': u'Surface',\
                    'var_desc': u"Surface geopotential bomex has ",\
                    'statistic': u'none\nM'})

phis_3d=np.zeros([1,1])

phis_3d[0,0]=0.0

nc_out.variables['phis'][:] = phis_3d[:]

################################
ustar_nc = nc_out.createVariable('ustar', 'f4', ('time','lat','lon'))

ustar_nc.setncatts({'long_name': u"Surface frictional velocity",\
                    'units': u"m/s",\
                    'var_desc': u"Surface frictional velocity, bomex has",\
                    'statistic': u'none'})

ustar_3d=np.zeros([theta_inv.shape[0],1,1])

#bomex value
ustar_3d[:,0,0]=0.28

nc_out.variables['ustar'][:] = ustar_3d[:]


##############################

Tg_nc = nc_out.createVariable('Tg', 'f4', ('time','lat','lon'))

Tg_nc.setncatts({'long_name': u"Ground Temperature",\
                    'units': u"K",\
                    'var_desc': u"Ground Temperature from varanal analysis",\
                    'statistic': u'none'})

Tg_3d=np.zeros([theta_inv.shape[0],1,1])

Tg_3d[:,0,0]=T_skin_mean[:]

nc_out.variables['Tg'][:] = Tg_3d[:]

################################
##

Ps_nc = nc_out.createVariable('Ps', 'f4', ('time','lat','lon',))

Ps_nc.setncatts({'long_name': u"Surface pressure",\
                    'units': u"Pa",\
                    'var_desc': u"Surface pressure from varanal analysis",\
                    'statistic': u'none'})

Ps_3d=np.zeros([theta_inv.shape[0],1,1])

Ps_3d[:,0,0]=pa[0]

nc_out.variables['Ps'][:] = Ps_3d[:]

################################
##

Pt_nc = nc_out.createVariable('Ptend', 'f4', ('time','lat','lon',))

Pt_nc.setncatts({'long_name': u"Surface pressure tendency",\
                    'units': u"Pa/s",\
                    'var_desc': u"Surface pressure tendency, bomex has",\
                    'statistic': u'none'})

Pt_3d=np.zeros([theta_inv.shape[0],1,1])

Pt_3d[:,0,0]= 0.0

nc_out.variables['Ptend'][:] = Pt_3d[:]



##############################

T_nc = nc_out.createVariable('T', 'f4', ('time','lev','lat','lon'))
T_nc.setncatts({'long_name': u"Air Temperature",\
                    'units': u"K", 'level_desc': u'Surface',\
                    'var_desc': u"Air Temperature from varanal analysis",\
                    'statistic': u'none\nM'})

theta_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])

#theta_4d[:,:,0,0]=theta[:,:]
theta_4d[:,:,0,0]=T_mean[:,::-1]

nc_out.variables['T'][:] = theta_4d[:]

##############################
q_nc = nc_out.createVariable('q', 'f4', ('time','lev','lat','lon'))
q_nc.setncatts({'long_name': u"Water vapor mixing ratio",\
                    'units': u"kg/kg", 'level_desc': u'Surface',\
                    'var_desc': u"Water vapor mixin ratio from varanal analysis",\
                    'statistic': u'none\nM'})

q_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])

q_4d[:,:,0,0]=q[:,::-1]

nc_out.variables['q'][:] = q_4d[:]

##############################

u_nc = nc_out.createVariable('u', 'f4', ('time','lev','lat','lon'))
u_nc.setncatts({'long_name': u"u wind velocity ",\
                    'units': u"m/s", 'level_desc': u'Surface',\
                    'var_desc': u"u zonal  wind velocity  from varanal analysis",\
                    'statistic': u'none\nM'})

u_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])

u_4d[:,:,0,0]=u[:,::-1]

nc_out.variables['u'][:] = u_4d[:]

##############################

v_nc = nc_out.createVariable('v', 'f4', ('time','lev','lat','lon'))
v_nc.setncatts({'long_name': u"v wind velocity ",\
                    'units': u"m/s", 'level_desc': u'Surface',\
                    'var_desc': u"v meridional  wind velocity  from varanal analysis",\
                    'statistic': u'none\nM'})

v_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])

v_4d[:,:,0,0]=v[:,::-1]

nc_out.variables['v'][:] = v_4d[:]

##############################

o_nc = nc_out.createVariable('omega', 'f4', ('time','lev','lat','lon'))
o_nc.setncatts({'long_name': u"omega",\
                    'units': u"Pa/s", 'level_desc': u'Surface',\
                    'var_desc': u" vertical pressure velocity  from varanal analysis",\
                    'statistic': u'none\nM'})

o_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])

o_4d[:,:,0,0]=omega_mean[:,::-1]

nc_out.variables['omega'][:] = o_4d[:]

##############################

tls_nc = nc_out.createVariable('divT', 'f4', ('time','lev','lat','lon'))
tls_nc.setncatts({'long_name': u"Large scale temperature forcing",\
                      'units': u"K/s", 'level_desc': u'Surface',\
                      'var_desc': u" Large scale temperature forcing from varanal analysis",\
                      'statistic': u'none\nM'})
   
tls_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])

tls_4d[:,:,0,0]=t_ls[:,::-1]

nc_out.variables['divT'][:] = tls_4d[:]

##############################

qls_nc = nc_out.createVariable('divq', 'f4', ('time','lev','lat','lon'))
qls_nc.setncatts({'long_name': u" Large scale water vapor mixing ratio forcing",\
                      'units': u"kg/kg/s", 'level_desc': u'Surface',\
                      'var_desc': u" Large scale water vapor mixing ratio forcing from varanal analysis",\
                      'statistic': u'none\nM'})
   
qls_4d=np.zeros([theta_inv.shape[0],theta_inv.shape[1],1,1])

qls_4d[:,:,0,0]=q_ls[:,::-1]

nc_out.variables['divq'][:] = qls_4d[:]

##############################



nc_out.close()  # close the new file
print('Files were created' )
print('lsf_%s'%(explabel[0]) )
print('snd_%s'%(explabel[0]) )
print('sfd_%s'%(explabel[0]) )
print('%s.nc'%(explabel[0]) )


################################3


#Initial day
idi = dt.datetime(2022, 1, 1, h[0])
#idf = dt.datetime(2022, 1, 3, 10)
idf = dt.datetime(2022, 1, number_days+1, h[1])


#time of the composite day 
time=time_sec
lev = exp[0].lev[::-1]


#data= down.data_to_reference(data,exp[0].tsec[:])
data= down.data_to_reference(data,time[:])


ni,nf=down.data_n(idi,idf,data)


################################
#fig   = plt.figure()
#ax   = plt.axes()
#
#color = 'black'
#ax.set_xlabel(r'hour(UTC-4)', color=color)
##ax.set_ylabel('z [km]')
#plt.ylabel(r'') 
#
#color = 'black'
#
#ax.axis([idi,idf,0,400])

##-4 MANAUS LOCAL TIME
#ax.plot(data,SH_mean, color=color)
#
#ax.legend(frameon=False,loc='upper right')

#plt.savefig('%s/forcing_shf.pdf'%file_out, format='pdf',bbox_inches='tight' , dpi=1000)


hp        =   [6]

#used user parameter to plot(plotparameter.py
###########################################3

size_wg = 0.20
size_hf = 1.50


#plotsize(size_wg,size_hf, 1.0,'diurnal')
plotsize(size_wg,size_hf, 0.0,'diurnal')

fig   = plt.figure()
ax1   = plt.axes()

color = 'tab:red'
color2 = 'tab:green'

ax1.set_xlabel(r'$\mathrm{\theta}$ [K]', color='black')

ax1.set_ylabel('z [km]')

ax2 = ax1.twiny()  # instantiate a second axes that shares the same x-axis
#color = 'tab:blue'
ax2.set_xlabel(r'q [g/kg]', color='black')

ax1.axis([296,320,0,5])
ax2.axis([3 ,18.0,0,5])
ax1.grid()
#ax1.grid()

#fig.tight_layout()  # otherwise the right y-label is slightly clipped

ax1.text(300, 4, r'$\leftarrow$ q  ')
ax2.text(12 , 4, r'$\mathrm{\theta}  \rightarrow $ ')

for k in range(0,len(time)): 

        for i in range(0,len(hp)): 

            if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 
            #if hp[i]==data[k].hour and data[k].minute==00: 

                #print(data[k])

                line,color=h_color.color_hours(hp[i])

                #-4 MANAUS LOCAL TIME,it is in the reference time, ffrom 2021,12,31,20 horas
                ax1.plot(theta_inv[k,:], z[k,:]/1000.0,color=color,label='%d'%(hp[i]),dashes=line)

                ax2.plot(q[k,:]*1000.0, z[k,:]/1000.0,color=color,dashes=line)

#ax1.legend(frameon=False,loc='center right')
#ax1.text(302, 4.5, r'a)$\mathrm{\theta}$&q', fontsize=6, color='black')
ax1.text(300, 4.5, r'%s'%cases, fontsize=6, color='black')


if(legen):
    ax1.legend(frameon=False,loc='center right')


plt.savefig('%s/forcing_mean_tq_%s.pdf'%(file_out,cases[3::]),format='pdf',bbox_inches='tight' , dpi=1000)


hp        =   [6,9,12,15,18]
#hp        =   [6,8,10,12,14,16,18]

################################################################3

#plotsize(size_wg,size_hf, 1.0,'diurnal')
#plotsize(size_wg,size_hf, 0.0,'diurnal')

fig   = plt.figure()
ax   = plt.axes()

#ax.legend(frameon=False)

#ax.axis([-12,5,0,5])
#ax.text(-11.8, 3, r'u $\rightarrow$ ')
#ax.text( 1, 3, r'$\leftarrow$ v')

ax.axis([-10,1,0,5])
ax.text(-7, 3, r'$\leftarrow$u ')
ax.text(-1.5, 3, r'$\leftarrow$v')

plt.ylabel(r'z [km]') 
plt.grid()
#plt.ylabel(r'') 
#plt.xlabel(r' $\mathrm{ [ms^{-1}]}$ ') 


for k in range(0,len(time)): 

        for i in range(0,len(hp)): 

            if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 

                line,color=h_color.color_hours(hp[i])

                #-4 MANAUS LOCAL TIME
                ax.plot(u[k,:] ,z[k,:]/1000.0,label='%d'%(hp[i]),dashes=line,color=color)
                ax.plot(v[k,:] ,z[k,:]/1000.0,dashes=line,color=color)

ax.set_xlabel(r'$\mathrm{ [ms^{-1}]}$', color='black')

#ax.legend(frameon=False,loc='lower right')
#ax1.legend(frameon=False,loc='center right')
ax.text(-9, 4.5, r'%s'%(cases), fontsize=6, color='black')


if(legen):
    ax.legend(frameon=False,loc='lower left')

plt.savefig('%s/forcing_mean_uv_%s.pdf'%(file_out,cases[3::]), bbox_inches='tight' ,format='pdf', dpi=1000)


plt.show()
############################################################

fig   = plt.figure()
ax    = plt.axes()

#ax.legend(frameon=False)

ax.axis([-1.40,0.30,0,5])

plt.ylabel(r'z [km]') 
plt.xlabel(r'$\mathrm{ [cms^{-1}]}$ ') 
plt.grid()

for k in range(0,len(time)): 

        for i in range(0,len(hp)): 

            if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 

                line,color=h_color.color_hours(hp[i])

                #-4 MANAUS LOCAL TIME
                ax.plot(w[k,:]*100.0 ,z[k,:]/1000.0,label='%d'%(hp[i]),dashes=line,color=color)

#ax.legend(frameon=False,loc='lower right')
ax.text(-1.3, 4.5, r'%s w'%cases, fontsize=6, color='black')

if(legen):
    ax.legend(frameon=False,loc='center left')

plt.savefig('%s/forcing_mean_w_%s.pdf'%(file_out,cases[3::]), bbox_inches='tight' ,format='pdf', dpi=1000)
############################################################



################################
fig   = plt.figure()
ax   = plt.axes()

color = 'black'
ax.set_xlabel(r'$\mathrm{[Ks^{-1}]}$', color=color)
#ax.set_ylabel('z [km]')
ax.set_ylabel('z [km]')

ax.axis([-3.4e-5, 1.8e-5,0,5])
#ax.xaxis.set_major_locator(ticker.LinearLocator(3))

#fig.tight_layout()  # otherwise the right y-label is slightly clipped

#plt.ylabel(r'') 
#plt.xlabel(r'$\mathrm{ \theta_{ls}[Ks^{-1}]}$ ') 
plt.grid()


##to plot with scientific notation 
ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

for k in range(0,len(time)): 

        for i in range(0,len(hp)): 

            if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 

                line,color=h_color.color_hours(hp[i])

                #-4 MANAUS LOCAL TIME
                ax.plot(t_ls[k,:] ,z[k,:]/1000.0,label='%d'%(hp[i]),dashes=line,color=color)


#ax.legend(frameon=False,loc='lower right')
#ax.text(-2.9e-5, 4.5, r'd)$\mathrm{\theta_{ls}x10^{-5}}$', fontsize=6, color='black')
ax.text(-3.3e-5, 4.5, r'%s $\mathrm{\theta_{ls}}$'%cases, fontsize=6, color='black')
#ax.xaxis.get_offset_text().set_visible(False)

if(legen):
    ax.legend(frameon=False,loc='center right')

plt.savefig('%s/forcing_mean_tls_%s.pdf'%(file_out,cases[3::]), format='pdf',bbox_inches='tight' , dpi=1000)

################################
fig   = plt.figure()
ax   = plt.axes()

color = 'black'
ax.set_xlabel(r'$\mathrm{[g kg^{-1} s^{-1}]}}$', color=color)
ax.set_ylabel('z [km]')
#plt.ylabel(r'') 
plt.grid()

color = 'black'

ax.axis([-2.80e-5,1.8e-5,0,5])

#ax.xaxis.set_major_locator(ticker.LinearLocator(3))

#plt.tight_layout()  # otherwise the right y-label is slightly clipped
##to plot with scientific notation 
#ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

#ax.xaxis.set_minor_locator(locatormin)

for k in range(0,len(time)): 

        for i in range(0,len(hp)): 

            if hp[i]==data[k].hour and data[k].minute==00 and data[k].day==1: 

                line,color=h_color.color_hours(hp[i])

                #-4 MANAUS LOCAL TIME
                ax.plot(q_ls[k,:]*1000 ,z[k,:]/1000.0,label='%d'%(hp[i]),dashes=line,color=color)

if(legen):
    ax.legend(frameon=False,loc='center right')

#ax.text(-2.5e-8, 4.5, r'e)$\mathrm{q_{ls}x10^{-8}}$', fontsize=6, color='black')
ax.text(-2.4e-5, 4.5, r'%s $\mathrm{q_{ls}}$'%cases, fontsize=6, color='black')
#ax.xaxis.get_offset_text().set_fontsize(10)
#ax.xaxis.set_offset_position('right')

#10-5
#ax.xaxis.get_offset_text().set_visible(False)

#ax.text( 1.8e-8, -0.1, '1e-8', fontsize=6)


plt.savefig('%s/forcing_mean_qls_%s.pdf'%(file_out,cases[3::]), format='pdf',bbox_inches='tight' , dpi=1000)


plt.show()
