import os

#Repository location 
computer   = '/dados/bamc/jhonatan.aguirre/DATA/LASSO'

#Figure out folder  
#path = "../doc/figure_out/"
#Figure out folder  
path = "/home/jhonatan.aguirre/repositories/relatorio_2024_1/figs"


#forcing= ''%(computer)

# Check if the directory exists
if not os.path.exists(path):
    # If it doesn't exist, create it
    os.makedirs(path)


file_fig= path
file_temporal= path

#Size in inches to make the temporal plots
tplot_size=1.0

