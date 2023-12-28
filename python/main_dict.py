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
# path of the ncfile
#
from    Parameters_dict import *

################################################################ 
# to defined fig out direction 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.diurnal   as dc


#Defined the name of the experiments defined in Parameters files 
#separate with colon

exp          =  [f060615,f090615,f270615,
                 f010815,
                 f290815,f180516,f300516,
                 f140616,f250616,
                 f160716,f190716,f200716,
                 f190816,f300816] 


var     =  ['MCUP']###,'RELH','WOBS',]

#lim         =  [
#                (0,0.1),(0,15),(0,3),
#                (-0.7E-3,5.5E-3),(-1.5,2.0),(20,90),
#                (0, 0.04),(-20,20),(-80,90),
#               ]
#
#var_to      =  [
#                    1, 100, 1,  
#                    9.81/(exp[0].THETA[10,10]*1005.0*exp[0].RHO[10,10]), 100, 1,  
#                    1, 1 , 1,                    
#               ]
###figures name
##exp_label   =  [ 
##                 'uMF', 'CF'  , 'TKE',
##                 'B'  , 'Wobs', 'RH',
##                 'CLW', 'Q1'  , 'Q2',
##               ]

l1=[(0,0.1)] 
lim         =[
                l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,
            ]

v1=[1]
var_to      =  [
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
               ]

#figures name
#exp_label   =  [ 
#                    ['uMF']
#               ]

a1=[(0,5.0)]
alt         =  [
                a1,a1,a1,a1,a1,a1,
                a1,a1,a1,a1,a1,a1,
                a1,a1,a1,a1,a1,a1,
               ]

s1=[True]
show       =  [
                s1,s1,s1,s1,
                s1,s1,s1,s1,
                s1,s1,s1,s1,
                s1,s1,s1,s1,
                s1,s1,s1,s1,
               ]
diurnal       =  [
                s1,s1,s1,s1,
                s1,s1,s1,s1,
                s1,s1,s1,s1,
                s1,s1,s1,s1,
                s1,s1,s1,s1,
               ]


co1=['black']
color       =  [
                co1,co1,co1,co1, 
                co1,co1,co1,co1, 
                co1,co1,co1,co1, 
                co1,co1,co1,co1, 
               ]

xlabel      ='uMF [kgm$^{2}$s$^{-1}]$'



g1           =  [( 0.00,4.0,'lower right',True,True,True)]
lrh          =  ( 70.0,4.0,'lower right',True,True,True)

leg_loc      =  [ 
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                ]

dc.diurnal_hours_exp_var_sam(exp,var,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)
