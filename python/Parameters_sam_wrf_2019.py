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


name        	= 'f20190404'
#note       	=  WRF 20190404
file_f20190404	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190404_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 4, 4,9),(2019, 4, 4,19)] 
date_diurnal	= [(2019, 4, 4,9),(2019, 4, 4,19)] 
cal         	= ['days  since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190404 	= sam.ncload(name,date,file_f20190404,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190506'
#note       	=  WRF 20190506
file_f20190506	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190506_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 5, 6,9),(2019, 5, 6,19)] 
date_diurnal	= [(2019, 5, 6,9),(2019, 5, 6,19)] 
f20190506 	= sam.ncload(name,date,file_f20190506,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190512'
#note       	=  WRF 20190512
file_f20190512	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190512_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 5,12,9),(2019, 5,12,19)] 
date_diurnal	= [(2019, 5,12,9),(2019, 5,12,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190512 	= sam.ncload(name,date,file_f20190512,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190517'
#note       	=  WRF 20190517
file_f20190517	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190517_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 5,17,9),(2019, 5,17,19)] 
date_diurnal	= [(2019, 5,17,9),(2019, 5,17,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190517 	= sam.ncload(name,date,file_f20190517,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190607'
#note       	=  WRF 20190607
file_f20190607	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190607_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 6,7,9),(2019, 6, 7,19)] 
date_diurnal	= [(2019, 6,7,9),(2019, 6, 7,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190607 	= sam.ncload(name,date,file_f20190607,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190612'
#note       	=  WRF 20190612
file_f20190612	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190612_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 6,12,9),(2019, 6,12,19)] 
date_diurnal	= [(2019, 6,12,9),(2019, 6,12,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190612 	= sam.ncload(name,date,file_f20190612,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190617'
#note       	=  WRF 20190617
file_f20190617	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190617_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 6,17,9),(2019, 6,17,19)] 
date_diurnal	= [(2019, 6,17,9),(2019, 6,17,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190617 	= sam.ncload(name,date,file_f20190617,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190626'
#note       	=  WRF 20190626
file_f20190626	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190626_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 6,26,9),(2019, 6,26,19)] 
date_diurnal	= [(2019, 6,26,9),(2019, 6,26,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190626 	= sam.ncload(name,date,file_f20190626,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190701'
#note       	=  WRF 20190701
file_f20190701	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190701_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 7, 1,9),(2019, 7, 1,19)] 
date_diurnal	= [(2019, 7, 1,9),(2019, 7, 1,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190701 	= sam.ncload(name,date,file_f20190701,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190704'
#note       	=  WRF 20190704
file_f20190704	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190704_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 7, 4,9),(2019, 7, 4,19)] 
date_diurnal	= [(2019, 7, 4,9),(2019, 7, 4,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190704 	= sam.ncload(name,date,file_f20190704,cal,var1d,var2d,vars_diurnal,date_diurnal)



name        	= 'f20190709'
#note       	=  WRF 20190709
file_f20190709	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190709_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 7, 9,9),(2019, 7, 9,19)] 
date_diurnal	= [(2019, 7, 9,9),(2019, 7, 9,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190709 	= sam.ncload(name,date,file_f20190709,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190714'
#note       	=  WRF 20190714
file_f20190714	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190714_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 7,14,9),(2019, 7,14,19)] 
date_diurnal	= [(2019, 7,14,9),(2019, 7,14,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190714 	= sam.ncload(name,date,file_f20190714,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190804'
#note       	=  WRF 20190804
file_f20190804	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190804_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 8, 4,9),(2019, 8, 4,19)] 
date_diurnal	= [(2019, 8, 4,9),(2019, 8, 4,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190804 	= sam.ncload(name,date,file_f20190804,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190707'
#note       	=  WRF 20190707
file_f20190707	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190707_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 7, 7,9),(2019, 7, 7,19)] 
date_diurnal	= [(2019, 7, 7,9),(2019, 7, 7,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190707 	= sam.ncload(name,date,file_f20190707,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190805'
#note       	=  WRF 20190805
file_f20190805	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190805_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 8, 5,9),(2019, 8, 5,19)] 
date_diurnal	= [(2019, 8, 5,9),(2019, 8, 5,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190805 	= sam.ncload(name,date,file_f20190805,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190901'
#note       	=  WRF 20190901
file_f20190901	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190901_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 9, 1,9),(2019, 9, 1,19)] 
date_diurnal	= [(2019, 9, 1,9),(2019, 9, 1,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190901 	= sam.ncload(name,date,file_f20190901,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'f20190929'
#note       	=  WRF 20190929
file_f20190929	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_20190929_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2019, 9,29,9),(2019, 9,29,19)] 
date_diurnal	= [(2019, 9,29,9),(2019, 9,29,19)] 
cal         	= ['days   since 2018-12-31 00:00:00 +06:00:00','gregorian']
f20190929 	= sam.ncload(name,date,file_f20190929,cal,var1d,var2d,vars_diurnal,date_diurnal)
