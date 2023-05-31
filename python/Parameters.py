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


file1   =   '%s/DADOS/raw_model/sgp20150606_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
f060615 =  var_l.ncload(file1,calendar)
#to work with a dictionary 
#var      = var_l.ncload(file1,calendar)
#f1 =  { 'name':'lasso_060615','date':[2015,6,6], 'data':var, 'var'=[var.MCUP]}


file2   =   '%s/DADOS/raw_model/sgp20150609_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
f090615 = var_l.ncload(file2,calendar)

file3   =   '%s/DADOS/raw_model/sgp20150627_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
f270615 = var_l.ncload(file3,calendar)

file4   =   '%s/DADOS/raw_model/sgp20150801_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
f010815 = var_l.ncload(file4,calendar)

file5   =   '%s/DADOS/raw_model/sgp20150829_rerun2020.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
f290815 = var_l.ncload(file5,calendar)

file6   =   '%s/DADOS/raw_model/sgp20160518_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f180516 = var_l.ncload(file6,calendar)

file7   =   '%s/DADOS/raw_model/sgp20160530_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f300516 = var_l.ncload(file7,calendar)

file8   =   '%s/DADOS/raw_model/sgp20160614_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f140616 = var_l.ncload(file8,calendar)

file9   =   '%s/DADOS/raw_model/sgp20160625_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f250616 = var_l.ncload(file9,calendar)

file10  =   '%s/DADOS/raw_model/sgp20160716_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f160716 = var_l.ncload(file10,calendar)

file11  =   '%s/DADOS/raw_model/sgp20160719_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f190716 = var_l.ncload(file11,calendar)

file12  =   '%s/DADOS/raw_model/sgp20160720_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f200716 = var_l.ncload(file12,calendar)

file13  =   '%s/DADOS/raw_model/sgp20160819_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f190816 = var_l.ncload(file13,calendar)

file14 =   '%s/DADOS/raw_model/sgp20160830_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
f300816 = var_l.ncload(file14,calendar)

