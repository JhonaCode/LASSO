######################################
######################################
#Program to plot meteorological date 
#of the OUT_STAT files 
#of SAM with python and  Netcdf library.
#
#Create by: Jhonatan Aguirre 
#Date:23/03/1010
#working 
######################################
######################################

import  sam_python.temporal_plot   as temp

from    Parameters_sam import *

import  matplotlib.pyplot as plt

#Defined the name of the experiments defined in Parameters files 
#separate with colon

#LARGE
exp          =  [
                all1,large,
                medium,small
                ] 

explabel1     = [
                 ['Todos'  ,'Todos'  ,'Todos'   ],
                 ['Grande' ,'Grande' ,'Grande'  ],
                 ['Médio'  ,'Médio'  ,'Médio'   ],
                 ['Pequeno','Pequeno','Pequeno' ],
                ] 

var     =  ['LHF','SHF','PREC']


v1=[1,1,1]
var_to      =  [
                v1,v1,v1,v1,v1,
               ]


a0=(0,150.0,4)
a1=[a0,a0,a0,a0]
alt         =  [
               a0,a0,a0,a0, 
               ]

#co1='RdBu_r'
co1         =  ['red','blue','magenta','green']

color       =  [
                co1,co1,co1
               ]

s1=[True]
show       =  [ s1,s1,s1,s1,s1,s1, s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
               ]

#X           =  'Hours LT (UTC-4)'
X           =  'Horas HL (UTC-6)'
Y           =  'Sensible Heat FLux $\mathrm{ [W m^{-2}]}$'
Y2          =  'Latent   Heat FLux $\mathrm{ [W m^{-2}]}$'
Y3          =  'Precipitation  [mm]'

l1          =  [([X,Y], ['a)' ,(2024,1,1,6,30),290],[False,'upper right'],[0.45,0])]
l2          =  [([X,Y2],['b)' ,(2024,1,1,6,30),210],[False,'upper right'],[0.45,0])]
l3          =  [([X,Y3],['c)' ,(2024,1,1,6,30),5.2],[False,'upper right'],[0.45,0])]


plot_def    =  [
                l1,l2,l3
                ]


temp.temporal_plot_var_exp(exp,var=var,explabel1=explabel1,explabel2=explabel1,alt=alt,color=color,var_to=var_to,plot_def=plot_def,show=show)
#two.plot2d_contour(exp,var=var,contour=contour,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)


