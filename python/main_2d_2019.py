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

from    Parameters_sam_wrf_2019 import *

import  matplotlib.pyplot as plt


# to work without display
plt.switch_backend('agg')


####246172

#Defined the name of the experiments defined in Parameters files 
#separate with colon

exp          =  [
                f20190404,###a)04-04-2019'
                f20190506,###b)06-05-2019'
                f20190512,###c)12-05-2019'
                f20190517,###d)17-05-2019'
                f20190607,###f)07-06-2019'
                f20190612,###g)12-06-2019'
                f20190617,###h)17-06-2019'
                f20190626,###i)26-06-2019'
                f20190701,###j)01-07-2019'
                f20190704,###k)04-07-2019'
                f20190707,###l)07-07-2019'
                f20190709,###m)09-07-2019'
                f20190714,###n)14-07-2019'
                f20190804,###o)04-08-2019'
                f20190805,###p)05-08-2019'
                f20190901,###r)01-09-2019'
                f20190929, ###s)29-09-2019'
                ]         


explabel1     = [
                 ['a)04-04-2019','a)04-04-2019','a)04-04-2019',],
                 ['b)06-05-2019','b)06-05-2019','b)06-05-2019',],
                 ['c)12-05-2019','c)12-05-2019','c)12-05-2019',],

                 ['d)17-05-2019','d)17-05-2019','d)17-05-2019',],
                 ['f)07-06-2019','f)07-06-2019','f)07-06-2019',],
                 ['g)12-06-2019','g)12-06-2019','g)12-06-2019',],

                 ['h)17-06-2019','h)17-06-2019','h)17-06-2019',],
                 ['i)26-06-2019','i)26-06-2019','i)26-06-2019',],
                 ['j)01-07-2019','j)01-07-2019','j)01-07-2019',],

                 ['k)04-07-2019','k)04-07-2019','k)04-07-2019',],
                 ['l)07-07-2019','l)07-07-2019','l)07-07-2019',],
                 ['m)09-07-2019','m)09-07-2019','m)09-07-2019',],

                 ['n)14-07-2019','n)14-07-2019','n)14-07-2019',],
                 ['o)04-08-2019','o)04-08-2019','o)04-08-2019',],
                 ['p)05-08-2019','p)05-08-2019','p)05-08-2019',],

                 ['r)01-09-2019','r)01-09-2019','r)01-09-2019',],
                 ['s)29-09-2019','s)29-09-2019','s)29-09-2019',],
                ] 



#var     =  ['MCUP','CLD','QC']#,'RELH','WOBS']
#var     =  ['CLD','MCUP','RELH']#,'WOBS']
var     =  ['MCUP']



cmf=(00.0,0.15,21,r'kg/m/s$^{2}$')
ccf=(0.0,32,21,'%')
crh=(0,100,21,'%')
cw =(-3,3,21,'cm/s')
cq =(0.0,0.1,21,'g/kg')

c1=[cmf,ccf,cq]
#c1=[ccf,cmf,cq,crh]

contour      =[
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
               ]


a0=(0,5.0)
a1=[a0,a0,a0,a0]
alt         =  [
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
               ]
s1=[False,False,False,False]
#s1=[True,True,True,True,]

show       =  [ s1,s1,s1,s1,s1,s1, s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
                s1,s1,s1,s1,s1,s1, 
               ]


                #barra,x,y,lfc..
a0          =  (False,True,False,True ,0.35,0.00)
ab          =  (True ,True,False,True ,0.35,1.28)
abz         =  (True ,True ,True,True ,0.35,1.34)
az          =  (False,True ,True,True ,0.35,0.06)

#a01         =  (False,True,True ,False ,0.35,0.06)
#a02         =  (False,True,False,False ,0.35,0.00)
#a03         =  (True ,True,False,False ,0.35,1.34)

a01         =  (False,True,True ,True ,0.35,0.06)
a02         =  (False,True,False,True ,0.35,0.00)
a03         =  (True ,True,False,True ,0.35,1.34)

a1          =  [a01,az,az,a0] 
a2          =  [a02,a0,a0,a0] 
a3          =  [a03,ab,ab,a0] 

axis_on     =  [
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

two.plot2d_contour(exp,var=var,contour=contour,explabel1=explabel1,alt=alt,color=color,var_to=var_to,axis_on=axis_on,show=show)




