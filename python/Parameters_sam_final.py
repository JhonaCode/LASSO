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


name        	= 'large'
#note       	= Composto final  large_lsf_final
file_large	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_large_lsf_final_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days  since 2023-12-31 00:00:00 +06:00:00','gregorian']
large 	= sam.ncload(name,date,file_large,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'small'
#note       	= Composto final  small_lsf_final
file_small	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_lsf_final_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days  since 2023-12-31 00:00:00 +06:00:00','gregorian']
small 	= sam.ncload(name,date,file_small,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'medium'
#note       	= Composto final  medium_lsf_final
file_medium	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_lsf_final_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days  since 2023-12-31 00:00:00 +06:00:00','gregorian']
medium 	= sam.ncload(name,date,file_medium,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'todos'
#note       	= Composto final  medium_lsf_final
file_todos	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_todos_lsf_final_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days  since 2024-12-31 00:00:00 +06:00:00','gregorian']
todos 	= sam.ncload(name,date,file_todos,cal,var1d,var2d,vars_diurnal,date_diurnal)
