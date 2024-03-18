#######################################################
#File to define the direction of the sam runs.
#######################################################


### My own files


##Adress of the computer
from     files_direction  import *


import   sam_python.var_files.var_to_load_sam as sam


#######################################################
#Files of SAM to load.
#######################################################


name        	= '20180514'
#note       	= WRF 20180514
file_20180514	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180514_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,5,14,9),(2018,5,14,19)] 
date_diurnal	= [(2018,5,14,9),(2018,5,14,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180514 	= sam.ncload(name,date,file_20180514,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180522'
#note       	= WRF 20180522
file_20180522	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180522_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,5,22,9),(2018,5,22,19)] 
date_diurnal	= [(2018,5,22,9),(2018,5,22,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180522 	= sam.ncload(name,date,file_20180522,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180523'
#note       	= WRF 20180523
file_20180523	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180523_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,5,23,9),(2018,5,23,19)] 
date_diurnal	= [(2018,5,23,9),(2018,5,23,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180523 	= sam.ncload(name,date,file_20180523,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180529'
#note       	= WRF 20180529
file_20180529	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180529_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,5,29,9),(2018,5,29,19)] 
date_diurnal	= [(2018,5,29,9),(2018,5,29,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180529 	= sam.ncload(name,date,file_20180529,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180530'
#note       	= WRF 20180530
file_20180530	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180530_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,5,30,9),(2018,5,30,19)] 
date_diurnal	= [(2018,5,30,9),(2018,5,30,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180530 	= sam.ncload(name,date,file_20180530,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180531'
#note       	= WRF 20180531
file_20180531	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180531_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,5,31,9),(2018,5,31,19)] 
date_diurnal	= [(2018,5,31,9),(2018,5,31,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180531 	= sam.ncload(name,date,file_20180531,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180606'
#note       	= WRF 20180606
file_20180606	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180606_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,6,6,9),(2018,6,6,19)] 
date_diurnal	= [(2018,6,6,9),(2018,6,6,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180606 	= sam.ncload(name,date,file_20180606,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180618'
#note       	= WRF 20180618
file_20180618	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180618_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,6,18,9),(2018,6,18,19)] 
date_diurnal	= [(2018,6,18,9),(2018,6,18,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180618 	= sam.ncload(name,date,file_20180618,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180619'
#note       	= WRF 20180619
file_20180619	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180619_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,6,19,9),(2018,6,19,19)] 
date_diurnal	= [(2018,6,19,9),(2018,6,19,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180619 	= sam.ncload(name,date,file_20180619,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180704'
#note       	= WRF 20180704
file_20180704	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180704_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,4,9),(2018,7,4,19)] 
date_diurnal	= [(2018,7,4,9),(2018,7,4,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180704 	= sam.ncload(name,date,file_20180704,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180705'
#note       	= WRF 20180705
file_20180705	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180705_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,5,9),(2018,7,5,19)] 
date_diurnal	= [(2018,7,5,9),(2018,7,5,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180705 	= sam.ncload(name,date,file_20180705,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180707'
#note       	= WRF 20180707
file_20180707	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180707_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,7,9),(2018,7,7,19)] 
date_diurnal	= [(2018,7,7,9),(2018,7,7,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180707 	= sam.ncload(name,date,file_20180707,cal,var1d,var2d,vars_diurnal,date_diurnal)



name        	= '20180709'
#note       	= WRF 20180709
file_20180709	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180709_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,9,9),(2018,7,9,19)] 
date_diurnal	= [(2018,7,9,9),(2018,7,9,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180709 	= sam.ncload(name,date,file_20180709,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180710'
#note       	= WRF 20180710
file_20180710	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180710_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,10,9),(2018,7,10,19)] 
date_diurnal	= [(2018,7,10,9),(2018,7,10,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180710 	= sam.ncload(name,date,file_20180710,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180711'
#note       	= WRF 20180711
file_20180711	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180711_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,11,9),(2018,7,11,19)] 
date_diurnal	= [(2018,7,11,9),(2018,7,11,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180711 	= sam.ncload(name,date,file_20180711,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180712'
#note       	=  WRF 20180712
file_f20180712	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180712_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,12,9),(2018,7,12,19)] 
date_diurnal	= [(2018,7,12,9),(2018,7,12,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180712 	= sam.ncload(name,date,file_f20180712,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180731'
#note       	=  WRF 20180731
file_f20180731	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180731_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,7,31,9),(2018,7,31,19)] 
date_diurnal	= [(2018,7,31,9),(2018,7,31,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180731 	= sam.ncload(name,date,file_f20180731,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180805'
#note       	=  WRF 20180805
file_f20180805	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180805_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,8,5,9),(2018,8,5,19)] 
date_diurnal	= [(2018,8,5,9),(2018,8,5,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180805 	= sam.ncload(name,date,file_f20180805,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180809'
#note       	=  WRF 20180809
file_f20180809	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180809_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,8,9,9),(2018,8,9,19)] 
date_diurnal	= [(2018,8,9,9),(2018,8,9,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180809 	= sam.ncload(name,date,file_f20180809,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180811'
#note       	=  WRF 20180811
file_f20180811	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180811_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,8,11,9),(2018,8,11,19)] 
date_diurnal	= [(2018,8,11,9),(2018,8,11,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180811 	= sam.ncload(name,date,file_f20180811,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= '20180901'
#note       	=  WRF 20180901
file_f20180901	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180901_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,1,9),(2018,9,1,19)] 
date_diurnal	= [(2018,9,1,9),(2018,9,1,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180901 	= sam.ncload(name,date,file_f20180901,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20180902'
#note       	=  WRF 20180902
file_f20180902	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180902_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,2,9),(2018,9,2,19)] 
date_diurnal	= [(2018,9,2,9),(2018,9,2,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180902 	= sam.ncload(name,date,file_f20180902,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20180909'
#note       	=  WRF 20180909
file_f20180909	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180909_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,9,9),(2018,9,9,19)] 
date_diurnal	= [(2018,9,9,9),(2018,9,9,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180909 	= sam.ncload(name,date,file_f20180909,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20180911'
#note       	=  WRF 20180911
file_f20180911	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180911_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,11,9),(2018,9,11,19)] 
date_diurnal	= [(2018,9,11,9),(2018,9,11,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180911 	= sam.ncload(name,date,file_f20180911,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20180914'
#note       	=  WRF 20180914
file_f20180914	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180914_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,14,9),(2018,9,14,19)] 
date_diurnal	= [(2018,9,14,9),(2018,9,14,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180914 	= sam.ncload(name,date,file_f20180914,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20180916'
#note       	=  WRF 20180916
file_f20180916	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180916_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,16,9),(2018,9,16,19)] 
date_diurnal	= [(2018,9,16,9),(2018,9,16,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180916 	= sam.ncload(name,date,file_f20180916,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20180917'
#note       	=  WRF 20180917
file_f20180917	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180917_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,17,9),(2018,9,17,19)] 
date_diurnal	= [(2018,9,17,9),(2018,9,17,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180917 	= sam.ncload(name,date,file_f20180917,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20180918'
#note       	=  WRF 20180918
file_f20180918	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20180918_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,9,18,9),(2018,9,18,19)] 
date_diurnal	= [(2018,9,18,9),(2018,9,18,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20180918 	= sam.ncload(name,date,file_f20180918,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20181001'
#note       	=  WRF 20181001
file_f20181001	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20181001_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,10,1,9),(2018,10,1,19)] 
date_diurnal	= [(2018,10,1,9),(2018,10,1,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20181001 	= sam.ncload(name,date,file_f20181001,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20181002'
#note       	=  WRF 20181002
file_f20181002	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20181002_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2018,10,2,9),(2018,10,2,19)] 
date_diurnal	= [(2018,10,2,9),(2018,10,2,19)] 
cal         	= ['days   since 2017-12-31 00:00:00 +06:00:00','gregorian']
f20181002 	= sam.ncload(name,date,file_f20181002,cal,var1d,var2d,vars_diurnal,date_diurnal)
