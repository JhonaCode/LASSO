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

##Small
exp          =  [f060615,f270615,
                 f290815,f250616,
                 f180816,f300816] 

##Big
exp          =  [f090615,f010815,
                 f100616,f110616,
                 f190616,f160716,
                 f190716,f200716,
                 ] 
##Não existe
#exp          =  [
#                 f180516,f140616,
#                 f190616] 


#var     =  ['MCUP','WOBS','RELH','CLD']###,'RELH','WOBS',]
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

l1=[(0,0.1),(-4,4),(5,95),(0,30)] 
lim         =[
                l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,
            ]

v1=[1,100,1,100]
var_to      =  [
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
                    v1,v1,v1,v1,v1, 
               ]


a1=[(0,5.0),(0,5.0),(0,5.0),(0,5.0)]
alt         =  [
                a1,a1,a1,a1,a1,a1,
                a1,a1,a1,a1,a1,a1,
                a1,a1,a1,a1,a1,a1,
               ]

s1=[True,True,True,True]
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


co1=['black','black','black','black']
color       =  [
                co1,co1,co1,co1, 
                co1,co1,co1,co1, 
                co1,co1,co1,co1, 
                co1,co1,co1,co1, 
               ]

xlabel      ='uMF [kgm$^{2}$s$^{-1}]$'


g3           =  ( 0.00,4.0,'lower right',True,True,True)
lrh          =  ( 70.0,4.0,'lower right',True,True,True)

g1=[g3,g3,g3,g3]

leg_loc      =  [ 
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                    g1,g1,g1,g1,g1,
                ]

dc.diurnal_hours_exp_var_sam(exp,var,alt=alt,var_to=var_to,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)
