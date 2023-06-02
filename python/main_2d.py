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

import  sam_python.data_own          as down

import  sam_python.two_dimensional   as cf

from    files_direction import *

from    Parameters_dict import *

import  matplotlib.pyplot as plt

#Defined the name of the experiments defined in Parameters files 
#separate with colon

exp          =  [f060615] 

contour      =[
                (00.0,0.1,21),(0.0,15,21),(20,90,21),(-2,2,21)
              ]


var_to      =  [
                    1, 100, 1,100,  
               ]

#figures name
exp_label   =  [ 
                 'uMF', 'CF'  , 'RH','Wobs'
               ]

#l1           =  ( 0.00,4.0,'lower right',True,True)
#lrh          =  ( 70.0,4.0,'lower right',True,True)

#leg_loc      =  [ 
#                l1,l1,l1,
#                l1,l1,lrh,
#                l1,l1,l1,
#                ]

alt         =  [
                5.0, 5.0, 5.0, 
                5.0, 5.0, 5.0, 
                5.0, 5.0, 5.0, 
               ]

color       =  [
                'RdBu_r','RdBu_r','RdBu_r','RdBu_r'
               ]

show       =  [
                True,True,True,
                True,True,True,
                True,True,True,
               ]

#Minimum calll
#fig,ax      =   dc.diurnal_hours_dict(ex,name,var,ex_date)
#complete call

for ex in exp:

    #cf.plot2d_contour(ex,contour,axis_on,show)
    cf.plot2d_contour(ex,var_to=var_to,contour=contour,color=color, alt=alt,show=show)
