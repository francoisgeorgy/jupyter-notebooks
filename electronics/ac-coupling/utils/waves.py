import numpy as np

def squarewave(a, f, t):
    """
    Return a periodic square-wave waveform.

    Parameters
    ----------
    a : float
        Amplitude
    f : float
        Frequency in [Hz]
    t : array_like
        The input time array.

    Returns
    -------
        Output array containing the square waveform.
    """
    return a * np.sign(np.sin(2 * np.pi * f * t))

# periodic RC discharge
def periodic_RC_discharge(R, C, t, f):
    """
    Return the RC discharge waveform.

    Parameters
    ----------
    R : float
        Resistance in [Ohm]
    C : float
        Capacitor in [F]
    t : array_like
        The input time array.
    f : float
        The frequency at which the discharge repeats.

    Returns
    -------
        Output array containing the waveform.
    """
    tau = R*C
    return np.exp(-(np.mod(t-0.00000001, (1/f)/2)) / tau)