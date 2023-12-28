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

exp          =  [f060615,f090615,f270615,
                 f010815,
                 f290815,f180516,f300516,
                 f140616,f250616,
                 f160716,f190716,f200716,
                 f190816,f300816] 


var     =  ['MCUP']###,'RELH','WOBS',]

#print(f060615.z[0:80])
#exit()


cmf=(00.0,0.15,21,'kg/m/s2')
ccf=(0.0,25,21)
crh=(10,90,21)
cw =(-3,3,21)

contour      =[
                [cmf],[cmf],[cmf],
                [cmf],
                [cmf],[cmf],[cmf],
                [cmf],[cmf],
                [cmf],[cmf],[cmf],
                [cmf],[cmf],
              ]

v1=[1]
var_to      =  [
                    [v1],[v1],[v1], 
                    [v1],[v1],[v1], 
                    [v1],[v1],[v1], 
                    [v1],[v1],[v1], 
                    [v1],[v1],[v1], 
               ]

#figures name
exp_label   =  [ 
                    ['uMF']
               ]

a1=(0,5.0)
alt         =  [
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
               ]

#co1='RdBu_r'
co1         =  'whbuyl'

color       =  [
                [co1],[co1],[co1],[co1],[co1],
                [co1],[co1],[co1],[co1],[co1],
                [co1],[co1],[co1],[co1],[co1],
                [co1],[co1],[co1],[co1],[co1],
               ]
s1=False
show       =  [
                [s1],[s1],[s1],[s1],[s1], 
                [s1],[s1],[s1],[s1],[s1], 
                [s1],[s1],[s1],[s1],[s1], 
                [s1],[s1],[s1],[s1],[s1], 
               ]


a1          =  (True,True,True ,True,0.35,1.34)
axis_on     =  [
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
                [a1],[a1],[a1],[a1],
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


two.plot2d_contour(exp,var=var,contour=contour,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)




