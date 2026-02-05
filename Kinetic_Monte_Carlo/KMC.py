#KMc
#%%
import numpy as np 
import numba 
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
    pos_array = []
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
        pos_array.append(position.copy())
        
    
    return pos_array

#%%test KMC1
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
    pos_array = []
    for i in range(N):
        x_1 = np.random.rand(1)[0]
        x_2 = np.random.randint(0,4,1)[0]
        if x_1*gamma > 0 and x_1*gamma < gamma_1 : 
            #hopping from O to another O 
            
            if x_2 <= 1 :
                if position[2] == 
                position[0] = position[0] + d_1
                position[2] =
            elif :
                
            else :
                
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
        pos_array.append(position.copy())
        
    
    return pos_array
