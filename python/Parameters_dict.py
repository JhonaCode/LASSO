########################################################
#File to define the direction of the SAM runs.
########################################################

### My own files

##Adress of the computer
from     files_direction  import *

import   sam_python.var_files.var_to_load_sam_lasso  as var_l

########################################################
#Files of SAM to load.
########################################################

#var        = [ 
#               'MCUP'  , 'CLD' , 'TKE' , 
#               'TVFLUX', 'WOBS', 'RELH',  
#               'QC'    , 'Q1C' , 'Q2',  
#             ]
#var        = [ 
#              'MCUP','CLD','RELH','WOBS' 
#             ]
#

var1d       = ['MCUP','QC']
var2d       = ['MCUP','QC']
vars_diurnal= ['MCUP','QC']


name       = 'lasso_060615'
date       = [(2015,6,6,7),(2015,6,6,20)]
date_diurnal=[(2015,6,6,9),(2015,6,6,19)]
calendar   = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
file1      = '%s/DADOS/raw_model/sgp20150606_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
f060615    =  var_l.ncload(name,file1,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)


name        = 'lasso_090615'
file1       = '%s/DADOS/raw_model/sgp20150606_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
file2       =   '%s/DADOS/raw_model/sgp20150609_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,6,9,7),(2015,6,9,20)]
date_diurnal= [(2015,6,9,7),(2015,6,9,19)]
f090615     = var_l.ncload(name,file2,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_270615'
file3       = '%s/DADOS/raw_model/sgp20150627_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,6,27,7),(2015,6,27,20)]
date_diurnal= [(2015,6,27,9),(2015,6,27,19)]
f270615     = var_l.ncload(name,file3,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_010815'
file4       =   '%s/DADOS/raw_model/sgp20150801_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,8,1,7),(2015,8,1,20)]
date_diurnal= [(2015,8,1,9),(2015,8,1,19)]
f010815     = var_l.ncload(name,file4,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_290815'
file5       =   '%s/DADOS/raw_model/sgp20150829_rerun2020.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,8,29,7),(2015,8,29,20)]
date_diurnal= [(2015,8,29,9),(2015,8,29,19)]
f290815     = var_l.ncload(name,file5,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_180516'
file6       =   '%s/DADOS/raw_model/sgp20160518_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,5,18,7),(2016,5,18,20)]
date_diurnal= [(2016,5,18,9),(2016,5,18,19)]
f180516     = var_l.ncload(name,file6,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_300516'
file7       =   '%s/DADOS/raw_model/sgp20160530_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,5,30,7),(2016,5,30,20)]
date_diurnal= [(2016,5,30,9),(2016,5,30,19)]
f300516     = var_l.ncload(name,file7,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_140616'
file8       =   '%s/DADOS/raw_model/sgp20160614_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,6,14,7),(2016,6,14,20)]
date_diurnal= [(2016,6,14,9),(2016,6,14,19)]
f140616     = var_l.ncload(name,file8,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_250616'
file9       =   '%s/DADOS/raw_model/sgp20160625_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,6,25,7),(2016,6,25,20)]
date_diurnal= [(2016,6,25,9),(2016,6,25,19)]
f250616     = var_l.ncload(name,file9,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_160716'
file10      =   '%s/DADOS/raw_model/sgp20160716_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,7,16,7),(2016,7,16,20)]
date_diurnal= [(2016,7,16,9),(2016,7,16,19)]
f160716     = var_l.ncload(name,file10,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_190716'
file11      =   '%s/DADOS/raw_model/sgp20160719_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,7,19,7),(2016,7,19,20)]
date_diurnal= [(2016,7,19,9),(2016,7,19,19)]
f190716     = var_l.ncload(name,file11,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_200716'
file12      =   '%s/DADOS/raw_model/sgp20160720_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,7,20,7),(2016,7,20,20)]
date_diurnal= [(2016,7,20,9),(2016,7,20,19)]
f200716     = var_l.ncload(name,file12,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_190816'
file13      =   '%s/DADOS/raw_model/sgp20160819_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,8,19,7),(2016,8,19,20)]
date_diurnal= [(2016,8,19,9),(2016,8,19,19)]
f190816     = var_l.ncload(name,file13,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_300816'
file14      =   '%s/DADOS/raw_model/sgp20160830_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,8,30,7),(2016,8,30,20)]
date_diurnal= [(2016,8,30,9),(2016,8,30,19)]
f300816 = var_l.ncload(name,file14,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

