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
name       = 'teste1'
date       = [(2024,1,1,7),(2024,1,1,20)]
date_diurnal=[(2024,1,1,7),(2024,1,1,19)]
calendar   = ["days  since 2024-01-01 00:00:00 +06:00:00",'gregorian']
file1      = '%s/SAM_OWN/OUT_STAT/LASSO_lasso_sam_lsf_144x226_100_50m_0p5.nc'%(computer)
teste      =  var_l.ncload(name,file1,calendar,var1d,var2d,vars_diurnal,date,date_diurnal)

