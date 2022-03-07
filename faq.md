# T81-558: Applications of Deep Neural Networks
**Frequently Asked Questions (FAQ)**
* Instructor: [Jeff Heaton](https://sites.wustl.edu/jeffheaton/), McKelvey School of Engineering, [Washington University in St. Louis](https://engineering.wustl.edu/Programs/Pages/default.aspx)
* For more information visit the [class website](https://sites.wustl.edu/jeffheaton/t81-558/).

**********************************************************************************************************************
# Missing submit Function

**Problem:**
```
NameError: name 'submit' is not defined
```

**Solution:**
All of the assignments contain a cell that defines the submit function.  Make sure you have run this cell. Notebooks usually require all cells to be run, starting from the top.

**********************************************************************************************************************
# Can't Find Notebook

**Problem:**
```
FileNotFoundError: [Errno 2] No such file or directory: '/Users/jeffh/projects/t81_558_deep_learning/t81_558_class1_intro_python.ipynb'
```
**Solution:**
The path that you are specifying for your assignment .ipynb file is not correct. I provide code to help you locate the assignment [here](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class1.ipynb).

**********************************************************************************************************************
# Submit Data Too Large

**Problem:**
```
Failure: HTTP content length exceeded 10485760 bytes.
```

**Solution:**
I see that error sometimes. Basically AWS Lambda only allows the HTTP request to go up to a certain size. All of my assignments stay well below the limit you are hitting. This means that the amount of data you are generating is far enough above what I am experiencing that you get this error. I would have a look at the number of rows, you are generating.


**********************************************************************************************************************
# Passing non-numeric values to model.fit

**Problem:**
```
ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type float).
```

**Solution:**
Print out your "x" being passed to the model.fit:

```
>>> x
array([['b', -0.9566132133203712, 'u', ..., 1, 1, 0],
       ['a', -0.06005052977584876, 'u', ..., 1, 1, 0],
       ['a', -0.8561017017122409, 'u', ..., 0, 1, 0],
       ...,
       ['a', 1.7571976000991476, 'y', ..., 1, 0, 1],
       ['b', -0.9154034935610378, 'u', ..., 0, 1, 0],
       ['b', -0.2781605099654916, 'u', ..., 0, 0, 1]], dtype=object)
```

See the character values? Those need to either be dropped or converted to dummy (and then dropped) before you call df.values.

**********************************************************************************************************************
# Dataframe not Callable (missing brackets)

**Problem:**
```
TypeError: 'DataFrame' object is not callable
```

**Solution**

You are missing brackets in your call to submit, you probably have simiar to:

```
submit(source_file=file,data=df_submit,key=key,no=1) #assuming assignment 1.
```

Should be:

```
submit(source_file=file,data=[df_submit],key=key,no=1)
```