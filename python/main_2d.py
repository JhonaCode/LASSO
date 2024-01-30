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

from    files_direction import *

from    Parameters_dict import *

import  matplotlib.pyplot as plt

#Defined the name of the experiments defined in Parameters files 
#separate with colon

#@exp          =  [f060615,f090615,f270615,
#@                 f010815,
#@                 f290815,f180516,f300516,
#@                 f140616,f250616,
#@                 f160716,f190716,f200716,
#@                 f190816,f300816] 

exp          =  [f060615,f090615,f270615,
                 f010815,f290815,
                 f180516,f300516,
                 f100616,f110616,f140616,
                 f190616,f250616,
                 f160716,f190716,f200716,
                 f180816,f190816,
                 f300816] 

var     =  ['MCUP','RELH','WOBS','CLD']
#var     =  ['QVOBS']#,'RELH','WOBS','CLD']

#print(f060615.z[0:80])
#exit()


cmf=(00.0,0.15,21,'kg/m/s2')
ccf=(0.0,25,21,'%')
crh=(0,100,21,'%')
cw =(-3,3,21,'cm/s')
cq =(0,16,21,'g/kg')

c1=[cmf,crh,cw,ccf]
#c1=[cq,crh,cw,ccf]

contour      =[
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
              ]

#v1=[1,1,100,100]
v1=[1,1,100,100]
var_to      =  [
                v1,v1,v1,v1,v1,
                v1,v1,v1,v1,v1,
                v1,v1,v1,v1,v1,
                v1,v1,v1,v1,v1,
               ]

#figures name
exp_label   =  [ 
                    ['uMF']
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
co1         =  ['whbuyl','RdBu_r','RdBu_r','whbuyl']

color       =  [
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
               ]
s1=[False,False,False,False]
#s1=[True,True,True,True,]
show       =  [
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
               ]


a0          =  (True,True,True ,True,0.35,1.34)
a1          =  [a0,a0,a0,a0] 
axis_on     =  [
                a1,a1,a1,a1,a1,
                a1,a1,a1,a1,a1,
                a1,a1,a1,a1,a1,
                a1,a1,a1,a1,a1,
               ]


e1=['','','','']

explabel1=[
            e1,
          ]

#d1=[(2014,1,1,8,00),(2014,1,1,20,5)]
#days        = [
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#                [d1,d1],
#              ]


#two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)

two.plot2d_contour(exp,var=var,contour=contour,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)




