import numpy as np

def get_squarewave(a, f, t):    
    return a * np.sign(np.sin(2 * np.pi * f * t))

# periodic RC discharge
def get_periodic_RC_discharge(R, C, t, f):
    tau = R*C
    return np.exp(-(np.mod(t-0.00000001, (1/f)/2)) / tau)