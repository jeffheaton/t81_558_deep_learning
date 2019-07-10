# T81 558:Applications of Deep Neural Networks
[Washington University in St. Louis](http://www.wustl.edu)

Instructor: [Jeff Heaton](https://sites.wustl.edu/jeffheaton/)

**The content of this course changes as technology evolves**, to keep up to date with changes [follow me on GitHub](https://github.com/jeffheaton).

Fall 2019, Mondays, Section 1: 2:30P-5:20P, Section 2: 6-9:00P, Online and in class room: TBA

# Course Description

Deep learning is a group of exciting new technologies for neural networks. Through a combination of advanced training techniques and neural network architectural components, it is now possible to create neural networks that can handle tabular data, images, text, and audio as both input and output. Deep learning allows a neural network to learn hierarchies of information in a way that is like the function of the human brain. This course will introduce the student to classic neural network structures, Convolution Neural Networks (CNN), Long Short-Term Memory (LSTM), Gated Recurrent Neural Networks (GRU), General Adversarial Networks (GAN) and reinforcement learning.  Application of these architectures to computer vision, time series, security, natural language processing (NLP), and data generation will be covered. High Performance Computing (HPC) aspects will demonstrate how deep learning can be leveraged both on graphical processing units (GPUs), as well as grids. Focus is primarily upon the application of deep learning to problems, with some introduction to mathematical foundations. Students will use the Python programming language to implement deep learning using Google TensorFlow and Keras. It is not necessary to know Python prior to this course; however, familiarity of at least one programming language is assumed. This course will be delivered in a hybrid format that includes both classroom and online instruction.

# Objectives

1. Explain how neural networks (deep and otherwise) compare to other machine learning models.
2. Determine when a deep neural network would be a good choice for a particular problem.
3. Demonstrate your understanding of the material through a final project uploaded to GitHub.

# Syllabus
This syllabus presents the expected class schedule, due dates, and reading assignments.  [Download current syllabus.](https://raw.githubusercontent.com/jeffheaton/t81_558_deep_learning/master/pdf/t81_558_spring2019_syllabus.pdf)

Module|Content
---|---
[Module 1](t81_558_class_01_1_overview.ipynb)<br>**Meet on 08/26/2019** | <ul><li>Part 1.1: Course Overview<li>Part 1.2: Introduction to Python<li>Part 1.3: Python Lists, Dictionaries, Sets & JSON<li>Part 1.4: File Handling<li>Part 1.5: Functions, Lambdas, and Map/ReducePython Preliminaries<li>**We will meet on campus this week!** (first meeting)</ul>
[Module 2](t81_558_class_02_1_python_pandas.ipynb)<br>Week of 09/09/2019 | <ul><li>	Part 2.1: Introduction to Pandas for Deep Learning<li>Part 2.2: Encoding Categorical Values in Pandas<li>Part 2.3: Grouping, Sorting, and Shuffling<li>Part 2.4: Using Apply and Map in Pandas<li>Part 2.5: Feature Engineering in Padas<li>[Module 1 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class1.ipynb) Due: 09/10/2019</ul>
[Module 3](t81_558_class_03_1_neural_net.ipynb)<br>Week of 09/16/2019 | <ul><li>Part 3.1: Deep Learning and Neural Network Introduction<li>Part 3.2: Introduction to Tensorflow & Keras<li>Part 3.3: Saving and Loading a Keras Neural Network<li>Part 3.4: Early Stopping in Keras to Prevent Overfitting<li>Part 3.5: Extracting Keras Weights and Manual Neural Network Calculation<li>TensorFlow and Keras for Neural Networks<li>[Module 2: Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class2.ipynb) due: 09/17/2019</ul>
[Module 4](t81_558_class_04_1_feature_encode.ipynb)<br>Week of 09/23/2019 | <ul><li>Part 4.1: Encoding a Feature Vector for Keras Deep Learning<li>Part 4.2: Keras Multiclass Classification for Deep Neural Networks with ROC and AUC<li>Part 4.3: Keras Regression for Deep Neural Networks with RMSE<li>Part 4.4: Backpropagation, Nesterov Momentum, and ADAM Training<li>Part 4.5: Neural Network RMSE and Log Loss Error Calculation from Scratch<li>[Module 3 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class3.ipynb) due: 09/24/2019</ul>
[Module 5](t81_558_class_05_1_reg_ridge_lasso.ipynb)<br>**Meet on 09/30/2019** | <ul><li>Part 5.1: Introduction to Regularization: Ridge and Lasso<li>Part 5.2: Using K-Fold Cross Validation with Keras<li>Part 5.3: Using L1 and L2 Regularization with Keras to Decrease Overfitting<li>Part 5.4: Drop Out for Keras to Decrease Overfitting<li>Part 5.5: Bootstrapping and Benchmarking Hyperparameters<li>[Module 4 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class4.ipynb) due: 10/01/2019<li>**We will meet on campus this week!** (2nd Meeting)</ul>
[Module 6](t81_558_class_06_1_python_images.ipynb)<br>Week of 10/07/2019 | <ul>	• Part 6.1: Image Processing in Python<li>Part 6.2: Keras Neural Networks for MINST and Fashion MINST<li>Part 6.3: Implementing a ResNet in Keras<li>Part 6.4: Computer Vision with OpenCV<li>Part 6.5: Recognizing Multiple Images with Darknet<li>[Module 5 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class5.ipynb) due: 10/08/2019</ul>
[Module 7](t81_558_class_07_1_gan_intro.ipynb)<br>Week of 10/14/2019 | <ul><li>Part 7.1: Introduction to GANS for Image and Data Generation<li>Part 7.2: Implementing a GAN in Keras<li>Part 7.3: Face Generation with StyleGAN and Python<li>Part 7.4: GANS for Semi-Supervised Learning in Keras<li>Part 7.5: An Overview of GAN Research<li>[Module 6 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class6.ipynb) due: 10/15/2019</ul>
[Module 8](t81_558_class_08_1_kaggle_intro.ipynb)<br>**Meet on 10/21/2019** | <ul><li>Part 8.1: Introduction to Kaggle<li>Part 8.2: Building Ensembles with Scikit-Learn and Keras<li>Part 8.3: How Should you Architect Your Keras Neural Network: Hyperparameters<li>Part 8.4: Bayesian Hyperparameter Optimization for Keras<li>Part 8.5: Current Semester's Kaggle<li>[Module 7 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class7.ipynb) due: 10/22/2019<li>**We will meet on campus this week!** (3rd Meeting)</ul>
[Module 9](t81_558_class_09_1_keras_transfer.ipynb)<br>Week of 10/28/2019 | <ul><li>Part 9.1: Introduction to Keras Transfer Learning<li>Part 9.2: Popular Pretrained Neural Networks for Keras. <li>Part 9.3: Transfer Learning for Computer Vision and Keras<li>Part 9.4: Transfer Learning for Languages and Keras<li>Part 9.5: Transfer Learning for Keras Feature Engineering<li>Regularization and Dropout<li>[Module 8 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class8.ipynb) due: 10/29/2019</ul>
[Module 10](t81_558_class_10_1_timeseries.ipynb)<br>Week of 11/04/2019 | <ul><li>Part 10.1: Time Series Data Encoding for Deep Learning, TensorFlow and Keras<li>Part 10.2: Programming LSTM with Keras and TensorFlow<li>Part 10.3: Image Captioning with Keras and TensorFlow<li>Part 10.4: Temporal CNN in Keras and TensorFlow<li>Part 10.5: Predicting the Stock Market with Keras and TensorFlow<li>Time Series and LSTM/GRU Networks<li>[Module 9 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class9.ipynb) due: 11/05/2019</ul>
[Module 11](t81_558_class_11_01_spacy.ipynb)<br>Week of 11/11/2019 | <ul><li>Natural Language Processing<li>[Module 10 Assignment](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/assignments/assignment_yourname_class10.ipynb) due: 11/12/2019</ul>
[Module 12](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class12_security.ipynb)<br>**Meet on 11/18/2019** | <ul><li>Security and Deep Learning<li>Kaggle Assignment due: 11/17/2019 (approx 4-6PM, due to Kaggle GMT timezone)<li>**We will meet on campus this week!** (4th Meeting)
[Module 13](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class13_adv.ipynb)<br>Week of 11/25/2019 | <ul><<li>Advanced/New Deep Learning Topics</ul>
[Module 14](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class14_aws.ipynb)<br>Week of 12/02/2019 | <ul><li>GPU, HPC and Cloud<li>Final Project due 12/09/2019</ul>


# Datasets

* [Iris](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/datasets_iris.ipynb) - Classify between 3 iris species.
* [Auto MPG](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/datasets_mpg.ipynb) - Regression to determine MPG.
* [WC Breast Cancer](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/datasets_wcbc.ipynb) - Binary classification: malignant or benign.
* [toy1](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/datasets_toy1.ipynb) - The toy1 dataset, regression for weights of geometric solids.

*Note: Other datasets may be added as the class progresses.*

# Final Project

For the final project you can choose a security project or choose your own dataset to create and fit a neural network.  For more information:

* Security Project - See Canvas for more information.
* [Independent Project](https://github.com/jeffheaton/t81_558_deep_learning/raw/master/pdf/t81_558_independent_project.pdf) - Choose your own dataset or one of my suggestions.

# Other Information

* [Helpful Functions](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/jeffs_helpful.ipynb) - Helpful Python functions for this class.
* [KDD99 Example](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/tf_kdd99.ipynb)
* [Care and Feeding of Python](http://www.heatonresearch.com/content/python_care.html) - Some useful commands for a local Python install.  Not needed if you are using Data Scientist Workbench.
