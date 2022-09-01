numpy.fft vs scipy.fft ?
------------------------

- https://stackoverflow.com/questions/6363154/what-is-the-difference-between-numpy-fft-and-scipy-fftpack

**Choice : scipy.fft**

Doc : https://docs.scipy.org/doc/scipy/reference/fft.html

Good to know
------------

In the frequency domain, the overall average of a signal is its content at DC or 0Hz, So that's why there's a peak at 0Hz.

A DC offset can be removed by subtracting the average level of the waveform before the DFT or FFT.


sci.fft
-------

`scipy.fft.fftfreq` : Return the Discrete Fourier Transform sample frequencies


Examples
--------

- https://scikit-dsp-comm.readthedocs.io/en/latest/nb_examples/Continuous-Time%20Signals%20and%20Systems%20using%20sigsys.html
- [Understanding Audio data, Fourier Transform, FFT and Spectrogram features for a Speech Recognition System](http://www.ivan123.tech/?p=255)
- [Plot FFT using Python](https://www.gaussianwaves.com/2020/01/how-to-plot-fft-in-python-fft-of-basic-signals-sine-and-cosine-waves/)

Books
-----

- Elegant SciPy - The Art of Scientific Python
  - https://github.com/elegant-scipy/elegant-scipy
    - https://github.com/elegant-scipy/notebooks
- Digital Modulations using Python
  - https://www.gaussianwaves.com/digital-modulations-using-python/