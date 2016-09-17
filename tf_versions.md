TensorFlow Versions
===================

TensorFlow versions happen often, nearly monthly.  They often change syntax and break things
that are based on TensorFlow.  This class is standardized on TensorFlow 0.8 (for this semester).
If you are using [IBM Data Scientist Workbench](https://datascientistworkbench.com/), you already
have TensorFlow 0.8 installed.

If you are installing directly to your computer, I suggest installing TensorFlow 0.8. 
This should only be done AFTER you have installed [Anaconda Python 3.5](https://www.continuum.io/downloads).

Install TensorFlow 0.8 for Mac
------------------------------

```
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.8.0-py3-none-any.whl
sudo pip install --upgrade $TF_BINARY_URL
```

Install TensorFlow 0.8 for Linux
--------------------------------

```
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp34-cp34m-linux_x86_64.whl
pip install --ignore-installed --upgrade $TF_BINARY_URL
```


TensorFlow 0.8 for Windows
--------------------------

I suggest trying [IBM Data Scientist Workbench](https://datascientistworkbench.com/) or 
using my Linux virtual machine that has everything installed.  You can download my VM
from Blackboard.