# Exports of my Anaconda Environments for TensorFlow

These are anaconda environments that I've created for various platforms.  

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
