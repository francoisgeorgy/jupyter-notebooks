# Jupyter notes

Install :

    pip install ipywidgets


Magic commands
--------------

https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-matplotlib

### `%matplotlib inline`

Content in preparation...

- https://github.com/ipython/ipython/issues/12190

    

MatPlotLib
----------

- https://nbviewer.org/github/ipython/ipython/blob/1.x/examples/notebooks/Part%203%20-%20Plotting%20with%20Matplotlib.ipynb
- https://www.data-blogger.com/python-matplotlib-pyplot-a-perfect-combination/

Output configuration :

- https://twitter.com/tedpetrou/status/1238812794218307590?lang=en

From https://ipython.readthedocs.io/en/stable/interactive/plotting.html :

> Running import matplotlib.pyplot as plt also registers this same function, so as of now it's not necessary to even 
> use %matplotlib inline if you use pyplot or a library that imports pyplot like pandas or seaborn.

See also : https://github.com/ipython/ipython/issues/12190

### %matplotlib backends :

`%matplotlib` must be called before any plotting or import of matplotlib.

    %matplotlib --list
    %matplotlib inline - Figures are shown as static png images (optionally svg if configured)
    %matplotlib notebook or %matplotlib nbagg - Interactive Figures inside the notebook
    %matplotlib widgets - - Interactive Figures inside the notebook (requires jupyter-matplotlib to be installed)
    %matplotlib tk or %matplotlib qt etc. - GUI windows show the figure externally to the notebook with the given interactive backend

### inline :

`%matplotlib inline` 

With this backend, the output of plotting commands is displayed inline within frontends like the Jupyter notebook, 
directly below the code cell that produced it. The resulting plots will then also be stored in the notebook document.

### interactive :

`%matplotlib notebook`
`%matplotlib widget`

With this backend, the output is an interactive plots embedded within the notebook, that can be zoomed and resizeed.

### Configure a default backend :

1. Edit file ~/.ipython/profile_default/ipython_config.py
2. Add line c.InteractiveShellApp.matplotlib = 'inline'


Widgets
-------

https://ipywidgets.readthedocs.io/en/stable/


Problems
--------

With : 

    %matplotlib widget

we get the error :
 
    ModuleNotFoundError: No module named 'ipympl'

Solution :

    pip install ipympl



