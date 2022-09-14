import matplotlib.pyplot as pp
import numpy as np
import scipy.fftpack

def plot(t, data, axes, title='', ymin=None, ymax=None):
    axes.plot(t, data)    
    if ymin is not None:
        axes.set_ylim(bottom=ymin)
    if ymax is not None:
        axes.set_ylim(top=ymax)
    axes.set_title(title)    
    axes.grid(True)
    
def plot_fft(data, f, periods, axes, title=''):

    samples = len(data)
    spacing = 1 / f * periods / samples
    x = scipy.fft.fftfreq(samples, spacing)[:samples//2]
    
    y = scipy.fft.fft(data)
    samples = len(y)
    axes.semilogy(x, 2.0/samples * np.abs(y[0:samples//2]))
    # axes.plot(x, 2.0/samples * np.abs(y[0:samples//2]))
    axes.set_xlim(left=0, right=1000)
    axes.set_ylim(10e-5, 10)
    axes.set_title(title)
    axes.grid(True)

def plot_fft_diff(data1, data2, f, periods, axes, title=''):

    if len(data1) != len(data2):
        print("ERROR: data not similar for plotting differences")
        return
    
    samples = len(data1)
    spacing = 1 / f * periods / samples
    x = scipy.fft.fftfreq(samples, spacing)[:samples//2]

    y1 = scipy.fft.fft(data1)
    y2 = scipy.fft.fft(data2)
    samples = len(y1)
    # len(y2) must be equal to len(y1)
    # print(2.0/samples * (np.abs(y1[0:samples//2])))
    # print(2.0/samples * (np.abs(y2[0:samples//2])))
    # print(2.0/samples * (np.abs(y1[0:samples//2]) - np.abs(y2[0:samples//2])))
    # for n in range(0, 100):
        # print(np.abs(y1[n]), np.abs(y2[n]), np.abs(y1[n]) - np.abs(y2[n]))
    axes.plot(x, 2.0/samples * (np.abs(y1[0:samples//2]) - np.abs(y2[0:samples//2])))
    axes.set_xlim(left=0, right=1000)
    axes.set_ylim(10e-5, 10)
    axes.set_title(title)
    axes.grid(True)