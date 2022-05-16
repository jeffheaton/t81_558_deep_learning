# Introduction
 
Starting in the spring semester of 2016, I began teaching the T81-558 Applications of Deep Learning course for Washington University in St. Louis. I never liked Microsoft Powerpoint for technical classes, so I placed my course material, examples, and assignments on GitHub. This material started with code and grew to include enough description that this information evolved into the book you see before you. 

I license the book's text under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. Similarly, I offer the book's code under the LGPL license. Though I provide this book both as a relatively inexpensive paperback and Amazon Kindle, you can obtain the book's PDF here:

* [https://arxiv.org/abs/2009.05673](https://arxiv.org/abs/2009.05673)

The book's code is available at the following GitHub repository:

* [https://github.com/jeffheaton/t81_558_deep_learning](https://github.com/jeffheaton/t81_558_deep_learning)

If you purchased this book from me, you have my sincere thanks for supporting my ongoing projects. I sell the book as a relatively low-cost paperback and Kindle ebook for those who prefer that format or wish to support my projects. I suggest that you look at the above GitHub site, as all of the code for this book is presented there as Jupyter notebooks that are entirely Google CoLab compatible. 

This book focuses on the application of deep neural networks. There is some theory; however, I do not focus on recreating neural network fundamentals that tech companies already provide in popular frameworks. The book begins with a quick review of the Python fundamentals needed to learn the subsequent chapters. With Python preliminaries covered, we start with classification and regression neural networks in Keras.

In my opinion, PyTorch, Jax, and Keras are the top three deep learning frameworks. When I first created this course, neither PyTorch nor JAX existed. I began the course based on TensorFlow and migrated to Keras the following semester. I believe TensorFlow remains a good choice for a course focusing on the application of deep learning. Some of the third-party libraries used for this course use PyTorch; as a result, you will see a blend of both technologies.  StyleGAN and TabGAN both make use of PyTorch. 

The technologies that this course is based on change rapidly. I update the Kindle and paperback books according to this schedule. Formal updates to this book typically occur just before each academic year's fall and spring semesters. 

The source document for this book is Jupyter notebooks. I wrote a Python utility that transforms my course Jupyter notebooks into this book. It is entirely custom, and I may release it as a project someday. However, because this book is based on code and updated twice a year, you may find the occasional typo. I try to minimize errors as much as possible, but please let me know if you see something. I use [Grammarly](https://www.grammarly.com/) to find textual issues, but due to the frequently updated nature of this book, I do not run it through a formal editing cycle for each release. I also double-check the code with each release to ensure CoLab, Keras, or another third-party library did not make a breaking change.

The book and course continue to be a work in progress. Many have contributed code, suggestions, fixes, and clarifications to the GitHub repository. Please submit a GitHub issue or a push request with a solution if you find an error.
