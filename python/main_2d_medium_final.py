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

#3  06-06-2015  
#14 25-06-2016 
#15 18-08-2016 

exp          =  [
                 f20180911,###'a)01-09-2018'
                 f20190612,###'b)12-06-2019'
                 f060615,  ###'c)06-06-2015'
                 f20190517,###'d)17-05-2019'
                 f20180619,###'e)19-06-2018'
                 f20190805,###'f)05-08-2019'
                 f20180914,###'g)14-09-2018'
                 f20190901,###'h)01-09-2019'
                 f20181002,###'i)02-10-2018'
                 f20180712,###'j)12-07-2018'
                 f20190707,###'k)07-07-2019'
                 f20190714,###'l)14-07-2019'
                 f20180710,###'m)10-07-2018'
                 f250616,  ###'n)25-06-2016'
                 f180816,  ###'o)18-08-2016'
                 f20180618,###'p)18-06-2018'
                 f20180705,###'q)05-07-2018'
                ] 

explabel1     = [
                    ['a)11-09-2018','a)11-09-2018',],
                    ['b)12-06-2019','b)12-06-2019',],
                    ['c)06-06-2015','c)06-06-2015',],
                    ['d)17-05-2019','d)17-05-2019',],
                    ['e)19-06-2018','e)19-06-2018',],
                    ['f)05-08-2019','f)05-08-2019',],
                    ['g)14-09-2018','g)14-09-2018',],
                    ['h)01-09-2019','h)01-09-2019',],
                    ['i)02-10-2018','i)02-10-2018',],
                    ['j)12-07-2018','j)12-07-2018',],
                    ['k)07-07-2019','k)07-07-2019',],
                    ['l)14-07-2019','l)14-07-2019',],
                    ['m)10-07-2018','m)10-07-2018',],
                    ['n)25-06-2016','n)25-06-2016',],
                    ['o)18-08-2016','o)18-08-2016',],
                    ['p)18-06-2018','p)18-06-2018',],
                    ['q)05-07-2018','q)05-07-2018',],
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




