########################################################
#Fredrick Kofi Tam                                  ####
#fkt2105                                            ####
#Assignment 4 Part b                                ####
# ENGI E1006                                        ####
#                                                   ####
########################################################


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
def read_grid(filename):
    """Create a site vacancy matrix from a text file.

    filename is a String that is the name of the 
    text file to be read. The method should return 
    the corresponding site vacancy matrix represented
    as a numpy array
    """
    #opens the file to read it
    input_file= open(filename, 'r')
    
    #saves the first line of the file as it is
    x= int(input_file.readline())
    
    #reads the rest of the file as a numpy array of booleans
    a = np.fromstring(input_file.read(),dtype=bool,sep=' ')
    
    #reshapes the array into a matrix with nXn dimensions 
    a.shape= (x,x)
    
    #closes file 
    input_file.close()
    
    #defines sites as a numpy array that is the opposite of a 
    sites=np.logical_not(a)
    return sites

def write_grid(filename,sites):
    """Write a site vacancy matrix to a file.

    filename is a String that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    #opens the file to write
    output_file= open(filename, 'w')
    
    #for the first line, takes the length of sites and writes that 
    output_file.write(str(len(sites)) + '\n')
    
    #writes sites into the file and closes file 
    np.savetxt(output_file,np.logical_not(sites),fmt='%u',delimiter=' ')
    output_file.close()
    print (' file has been created!') 


def undirected_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through undirected percolation
    """
    #start with an array of zeros (full) boolean is False 
    full=np.zeros(sites.shape, dtype=bool) 
    
    #traverses the first line of the array 
    for i in range(len(sites)):
        flow_from(sites,full, 0, i)
    return full

def flow_from(sites,full,i,j):
    """Adjusts the full array for flow from a single site

    This method does not return anything. It changes the array full
    """
    if i < 0 or j >= len(full):
        return
    if j < 0 or i >= len(full):
        return
    if not sites[i][j]:
        return
    if full[i][j]:
        return
    full[i][j] = True
    flow_from(sites,full,i+1,j)
    flow_from(sites,full,i,j+1)
    flow_from(sites,full,i, j-1)

def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """
    #checks the bottom row of full
    end = bool(sum(flow_matrix[len(flow_matrix)-1]))
    return end
def make_sites(p,n):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """
    #creates an array whose elements are ones and zeros 
    sites=np.random.binomial(1,p,(n,n))
    
    #converts  elements of sites into booleans
    sites=(sites==1)
    
    #returns sites 

    return sites

def show_perc(sites):
    """Displays a matrix using three colors for vacant, blocked, full
    
    Used to visualize undirected flow on the matrix sites.
    """
    #assigns full equal to the undericted_flow function 
    full= undirected_flow(sites)
    v = sites.astype(int) + full.astype(int)
    
    #uses matplotlib to visualize the flow 
    plt.matshow(v)
    plt.show()
    print ("hi") 
 
def make_plot(trials,n):
    """"generates and displays a graph of percolation p vs. vacancy p

    estimates percolation probability on an nxn grid for undirected 
    percolation by running a Monte Carlo simulation using the variable trials number
    of trials for each point. 
    """
    #divides up the points between three areas, with the middle one 
    #having the largest concentration 
    a1= np.linspace(0,0.5, int(15))
    a2= np.linspace(0.5, 0.7,int(70)) 
    a3=np.linspace(0.7,1, int(15))
    vac_prob= np.concatenate((a1, a2, a3))
    
    #opens an empty array named perc_prob 
    perc_prob= []
    plt.figure(2)
    #uses the new function written below to append the empty array
    for p in vac_prob:
        perc_prob.append(estimate(trials,n,p))
    plt.plot(vac_prob, perc_prob)
    plt.xlabel('probability of vacancy')
    plt.ylabel('probability of percolation')
    plt.title('vaccancy probability vs. percolation probability')
    plt.savefig('graph1.pdf')
    plt.show()
def estimate(trials, n, p):
        successes= 0 
        for i in range (0, trials):
            sites= make_sites(p,n)
            full= undirected_flow(sites)
            if percolates(full):
                successes= successes+1
        return (float(successes/trials))
                
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
