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


exp          =  [
                 f060615,f090615,
                 f270615,f010815,
                 f290815,f180516,
                 f300516,f100616,
                 f110616,f140616,
                 f190616,f250616,
                 f160716,f190716,
                 f200716,f180816,
                 f190816,f300816
                ] 

explabel1     = [
                 ['1)  06-06-2015','1)  06-06-2015'],['2) 09-06-2015','2) 09-06-2015'],
                 ['3)  27-06-2015','3)  27-06-2015'],['4) 01-08-2015','4) 01-08-2015'],
                 ['5)  29-08-2015','5)  29-08-2015'],['6) 18-05-2016','6) 18-05-2016'],
                 ['7)  30-05-2016','7)  30-05-2016'],['8) 10-06-2016','8) 10-06-2016'],
                 ['9)  11-06-2016','9)  11-06-2016'],['10)14-06-2016','10)14-06-2016'],
                 ['11) 19-06-2016','11) 19-06-2016'],['12)25-06-2016','12)25-06-2016'],
                 ['13) 16-07-2016','13) 16-07-2016'],['14)19-07-2016','14)19-07-2016'],
                 ['15) 20-07-2016','15) 20-07-2016'],['16)18-08-2016','16)18-08-2016'],
                 ['17) 19-08-2016','17) 19-08-2016'],['18)30-08-2016','18)30-08-2016']
                ] 


##Normal
#exp          =  [
#
#                 f060615,f270615,f290815,
#                 f250616,
#                 f180816,
#                 f300816,
#                ] 
#explabel1     = [
#                 ['a)06-06-2015','a)06-06-2015','a)06-06-2015'],['b)27-06-2015','b)27-06-2015','b)27-06-2015'],
#                 ['c)29-08-2015','c)29-08-2015','c)29-08-2015'], #['d)300516'],
#                 ['d)25-06-2016','d)25-06-2016','d)25-06-2016'], ['e)18-08-2016','e)18-08-2016','e)18-08-2016'],
#                 ['f)30-08-2016','f)30-08-2016','f)30-08-2016'],
#                ] 
#
#no shca
#exp          =  [
#                 f180516
#                 f140616,f190816,
#                ] 
#explabel1     =  [
#                 f180516
#                 f140616,f190816,
#                ] 


#var     =  ['CLD']
var     =  ['CLD']
#var     =  ['QVOBS']#,'RELH','WOBS','CLD']

#print(f060615.z[0:80])
#exit()


cmf=(00.0,0.15,21,r'kg/m/s$^{2}$')
ccf=(0.0,50,21,'%')
crh=(0,100,21,'%')
cw =(-3,3,21,'cm/s')
#cq =(0,16,21,'g/kg')
cq =(0.0,0.1,21,'g/kg')


#c1=[cmf,ccf,cq]
c1=[ccf,cmf]
#c1=[cq,crh,cw,ccf]

contour      =[
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
                c1,c1,c1,c1,c1,
              ]

#v1=[1,1,100,100]
#v1=[1,100,1]
v1=[100,1]
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
co1         =  ['whbuyl','whbuyl','whbuyl','RdBu_r']

color       =  [
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,co1,
               ]
#s1=[True,False,False,False]
#s1=[True,True,True,True,]
s1=[False,False,True,True,]
show       =  [ s1,s1,s1,s1,s1,s1, s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
               ]


                #barra,x,y,lfc..
a0          =  (False,True,False,False,0.35,0.00)
ab          =  (True ,True,False,False,0.35,1.28)
abz         =  (True ,True ,True,False,0.35,1.34)
az          =  (False,True ,True,False,0.35,0.06)

a1          =  [a0,a0,a0,a0] 
a2          =  [az,az,az,az] 
a3          =  [ab,ab,ab,ab] 
a4          =  [abz,abz,abz,abz] 
axis_on     =  [
                a2,a1,a3,
                a2,a1,a3,
                a2,a1,a3,
                a2,a1,a3,
                a2,a1,a3,
                a2,a1,a3,
                a2,a1,a3,
               ]


two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)
#two.plot2d_contour(exp,var=var,contour=contour,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)




