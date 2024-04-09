################################################################
#Program to plot meteorological date
#of the OUT_STAT files of SAM with
#python and  Netcdf library.

###########################
#Modified:23/01/23
# To run using the same files
# python_src files

###########################
#Create by: Jhonatan Aguirre
#Date:07/04/2022
#working
#python 3.9

################################################################
# To activate this environment, use
#
# $ conda activate py37
# Went panda is use
# To deactivate an active environment, use
#
# $ conda deactivate
#
# path of the ncfile or data to plot
#from    Parameters_sam_final import *
from    Parameters_dict import *
from    Parameters_sam_wrf import *
from    Parameters_sam_wrf_2019 import *

################################################################ 
# to defined fig out direction, and others important parameters 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.diurnal   as dc

import  datetime as dt 

import  matplotlib.pyplot as plt
# to work without display
#plt.switch_backend('agg')


#separate with coma

var         =   ['MCUP']        

"""
exp         =  [ 
                    f270615  ,###)1
                    f290815  ,###)2
                    f180516  ,###)3
                    f20181001,###)4
                    f20180606,###)5
                    f20180522,###)6
                    f20180707,###)7
                    f20180901,###)8
                    f20180916,###)9
                    f20180731,###)10
                    f20180917,###)11
                    f20180514,###)12
                    f20180709,###)13
                    f20180805,###)14
                    f20180918,###)15
                    f20190404,###)16
                    f20190512,###)17
                    f20190607,###)18
                    f20190709,###)19
                    f20190704,###)20
                    f20190701,###)21
                    f20190617,###)22
                    f20190626,###)23
#############################
                    f060615,  ###'c)06-06-2015'
                    f180816,  ###'o)18-08-2016'
                    f250616,  ###'n)25-06-2016'
                    f20180911,###'a)01-09-2018'
                    f20180619,###'e)19-06-2018'
                    f20180914,###'g)14-09-2018'
                    f20190901,###'h)01-09-2019'
                    f20181002,###'i)02-10-2018'
                    f20180712,###'j)12-07-2018'
                    f20180618,###'p)18-06-2018'
                    f20180705,###'q)05-07-2018'
                    f20180710,###'m)10-07-2018'
                    f20190707,###'k)07-07-2019'
                    f20190517,###'d)17-05-2019'
                    f20190805,###'f)05-08-2019'
                    f20190612,###'b)12-06-2019'
                    f20190714,###'l)14-07-2019'
################################
                    f300816,
                    f20180711,
                    f100616,
                    f20190804,
                    f20180523,
                    f200716,
                    f20180811,
                    f160716,
                    f090615,
                    f190616,
                    f010815,
                ]
"""
#FInal, com o gráfico em tres diferentes horas.
exp         =  [ 
                    f270615  ,###)1
                    f290815  ,###)2
                    f180516  ,###)3
                    f20180606,###)4
                    f20180731,###)5
                    f20180901,###)6
                    f20180917,###)7
                    f20190704,###)8
                    f20190709,###)9
                    ##nuven sozinha
                    #f20180805,###)9
                    ##nuven sozinha
                    #f20190512,###)10
                    #muito pequena
                    #f20180918,###)14
                    #small
                    f060615,  ###)1)06-06-2015'
                    f20180522,###)2
                    f20180707,###)3
                    f20180911,###)4
                    f20180916,###)5
                    f20181001,###)6
                    f20190404,###)7
                    f20190607,###)8
                    f20190612,###)9
                    f20190701,###)10
#############################
                    #medium
                    f250616,  ###)01)
                    f180816,  ###)02)
                    f20180514,###)03
                    f20180618,###)04)
                    f20180619,###)05)
                    f20180705,###)06)
                    f20180709,###)07)
                    f20180712,###)08)
                    f20180914,###)09)
                    f20181002,###)10)
                    f20190517,###)11)
                    f20190617,###)12)
                    f20190626,###)13)
                    f20190707,###)14)
                    f20190714,###)15)
                    f20190805,###)16)
                    f20190901,###)17)
################################    
                    #large
                    f090615,    ###)1
                    f010815,    ###)2
                    f100616,    ###)3
                    f190616,    ###)4
                    f160716,    ###)5
                    f200716,    ###)6
                    f300816,    ###)7
                    f20180523,  ###)8
                    f20180710,  ###)9
                    f20180711,  ###)10
                    f20190804,  ###)11
                    f20180811,  ###)12
                ]

exp_label   =  [
                    'sf',###)1
                    'sf',###)2
                    'sf',###)3
                    'sf',###)4
                    'sf',###)5
                    'sf',###)6
                    'sf',###)7
                    'sf',###)8
                    'sf',###)9
                    's' ,###)1
                    's' ,###)2
                    's' ,###)3
                    's' ,###)4
                    's' ,###)5
                    's' ,###)6
                    's' ,###)7
                    's' ,###)8
                    's' ,###)9
                    's' ,###)10
                    #
                    'm',###)1
                    'm',###)2
                    'm',###)3
                    'm',###)4
                    'm',###)5
                    'm',###)6
                    'm',###)7
                    'm',###)8
                    'm',###)9
                    'm',###)10
                    'm',###)11
                    'm',###)12
                    'm',###)13
                    'm',###)14
                    'm',###)15
                    'm',###)16
                    'm',###)17
                    #
                    'l',###)1
                    'l',###)2
                    'l',###)3
                    'l',###)4
                    'l',###)5
                    'l',###)6
                    'l',###)7
                    'l',###)8
                    'l',###)9
                    'l',###)10
                    'l',###)11
                    'l',###)12
                ]      


fig_name='teste'

lim         =  [
                (0,0.05),(0,0.05),(0,0.05),(0,0.05),
                (0,0.05),(0,0.05),(0,0.05),(0,0.05),
                (0,0.05),(0,0.05),(0,0.05),(0,0.05),
                (0,0.05),(0,0.05),(0,0.05),(0,0.05),
                (0,0.05),(0,0.05),(0,0.05),(0,0.05),
               ]

var_to      =  [
                    1 ,1,1,1,  
                    1 ,1,1,1,  
                    1 ,1,1,1,  
                    1 ,1,1,1,  
                    1 ,1,1,1,  
                    1 ,1,1,1,  
               ]

xlabel='x'

l1             =  ( [0.002,0.150],[0.02,3.30],'center right',True,True,True,xlabel) 

leg_loc      =  [ 
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                  l1,l1,l1,l1,
                ]


color       =  [
                ['black',[2,1,1,1]],
                ['black',[2,1,1,1]],
                ['black',[2,1,1,1]],
                ['black',[2,1,1,1]],
               ]

show       =  [
                True,True,True,True,
                True,True,True,True,
                True,True,True,True,
                True,True,True,True,
               ]

diurnal     =  [
                True,True,True,True,
                True,True,True,True,
                True,True,True,True,
                True,True,True,True,
              ]

a1=[0,5]
alt         =  [
                a1,a1,a1,a1,
                a1,a1,a1,a1,
               ]

fig1,ax1=dc.diurnal_exp_var_hour_sam_pdf(exp,var,11,fig_name,explabel=exp_label,
        alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

fig2,ax2=dc.diurnal_exp_var_hour_sam_pdf(exp,var,12,fig_name,explabel=exp_label,
        alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

fig3,ax3=dc.diurnal_exp_var_hour_sam_pdf(exp,var,14,fig_name,explabel=exp_label,
        alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

plt.show()
