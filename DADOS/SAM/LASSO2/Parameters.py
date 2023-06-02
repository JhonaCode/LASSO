########################################################
#File to define the direction of the SAM run´s.
########################################################

### My own files 

##Adress of the computer
from     files_direction  import *  

import   source.var_files.var_to_load_sam_core  as var_c

########################################################
#Files of SAM to load. 
########################################################



#Lasso run id 100, teste sam micro
file_1 = '%s/home/jhona/git_repositories/LASSO/DADOS/SAM/LASSO2/OUT_STAT/LASSO_teste2.nc'%(computer)
calendar = ['days  since 2014-12-31 00:00:00 +06:00:00','gregorian']
LASSO_teste2 = var_c.ncload(file_1,calendar)



#Lasso run id 100, teste sam micro
file_2 = '%s/home/jhona/git_repositories/LASSO/DADOS/SAM/LASSO2/OUT_STAT/LASSO_teste3.nc'%(computer)
calendar = ['days  since 2014-12-31 00:00:00 +06:00:00','gregorian']
LASSO_teste3 = var_c.ncload(file_2,calendar)



#Lasso run id 100, teste sam micro
file_3 = '%s/home/jhona/git_repositories/LASSO/DADOS/SAM/LASSO2/OUT_STAT/LASSO_teste4.nc'%(computer)
calendar = ['days  since 2014-12-31 00:00:00 +06:00:00','gregorian']
LASSO_teste4 = var_c.ncload(file_3,calendar)
