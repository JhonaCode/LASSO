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

"""
exp          =  [
                    f270615  ,###a)27-06-2016
                    f290815  ,###b)29-08-2015
                    f180516  ,###c)18-05-2016
                    f20180606,###d)06-06-2018
                    f20180731,###e)31-07-2018
                    f20180901,###f)01-09-2018
                    f20180917,###g)17-09-2018
                    f20190704,###h)04-07-2019
                    f20190709,###i)09-07-2019
                    #nuvem isolada
                    f20180805,###f)05-08-2018
                    f20190512,###i)12-05-2019
                ] 

explabel1     = [
                 ['a)27-06-2015' ,'a)27-06-2015','a)27-06-2015'],
                 ['b)29-08-2015' ,'b)29-08-2015','b)29-08-2015'],
                 ['c)18-05-2016' ,'c)18-05-2016','c)18-05-2016'],
                 ['d)06-06-2018' ,'d)06-06-2018','d)06-06-2018'],
                 ['e)31-07-2018' ,'e)31-07-2018','e)31-07-2018'],
                 ['f)01-09-2018' ,'f)01-09-2018','f)01-09-2018'],
                 ['g)17-09-2018' ,'g)17-09-2018','g)17-09-2018'],
                 ['h)04-07-2019' ,'h)04-07-2019','h)04-07-2019'],
                 ['i)09-07-2019' ,'i)09-07-2019','i)09-07-2019'],
                 ###
                 ['j)05-08-2018' ,'j)05-08-2018','j)05-08-2018'],
                 ['k)12-05-2019' ,'k)12-05-2019','k)12-05-2019'], 
                ]

"""
exp          =  [
                    f060615, ###'a)06-06-2015'
                    f20180522,###b)22-05-2018
                    f20180707,###c)07-07-2018
                    f20180911,###d)11-09-2018
                    f20180916,###e)16-09-2018
                    f20181001,###f)01-10-2018
                    f20190404,###g)04-04-2019
                    f20190607,###h)07-06-2019
                    f20190612,###i)12-06-2019
                    f20190701,###j)01-07-2019
                ]                  

explabel1     = [
                 ['a)06-06-2015','a)06-06-2015','a)06-06-2015'],
                 ['b)22-05-2018','b)22-05-2018','b)22-05-2018'],
                 ['c)07-07-2018','c)07-07-2018','c)07-07-2018'],
                 ['d)11-09-2018','d)11-09-2018','d)11-09-2018'],
                 ['e)16-09-2018','e)16-09-2018','e)16-09-2018'],
                 ['f)01-10-2018','f)01-10-2018','f)01-10-2018'],
                 ['g)04-04-2019','g)04-04-2019','g)04-04-2019'],
                 ['h)07-06-2019','h)07-06-2019','h)07-06-2019'],
                 ['i)12-06-2019','i)12-06-2019','i)12-06-2019'],
                 ['j)01-07-2019','j)01-07-2019','j)01-07-2019'], 
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




