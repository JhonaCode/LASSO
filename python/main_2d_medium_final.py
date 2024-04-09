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
#f20180710,###'g)10-07-2018'
#f20180911,###'i)01-09-2018'
#f20190612,###'m)12-06-2019'

exp          =  [
                 f250616,  ###'a)25-06-2016'
                 f180816,  ###'b)18-08-2016'
                 f20180514,###'c)14-05-2018'
                 f20180618,###'d)18-06-2018'
                 f20180619,###'e)19-06-2018'
                 f20180705,###'f)05-07-2018'
                 f20180709,###'g)09-07-2018
                 f20180712,###'h)12-07-2018'
                 f20180914,###'i)14-09-2018'
                 f20181002,###'j)02-10-2018'
                 f20190517,###'k)17-05-2019'
                 f20190617,###'l)17-06-2019'
                 f20190626,###'m)26-06-2019'
                 f20190707,###'n)07-07-2019'
                 f20190714,###'o)14-07-2019'
                 f20190805,###'p)05-08-2019'
                 f20190901,###'q)01-09-2019'
                ]              

explabel1     = [
                    ['a)25-06-2016','a)25-06-2016',], ###)01)25-06-2016'
                    ['b)18-08-2016','b)18-08-2016',], ###)02)18-08-2016'
                    ['c)14-05-2018','c)14-05-2018',], ###)03)14-05-2018
                    ['d)18-06-2018','d)18-06-2018',], ###)04)18-06-2018'
                    ['e)19-06-2018','e)19-06-2018',], ###)05)19-06-2018'
                    ['f)05-07-2018','f)05-07-2018',], ###)06)07-07-2019'
                    ['g)09-07-2018','g)09-07-2018',], ###)07)05-07-2018'
                    ['h)12-07-2018','h)12-07-2018',], ###)08)10-07-2018'
                    ['i)14-09-2018','i)14-09-2018',], ###)09)12-07-2018'
                    ['j)02-10-2018','j)02-10-2018',], ###)10)01-09-2018'
                    ['k)17-05-2019','k)17-05-2019',], ###)11)01-09-2019'
                    ['l)17-06-2019','l)17-06-2019',], ###)12)14-09-2018'
                    ['m)26-06-2019','m)26-06-2019',], ###)13)02-10-2018'
                    ['n)07-07-2019','n)07-07-2019',], ###)14)17-05-2019'
                    ['o)14-07-2019','o)14-07-2019',], ###)15)12-06-2019'
                    ['p)05-08-2019','p)05-08-2019',], ###)16)14-07-2019'
                    ['q)01-09-2019','q)01-09-2019',], ###)17)05-08-2019'
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




