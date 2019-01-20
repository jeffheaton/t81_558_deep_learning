# Exports of my Anaconda Environments for TensorFlow

These are anaconda environments that I've created for various platforms. These all
assume that you are using [Miniconda](https://conda.io/miniconda.html).  If you use
the wrong platform below, or install to the full Anaconda (instead of Miniconda),
you will most likely run into specific library versions not being available
for your platform/Python version combination.  These environments all use
Python 3.6; however, you can still install 3.7 as your base Python.

To make use of one of them, download the YML file for your platform, and use
the following commands.

For Mac:

```
conda env create -f wustl-mac.yml
source activate wustl
python -m ipykernel install --user --name wustl --display-name "Python 3.6 (wustl)"
```

For Linux:

```
conda env create -f wustl-linux.yml
activate wustl
python -m ipykernel install --user --name wustl --display-name "Python 3.6 (wustl)"
```

For Windows:

```
conda env create -f wustl-win.yml
activate wustl
python -m ipykernel install --user --name wustl --display-name "Python 3.6 (wustl)"
```
