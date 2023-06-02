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

import  source.data_own          as down

import  source.two_dimensional   as cf 

from    files_direction import * 

from    Parameters import *

import  matplotlib.pyplot as plt

import tkinter

matplotlib.use('TkAgg')


#Defined the name of the experiments defined in Parameters files 
#separate with colon
exp         =   [ LASSO_teste4, ]

#figures name
explabel    =   ['LASSO_teste4',]

# label in the figures
explabel2   =   ['LASSO_teste4',]

# Data to plot 
exp_days    =   [ (2015,6,6,9,2015,6,6,20), ]

hours	  =   [ (8,20)]

alt	  =   [  4.5,]

color	  =   [ 'navy',
              ] 

cor1      =   [ 'navy', 
              ] 

cor2      =   [ 'red', 
              ] 


explabel2 =   [' CF ' ] 
####bar ,y axis, top_lfc_pbl,cm a mais do grafico
axis_on   =[(True,True,True,0.4,0.0)]
contour   =[(0.005,15,21)]
fn1       =   cf.plot2d_im_ctn(exp,exp_days,alt,explabel,explabel2,hours,contour,axis_on,show=False) 


explabel2 =   [' uMF '] 
contour=[(0.001,0.12,21)]
axis_on=[(True,True,True,0.4,0.0)]
fn2    =   cf.plot2d_im_mass_flux(exp,exp_days,alt,explabel,explabel2,hours,contour,axis_on,show=False) 



explabel2 =   ['W$\mathrm{_{ls}}$'] 
axis_on   =   [(True,True,True,0.4,0.0)]
contour   =   [   
                (-2.80,1.5,21),
              ]

fn3       =   cf.plot2d_im_wobs(exp,exp_days,alt,explabel,explabel2,hours,contour,axis_on,show=False) 
contour   =   [   
                (10.0,100,21),
              ]
explabel2 =   [' RH' ] 
axis_on   =   [(True,True,True,0.4,0.0)]
fn4       =   cf.plot2d_im_relh(exp,exp_days,alt,explabel,explabel2,hours,contour,axis_on,show=False) 


explabel2 =   [' CLW '] 
contour   =   [(0.0005,0.03,21)]
axis_on   =   [(True,True,True,0.4,0.0)]
fn5       =   cf.plot2d_im_ql(exp,exp_days,alt,explabel,explabel2,hours,contour,axis_on,show=False) 


explabel2 =   [' Wc'] 
axis_on   =   [(True,True,True,0.4,0.0)]
contour   =   [(0.01,2.0,21)]
fn6       =   cf.plot2d_im_wsup(exp,exp_days,alt,explabel,explabel2,hours,contour,axis_on,show=False) 

explabel2 =   ['Wd'] 
axis_on   =   [(True,True,True,0.4,0.0)]
contour   =   [(-2,-0.01,21)]
fn7       =   cf.plot2d_im_wsup_down(exp,exp_days,alt,explabel,explabel2,hours,contour,axis_on,show=False) 

plt.show()




