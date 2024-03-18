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
#note       	= Teste, primeiro lasso
file_large	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,6),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,6),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
large 	= sam.ncload(name,date,file_large,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'medium'
#note       	= Teste, primeiro lasso
file_medium	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,6),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,6),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
medium 	= sam.ncload(name,date,file_medium,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'small'
#note       	= Teste, primeiro lasso
file_small	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,6),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,6),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
small 	= sam.ncload(name,date,file_small,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'all1'
#note       	= all shca  lasso case, the later was wrong
file_all1	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_all1_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,6),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,6),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
all1 	= sam.ncload(name,date,file_all1,cal,var1d,var2d,vars_diurnal,date_diurnal)


######experiments


name        	= 'm_w_l'
#note       	= Medim with the w of the large
file_m_w_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_w_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_w_l 	= sam.ncload(name,date,file_m_w_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'm_q_l'
#note       	= Medim with the q, q init and q ls, of the large
file_m_q_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_q_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_q_l 	= sam.ncload(name,date,file_m_q_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'm_theta_l'
#note       	= Medim with the theta, theta init and theta ls, of the large
file_m_theta_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_theta_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_theta_l 	= sam.ncload(name,date,file_m_theta_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'm_u_l'
#note       	= Medim with the u, u init and u ls, of the large
file_m_u_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_u_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_u_l 	= sam.ncload(name,date,file_m_u_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'm_v_l'
#note       	= Medim with the v, v init and v ls, of the large
file_m_v_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_v_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_v_l 	= sam.ncload(name,date,file_m_v_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


#Smalll to medium 

name        	= 's_w_m'
#note       	= Small with the w, w init and w ls, of the large
file_s_w_m	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_w_medium_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
s_w_m 	= sam.ncload(name,date,file_s_w_m,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 's_q_m'
#note       	= Small with the q, q init and q ls, of the large
file_s_q_m	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_q_medium_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
s_q_m 	= sam.ncload(name,date,file_s_q_m,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 's_theta_m'
#note       	= Small with the theta, theta init and theta ls, of the large
file_s_theta_m	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_theta_medium_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
s_theta_m 	= sam.ncload(name,date,file_s_theta_m,cal,var1d,var2d,vars_diurnal,date_diurnal)



name        	= 'm_tin_l'
#note       	= Medium with the t init  of the large
file_m_tin_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_tinit_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_tin_l 	= sam.ncload(name,date,file_m_tin_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'm_qin_l'
#note       	= Medium with the q init  of the large
file_m_qin_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_qinit_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_qin_l 	= sam.ncload(name,date,file_m_qin_l,cal,var1d,var2d,vars_diurnal,date_diurnal)

################## 
################## Two VARIABLES
##################


name        	= 'm_tq_l'
#note       	= Medium with the t and q init and ls  of the large
file_m_tq_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_tq_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_tq_l 	= sam.ncload(name,date,file_m_tq_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'm_tqin_l'
#note       	= Medium with the t and q init  of the large
file_m_tqin_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_tqinit_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_tqin_l 	= sam.ncload(name,date,file_m_tqin_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 'm_tqls_l'
#note       	= Medium with the t and q large scale  of the large
file_m_tqls_l	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_medium_tqls_large_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,9),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,9),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
m_tqls_l 	= sam.ncload(name,date,file_m_tqls_l,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 's_qin_m'
#note       	= Small with the q init  of the medium
file_s_qin_m	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_qinit_medium_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,6),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,6),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
s_qin_m 	= sam.ncload(name,date,file_s_qin_m,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 's_wq_m'
#note       	= Small with the w and q ls and init of the medium
file_s_wq_m	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_wq_medium_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,6),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,6),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
s_wq_m 	= sam.ncload(name,date,file_s_wq_m,cal,var1d,var2d,vars_diurnal,date_diurnal)


name        	= 's_wqinit_m'
#note       	= Small with the w and q init of the medium
file_s_wqinit_m	= '/dados/bamc/jhonatan.aguirre/DATA/LASSO/SAM_OWN/OUT_STAT/LASSO_small_wqinit_medium_lsf_144x226_100_50m_0p5.nc'
var1d       	= ['MCUP','QC'] 
var2d       	= ['MCUP','QC'] 
vars_diurnal	= ['MCUP','QC']
date        	= [(2024,1,1,6),(2024,1,1,19)] 
date_diurnal	= [(2024,1,1,6),(2024,1,1,19)] 
cal         	= ['days   since 2023-12-31 00:00:00 +06:00:00','gregorian']
s_wqin_m 	= sam.ncload(name,date,file_s_wqinit_m,cal,var1d,var2d,vars_diurnal,date_diurnal)
