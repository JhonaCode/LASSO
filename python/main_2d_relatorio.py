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

#exp          =  [
#                 f060615,f090615,f270615,
#                 f010815,f290815,
#                 f180516,f300516,
#                 f100616,f110616,f140616,
#                 f190616,f250616,
#                 f160716,f190716,f200716,
#                 f180816,f190816,
#                 f300816
#                ] 
#
#LARGE
exp          =  [
                 f090615,f010815,f100616,
                 f110616,f190616,f160716,
                 f190716,f200716
                ]

explabel1    =  [
                 ['a)09-06-2015','a)09-06-2015','a)09-06-2015'],['b)01-08-2015','b)01-08-2015','b)01-08-2015'],
                 ['c)10-06-2016','c)10-06-2016','c)10-06-2016'],
                 ['d)11-06-2016','d)11-06-2016','d)11-06-2016'],['e)19-06-2016','e)19-06-2016','e)19-06-2016'],
                 ['f)16-07-2016','f)16-07-2016','f)16-07-2016'],
                 ['g)19-07-2016','g)19-07-2016','g)19-07-2016'],['h)20-07-2016','h)20-07-2016','h)20-07-2016']
                ]

#Normal
#exp          =  [
#
#                 f060615,f270615,f250616,
#                 f290815,f180816,f300816,
#                 f300516,
#                ] 

#no shca
#exp          =  [
#                 f180516
#                 f140616,f190816,
#                ] 
#explabel1     =  [
#                 f180516
#                 f140616,f190816,
#                ] 


var     =  ['MCUP','CLD','QC']#,'RELH','WOBS']



cmf=(00.0,0.15,21,r'kg/m/s$^{2}$')
ccf=(0.0,32,21,'%')
crh=(0,100,21,'%')
cw =(-3,3,21,'cm/s')
cq =(0.0,0.1,21,'g/kg')

c1=[cmf,ccf,cq]

contour      =[
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
              ]

v1=[1,100,1]
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
co1         =  ['whbuyl','whbuyl','whbuyl']

color       =  [
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
               ]
s1=[False,False,False,False]
#s1=[True,True,True,True,]

show       =  [ s1,s1,s1,s1,s1,s1, s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
               ]


                #barra,x,y,lfc..
a0          =  (False,True,False,True ,0.35,0.00)
ab          =  (True ,True,False,True ,0.35,1.28)
abz         =  (True ,True ,True,True ,0.35,1.34)
az          =  (False,True ,True,True ,0.35,0.06)

a1          =  [a0,a0,a0,a0] 
a2          =  [az,az,az,az] 
a3          =  [ab,ab,ab,ab] 
axis_on     =  [
                a2,a1,a3,
                a2,a1,a3,
                a2,a3,
               ]




#two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)

two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)




