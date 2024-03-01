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

from    Parameters_sam import *

import  matplotlib.pyplot as plt

#Defined the name of the experiments defined in Parameters files 
#separate with colon

#exp1=small
#exp2=medium
###case=' Medium-Small'
#case=' Médio-Pequeno'

exp1=medium
exp2=large
#case=' Large-Medium'
case=' Grande-Médio'



#exp1=small
#exp2=large
##case=' Large-Small'
#case=' Grande-Pequeno'


#separate with coma
#exp_label   = [
#                  r'a) $\mathrm{\theta_v}$'+case,r'a) RH'+case, r'a) W'+case,
#                  r'b) $\mathrm{\theta_v}$'+case,r'b) RH'+case, r'b) W'+case,
#                  r'c) $\mathrm{\theta_v}$'+case,r'c) RH'+case, r'c) W'+case,
#                  r'a) $\mathrm{\theta_v}$'+case,r'b) RH'+case, r'c) W'+case,
#                  r'a) $\mathrm{\theta_v}$'+case,r'b) RH'+case, r'c) W'+case,
#]

#exp_label   =  [
#                #r'a) $\mathrm{\theta_{ls}}$'+case, r'a) q$\mathrm{_{ls}}$'+case,
#                #r'a) U'+case, r'a) V'+case,
#                #r'b) $\mathrm{\theta_{ls}}$'+case, r'b) q$\mathrm{_{ls}}$'+case,
#                #r'b) U'+case, r'b) V'+case,
#                #r'c) $\mathrm{\theta_{ls}}$'+case, r'c) q$\mathrm{_{ls}}$'+case,
#                #r'c) U'+case, r'c) V'+case,
#]

exp_label   =  [
                r'a) $\mathrm{\theta_v}$'+case,
                r'b) $\mathrm{\theta_{ls}}$'+case,
                r'c) RH'+case,
                r'd) q$\mathrm{_{ls}}$'+case,
                r'e) W'+case,
                r'f) U'+case,
                r'g) V'+case,
                ]

#var         =  ['TTEND','QTEND','UOBS','VOBS']
var     =  ['THETAV','TTEND','RELH','QTEND','WOBS','UOBS','VOBS']


#Keyword to save the fig, in special figures
keyf=['zoom','zoom','zoom','zoom','zoom','zoom','zoom','zoom','zoom']
#keyf=['pt','pt','pt','pt']


#var     =  ['THETAV','RELH','WOBS']


#c1=(-3.0   ,3.0  ,21,'[K]')
#c2=(-50    ,50    ,21,'[%]')
#c3=(-3.0   ,3.0   ,21,'[cms$^{-1}$]')

#c1=(-13.0   ,13.0  ,21,'[K]')
#c2=(-70    ,70    ,21,'[%]')
#c3=(-5.0   ,5.0   ,21,'[cms$^{-1}$]')

#contour      =[
#                c1,c2,c3
#              ]
#

#c1=(-15    ,15    ,21,'[Kday$^{-1}$]')
#c2=(-15    ,15    ,21,'[gkg$^{-1}$day$^{-1}$]')
#c3=(-10    ,10    ,21,'[ms$^{-1}$]')
#c4=(-10    ,10    ,21,'[ms$^{-1}$]')

#c1=(-10    ,10    ,21,'[Kday$^{-1}$]')
#c2=(-10    ,10    ,21,'[gkg$^{-1}$day$^{-1}$]')
#c3=(-5    ,5    ,21,'[ms$^{-1}$]')
#c4=(-5    ,5    ,21,'[ms$^{-1}$]')


c1=(-3     ,3     ,21,'[K]')
c2=(-10    ,10    ,21,'[Kday$^{-1}$]')
c3=(-50    ,50    ,21,'[%]')
c4=(-10    ,10    ,21,'[gkg$^{-1}$day$^{-1}$]')
c5=(-4    ,4    ,21,'[ms$^{-1}$]')
c6=(-4    ,4    ,21,'[ms$^{-1}$]')
c7=(-4    ,4    ,21,'[ms$^{-1}$]')



contour     =[
              c1,c2,c3,c4,
              c5,c6,c7
             ]


var_to      =  [
#                1,1,100,
                1,1,1,1,
                100,1,1,
               ]


alt         =  [
                [0,5.0], [0,5.0], [0,5.0], 
                [0,5.0], [0,5.0], [0,5.0], 
                [0,5.0], [0,5.0], [0,5.0], 
                ]

co1='RdBu_r'

color       =  [
                co1,co1,co1,co1,co1,
                co1,co1,co1,co1,co1,
               ]


####bar ,x,y axis, top_lfc_pbl,cm a mais do grafico
a1          =  (False,True ,True ,True,0.35,0.00)
a2          =  (False,True ,False,True,0.35,0.06)
a3          =  (True ,True ,False,True,0.35,1.34)
a4          =  (True ,True ,True ,True,0.35,1.40)
a5          =  (True ,True ,False,True,0.35,1.34)

axis_on     =  [a1,a1,a1,a1]
axis_on     =  [a2,a2,a2,a2]
axis_on     =  [a3,a3,a3,a3]
#axis_on     =  [a4,a5,a4,a4]
axis_on     =  [a4,a5,a5,a4,a5,a5,a4]


show       =  [
                 True,True,True,
                 True,True,True,
                 #False,False,False,False
              ]

days        = [
                [(2024,1,1,8),(2024,1,1,20)],
                [(2024,1,1,8),(2024,1,1,20)],
                [(2024,1,1,8),(2024,1,1,20)],
                [(2024,1,1,8),(2024,1,1,20)],
                [(2024,1,1,8),(2024,1,1,20)],
                [(2024,1,1,8),(2024,1,1,20)],
                [(2024,1,1,8),(2024,1,1,20)],
                [(2024,1,1,8),(2024,1,1,20)],
            ]


two.plot2d_im_diff(exp1,exp2,var,alt=alt,days=days,color=color,explabel1=exp_label,var_to=var_to,contour=contour,axis_on=axis_on,keyf=keyf,show=show)

