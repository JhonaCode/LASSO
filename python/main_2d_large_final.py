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
from    Parameters_sam_wrf import *
from    Parameters_sam_wrf_2019 import *

import  matplotlib.pyplot as plt


# to work without display
plt.switch_backend('agg')

label=['_final']

exp          =  [
                 f090615,   ###)1
                 f010815,   ###)2
                 f100616,   ###)3
                 f190616,   ###)4
                 f160716,   ###)5
                 f200716,   ###)6
                 f300816,   ###)7
                 f20180523, ###)8
                 f20180710, ###)9
                 f20180711, ###)10
                 f20180811, ###)11
                 f20190804, ###)12
                ] 

explabel1     = [
                 ['a)09-06-2015','a)09-06-2015'],
                 ['b)01-08-2015','b)01-08-2015'],
                 ['c)10-06-2016','c)10-06-2016'],
                 ['d)19-06-2016','d)19-06-2016'],
                 ['e)16-07-2016','e)16-07-2016'],
                 ['f)20-07-2016','f)20-07-2016'],
                 ['g)30-08-2016','g)30-08-2016'],
                 ['h)23-05-2018','h)23-05-2018'],
                 ['i)10-07-2018','i)10-07-2018'],
                 ['j)11-07-2018','j)11-07-2018'],
                 ['k)11-08-2018','k)11-08-2018'],
                 ['l)04-08-2019','l)04-08-2019'],
                 ]


var     =  ['MCUP','CLD']#,'RELH','WOBS']
#var     =  ['CLD','MCUP']#,'RELH']#,'WOBS']



cmf=(00.0,0.15,21,r'kg/m/s$^{2}$')
ccf=(0.0,32,21,'%')
crh=(0,100,21,'%')
cw =(-3,3,21,'cm/s')
cq =(0.0,0.1,21,'g/kg')

c1=[cmf,ccf]#,cq,crh]
#c1=[ccf,cmf,cq,crh]

contour      =[
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
              ]

v1=[1,100,1]
#v1=[100,1,100]
var_to      =  [
                v1,v1,v1,v1,v1,
                v1,v1,v1,v1,v1,
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
                co1,co1,co1,co1,co1,co1,
               ]
s1=[False,False,False,False]
#s1=[True,True,True,True,]

show       =  [ s1,s1,s1,s1,s1,s1,
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
               ]


                #barra,x,y,lfc..
a01         =  (False,True,True ,True  ,0.35,0.06)
a02         =  (False,True,False,True  ,0.35,0.00)
a03         =  (True ,True,False,True  ,0.35,1.28)

a1          =  [a01,a01,a01] 
a2          =  [a02,a02,a02] 
a3          =  [a03,a03,a03] 


axis_on     =  [
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
                a1,a2,a3,
               ]


#a1          =  [a01,a01,a0,a0] 
#a2          =  [a02,a01,a0,a0] 
#a3          =  [a03,a01,a0,a0] 
#a2          =  [az,az,az,az] 
#a3          =  [ab,ab,ab,ab] 
#a3          =  [a01,ab,ab,ab] 

#axis_on     =  [
#                a2,a1,a3,
#                a2,a1,a3,
#                a2,a1,a3,
#                a2,a1,a3,
#                a2,a1,a3,
#                a2,a1,a3,
#                a2,a1,a3,
#               ]
#



#two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)

two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show,label=label)




