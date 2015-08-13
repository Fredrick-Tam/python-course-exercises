#############################################
#Fredrick Kofi Tam                          #
#Uni: fkt2105                               #
#Assignment 4                               #                           
#E1006                                      #
#############################################

import numpy as np

def read_grid(filename):
    """Create a site vacancy matrix from a text file.
    filename is a String that is the name of the 
    text file to be read. The method should return 
    the corresponding site vacancy matrix represented
    as a numpy array
    """
     
    input_matrix = open(filename,'r')
    line = int(input_matrix.readline())
    matrix = np.fromstring(input_matrix.read(), dtype=bool,sep=" ")
    matrix.shape = (line,line)
    sites = matrix >0.5 
    input_matrix.close()
    return sites
def write_grid(filename,sites):
    """Write a site vacancy matrix to a file.

    filename is a String that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    output_matrix = open(filename, 'w')
    size = len(sites)
    output_matrix.write(str(size))
    output_matrix.write('\n')
    np.savetxt(output_matrix, sites.astype(int), fmt = '%u', delimiter =" ")
    output_matrix.close()
    print("file has been overwritten")

def flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through vertical percolation
    """
    flow_matrix = sites
    size = len(flow_matrix)
    for i in range(1,size):
        for j in range(size):
            flow_matrix[i][j] and flow_matrix[i-1][j]
    return flow_matrix
    
def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """
    
    size = len(flow_matrix)
    if sum(flow_matrix[size-1])==0:
        return True
    else:
        return False
    
    
def make_sites(p,n):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """
    d= np.random.binomial(1,p,(n,n))
    new_array = (d==1)
    return new_array

    
    
    
     
     
     
      
