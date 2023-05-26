########################################################
#File to define the direction of the SAM runs.
########################################################

### My own files 

##Adress of the computer
from     files_direction  import *

import   sam_python.var_files.var_to_load_sam_lasso  as var_c


#shca , 12 point per hours statistics , 100 m resolution 
file_1 = '%s/home/jhona/git_repositories/LASSO/DADOS/SAM/LASSO/OUT_STAT/LASSO_teste2.nc'%(computer)
calendar = ['days  since 2014-12-31 00:00:00 +06:00:00','gregorian']
l2 = var_c.ncload(file_1,calendar)


#shca , 12 point per hours statistics , 100 m resolution 
file_2 = '%s/home/jhona/git_repositories/LASSO/DADOS/SAM/LASSO/OUT_STAT/LASSO_teste3.nc'%(computer)
calendar = ['days  since 2014-12-31 00:00:00 +06:00:00','gregorian']
l3 = var_c.ncload(file_2,calendar)
