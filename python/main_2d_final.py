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

import  sam_python.two_dimensional   as two

from    Parameters_sam_final import *

import  matplotlib.pyplot as plt

# to work without display
#plt.switch_backend('agg')

#Defined the name of the experiments defined in Parameters files 
#separate with colon


exp          =  [
                #small,
                medium,
                #large,
                #todos,
                ] 

explabel1     = [
                 [r'a)Pequeno Fm $ ' ],
                 [r'b)Médio   Fm $ ' ],
                 [r'c)Grande  Fm $'  ],
                 [r'c)Todos  Fm $'  ],
                ] 

var     =  ['MCUP']

label=['_final']


cmf=(00.0,0.15,21,r'kg/m/s$^{2}$')
ccf=(0.0,50,21,'%')
crh=(0,100,21,'%')
cw =(-3,3,21,'cm/s')
#cq =(0,16,21,'g/kg')
cq =(0.0,0.1,21,'g/kg')


#c1=[cmf,ccf,cq]
c1=[cmf]
#c1=[cq,crh,cw,ccf]

contour      =[
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
              ]

#v1=[1,1,100,100]
#v1=[1,100,1]
v1=[1]
var_to      =  [
                v1,v1,v1,v1,v1,
                v1,v1,v1,v1,v1,
                v1,v1,v1,v1,v1,
                v1,v1,v1,v1,v1,
               ]


a0=(0,5.0)
a1=[a0,a0,a0,a0]
alt         =  [
               a1,a1,a1,a1,a1, 
               a1,a1,a1,a1,a1, 
               a1,a1,a1,a1,a1, 
               a1,a1,a1,a1,a1, 
               ]

#co1='RdBu_r'
co1         =  ['whbuyl','whbuyl','whbuyl', 
                'whbuyl','whbuyl','whbuyl'
                ]

color       =  [
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
               ]
#s1=[True,False,False,False]
s1=[True,True,True,True,]
#s1=[False,False,True,True,]
show       =  [ s1,s1,s1,s1,s1,s1, s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
               ]


                #barra,x,y,lfc..
a0          =  (False,True,False,False,0.35,0.00)
ab          =  (True ,True,False,False,0.35,1.28)
abz         =  (True ,True,True ,False,0.35,1.34)
az          =  (False,True,True ,False,0.35,0.06)

a1          =  [a0,a0,a0,a0] 
a2          =  [az,az,az,az] 
a3          =  [ab,ab,ab,ab] 
a4          =  [abz,abz,abz,abz] 
axis_on     =  [
                a4,
                a4,a4,a4,
                a4,a4,a4,
               ]


two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show,label=label)
#two.plot2d_contour(exp,var=var,contour=contour,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)


