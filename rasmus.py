import numpy as np

class rasmus_fast:
    def __init__(self): self.name = "Rasmus' fast implementation"
        
    def Z(self, n, w):
        # Much faster than native python loop
        return 2*np.prod(np.exp(omega)+np.exp(-omega))
    
class rasmus_brute:
    def __init__(self): self.name = "Rasmus' vectorized brute implementation"
        
    def Z(self, n, w):
        # generate all states
        comb = np.arange(2**n)
        x = comb[None,:] & (1 << np.arange(n))[:,None]
        x = (x > 0) * 2 - 1
        
        # calculate all interactions and sum total energy of each state vector
        exponents = np.sum(-omega[:,None]*x[:-1]*x[1:], axis=0)
        return np.sum(np.exp(exponents))
