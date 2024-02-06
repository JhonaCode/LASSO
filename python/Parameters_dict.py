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


######################2015 
name       = 'lasso_060615'
date       = [(2015,6,6,7),(2015,6,6,20)]
date_diurnal=[(2015,6,6,9),(2015,6,6,19)]
calendar   = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
file1      = '%s/lasso_sam_20150606/raw_model/sgp20150606_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
f060615    =  var_l.ncload(name,file1,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)


name        = 'lasso_090615'
file2       = '%s/lasso_sam_20150609/raw_model/sgp20150609_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,6,9,7),(2015,6,9,20)]
date_diurnal= [(2015,6,9,7),(2015,6,9,19)]
f090615     = var_l.ncload(name,file2,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_270615'
file3       = '%s/lasso_sam_20150627/raw_model/sgp20150627_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,6,27,7),(2015,6,27,20)]
date_diurnal= [(2015,6,27,9),(2015,6,27,19)]
f270615     = var_l.ncload(name,file3,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_010815'
file4       =   '%s/lasso_sam_20150801/raw_model/sgp20150801_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,8,1,7),(2015,8,1,20)]
date_diurnal= [(2015,8,1,9),(2015,8,1,19)]
f010815     = var_l.ncload(name,file4,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_290815'
file5       =   '%s/lasso_sam_20150829/raw_model/sgp20150829_rerun2020.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2015,8,29,7),(2015,8,29,20)]
date_diurnal= [(2015,8,29,9),(2015,8,29,19)]
f290815     = var_l.ncload(name,file5,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

#########2016

name        = 'lasso_180516'
file6       =   '%s/lasso_sam_20160518/raw_model/sgp20160518_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,5,18,7),(2016,5,18,20)]
date_diurnal= [(2016,5,18,9),(2016,5,18,19)]
f180516     = var_l.ncload(name,file6,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_300516'
file7       =   '%s/lasso_sam_20160530/raw_model/sgp20160530_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,5,30,7),(2016,5,30,20)]
date_diurnal= [(2016,5,30,9),(2016,5,30,19)]
f300516     = var_l.ncload(name,file7,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_100616'
file8       =   '%s/lasso_sam_20160610/raw_model/sgp20160610_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,6,10,7),(2016,6,10,20)]
date_diurnal= [(2016,6,10,9),(2016,6,10,19)]
f100616     = var_l.ncload(name,file8,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_110616'
file9       =   '%s/lasso_sam_20160611/raw_model/sgp20160611_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,6,11,7),(2016,6,11,20)]
date_diurnal= [(2016,6,11,9),(2016,6,11,19)]
f110616     = var_l.ncload(name,file9,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_140616'
file10      = '%s/lasso_sam_20160614/raw_model/sgp20160614_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,6,14,7),(2016,6,14,20)]
date_diurnal= [(2016,6,14,9),(2016,6,14,19)]
f140616     = var_l.ncload(name,file10,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_190616'
file11       =   '%s/lasso_sam_20160619/raw_model/sgp20160619_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,6,19,7),(2016,6,19,20)]
date_diurnal= [(2016,6,19,9),(2016,6,19,19)]
f190616     = var_l.ncload(name,file11,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)


name        = 'lasso_250616'
file12       =   '%s/lasso_sam_20160625/raw_model/sgp20160625_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,6,25,7),(2016,6,25,20)]
date_diurnal= [(2016,6,25,9),(2016,6,25,19)]
f250616     = var_l.ncload(name,file12,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)


name        = 'lasso_160716'
file13      =   '%s/lasso_sam_20160716/raw_model/sgp20160716_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,7,16,7),(2016,7,16,20)]
date_diurnal= [(2016,7,16,9),(2016,7,16,19)]
f160716     = var_l.ncload(name,file13,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_190716'
file14      =   '%s/lasso_sam_20160719/raw_model/sgp20160719_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,7,19,7),(2016,7,19,20)]
date_diurnal= [(2016,7,19,9),(2016,7,19,19)]
f190716     = var_l.ncload(name,file14,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_200716'
file15      =   '%s/lasso_sam_20160720/raw_model/sgp20160720_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,7,20,7),(2016,7,20,20)]
date_diurnal= [(2016,7,20,9),(2016,7,20,19)]
f200716     = var_l.ncload(name,file15,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_180816'
file16      =   '%s/lasso_sam_20160818/raw_model/sgp20160818_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,8,18,7),(2016,8,18,20)]
date_diurnal= [(2016,8,18,9),(2016,8,18,19)]
f180816     = var_l.ncload(name,file16,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

name        = 'lasso_190816'
file17      =   '%s/lasso_sam_20160819/raw_model/sgp20160819_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,8,19,7),(2016,8,19,20)]
date_diurnal= [(2016,8,19,9),(2016,8,19,19)]
f190816     = var_l.ncload(name,file17,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)


name        = 'lasso_300816'
file18      =   '%s/lasso_sam_20160830/raw_model/sgp20160830_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar    = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
date        = [(2016,8,30,7),(2016,8,30,20)]
date_diurnal= [(2016,8,30,9),(2016,8,30,19)]
f300816 = var_l.ncload(name,file18,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

