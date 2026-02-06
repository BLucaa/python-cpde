#KMc
"""
Kinetic Monte Carlo Simulation Module
=====================================

This module provides functions for performing Kinetic Monte Carlo (KMC) simulations
of hydrogen atom hopping on lattice structures.

The module includes:
    - KMC1: Simple 2D lattice hopping simulation
    - KMC2: 2D lattice hopping with multiple transition types

Example:
    >>> import numpy as np
    >>> from KMC import KMC1, KMC2
    >>> 
    >>> # Simple 2D simulation
    >>> initial_pos = [0, 0]
    >>> trajectory = KMC1(initial_pos, 0.5, 0.5, 1000)
"""
#%%
import numpy as np 
import numba 
import math
#%%Kinetic Monte Carlo

@numba.jit(nopython=True)
def KMC1(position_0, gamma_1, gamma_2,N):
    """
    KMC on a normalized lattice 
    simple hopping of an hydrigen atom on a lattice 
    
    Args:
        position_0 (_type_): _description_
        gamma_1 (_type_): _description_
        gamma_2 (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    position = position_0.copy()
    gamma = gamma_1 + gamma_2
    pos_array = np.zeros((N, 2), dtype=np.float64)
    for i in range(N):
        x_1 = np.random.rand(1)[0]
        x_2 = np.random.randint(0,4,1)[0]
        if x_1*gamma > 0 and x_1*gamma < gamma_1 :
            
            if x_2 <= 1 :
                position[0] = position[0] + (-1)**x_2
            else :
                position[1] = position[1] + (-1)**x_2
        elif gamma*x_1 > gamma_1 : 
            if x_2 == 0 :
                position[1] = position[1] - 1
                position[0] = position[0] + 1
            elif x_2 == 1 :
                position[1] = position[1] + 1
                position[0] = position[0] - 1
            elif x_2 == 2 :
                position[1] = position[1] - 1
                position[0] = position[0] - 1
            else :
                position[1] = position[1] + 1
                position[0] = position[0] + 1
        
        pos_array[i, 0] = position[0]
        pos_array[i, 1] = position[1]
        
        
    
    return pos_array

#%%test KMC1
if __name__ == "__main__":
        
    position_0 =[0,0]
    gamma_1 =1/2
    gamma_2 = 1/2
    N=200
    a= np.array(KMC1(position_0, gamma_1, gamma_2,N))
    print(a) 

#%% KMC 2 
@numba.jit(nopython=True)
def KMC2(position_0, gamma_1, gamma_2, a,b ,N):
    """_summary_

    Args:
        position_0 (_type_): _description_
        gamma_1 (_type_): _description_
        gamma_2 (_type_): _description_
        a (_type_): _description_
        b (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    position = position_0.copy()
    gamma = gamma_1 + gamma_2
    d_1 = a - 2*b
    d_2 = math.sqrt(2)*b
    pos_array = np.zeros((N, 3), dtype=np.float64)
    
    for i in range(N):
        x_1 = np.random.rand(1)[0]
        x_2 = np.random.randint(0,2,1)[0]
        if x_1*gamma > 0 and x_1*gamma < gamma_1: 
            #hopping from O to another O 
            if position[2]==1 :
                position[0] = position[0] + d_1
                position[2] = 3
            elif position[2]==3 : 
                position[0] = position[0] - d_1
                position[2] = 1
            elif position[2] == 0 :
                position[1] = position[1] + d_1
                position[2] = 2
            else :
                position[1] = position[1] - d_1
                position[2] = 0
                
        elif  gamma*x_1 > gamma_1 : 
            #rotation around the atom 
            if position[2] == 0: 
                position[1] = position[1] - b 
                if x_2 == 0 : 
                    position[0] = position[0] + b 
                    position[2] = 1
                else : 
                    position[0] = position[0] - b
                    position[2] = 3
                    
            elif position[2] == 1: 
                position[0] = position[0] - b 
                if x_2 == 0 : 
                    position[1] = position[1] + b
                    position[2] = 0 
                else : 
                    position[1] = position[1] - b
                    position[2] = 2
            
            elif position[2] == 2: 
                position[1] = position[1] + b 
                if x_2 == 0 : 
                    position[0] = position[0] + b
                    position[2] = 1
                else : 
                    position[0] = position[0] - b
                    position[2] = 3
                    
            elif position[2] == 3: 
                position[0] = position[0] + b 
                if x_2 == 0 : 
                    position[1] = position[1] + b 
                    position[2] = 0
                else : 
                    position[1] = position[1] - b
                    position[2] = 2
            
        pos_array[i, 0] = position[0]
        pos_array[i, 1] = position[1]
        pos_array[i, 2] = position[2]
        
    return pos_array

#%%test KMC2
if __name__ == "__main__" : 
    position_0 =[0,1,0]
    gamma_1 = 0
    gamma_2 = 1
    a=1
    b=1
    N=200
    a= np.array(KMC2(position_0, gamma_1, gamma_2, a,b ,N))
    print(a) 
