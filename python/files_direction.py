import os

#Repository location 
computer   = '/pesq/dados/bamc/disk04/jhonatan/git_repositories/LASSO'

#Figure out folder  
path = "../doc/figure_out/"

# Check if the directory exists
if not os.path.exists(path):
    # If it doesn't exist, create it
    os.makedirs(path)


file_fig= path
