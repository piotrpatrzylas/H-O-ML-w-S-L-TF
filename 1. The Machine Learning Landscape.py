"""
1. How would you define Machine Learning?
It is teaching computer to learn without explicitly stating all the information/rules about the World.

2. Can you name four types of problems where it shines?
-complicated problems thad would require lots of tuning/instructions
-hard problems where no simple solution(s) exist
-problems for which inputs are changing rapidly, need to adapt/learn quickly
-getting insight from Big Data

3. What is a labeled training set?
This is a set used in supervised ML for training an algorithm. It contains y variable (response).

4. What are the two most common supervised tasks?
Classification and regression.

5. Can you name four common unsupervised tasks?
-clustering
-dimension reduction (PCA)
-visualization (dendrograms)
-anomaly detection

6. What type of ML algorithm would you use to allow a robot to walk in various unknown terrains?
Monte Carlo algorithm in Reinforced ML.

7. What type of algorithm would you use to segment your customers into multiple groups?
Some sort of Unsupervised ML clustering algorithm - like. hierarchical clustering.

8. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem.
This would be (at least initially) supervised learning problem - we need to give an example/define what spam is and what
spam is not. We could also try to use unsupervised ML - for example to cluster emails into 2 groups hoping that they
will be divided into spam and not-spam, however results for this could far from ideal.

9. What is an online learning system?
Online learning system is system that is updated in small batches continuously

10. What is out-of-core learning?
This is a type of online learning system where data is too big to fit into computers memory - it must bu cut into chunks.

11. What type of learning algorithm relies on a similarity measure to make prediction?
Instance based learning algorithm.

12. What is the difference between a model parameter and a learning algorithm hyperparameter?
Parameter is parameter of the model (for example what features should we include in our model)
Hyperparameter is parameter of the algorithm (for example how flexible should algorithm be)

13. What do model-based learning algorithms search for? What is the most common strategy they use do success?
How do they make predictions?
Model-based ML algorithm would search for the most optimal values for a given model (like linear regression).
The most common strategy is to minimise the cost function.
To make prediction we can feed new data into obtained model.

14. Can you name four of the main challenges in ML?
-insufficient quantity of data
-nonrepresantive data/biased data
-poor quality data
-using wrong models for a given data (under- and over-fit)

15. If your model performs great on the training data but generalizes poorly to new instances, what is happening?
Can you name 3 possible solutions?
The model overfits the data.
-using simpler models
-using more data
-reducing noise in a data

16. What is a test set and why would you want to use it?
Test set is a subset of the data not used in a training of ML algorithm.
It is used to check how model performs with unseen data.

17. What is the purpose of a validation set?
This is a subset of data used to compare different models.

18. What can go wrong if you tune hyperparameters using the test set?
It can results in over-fitting

19. What is cross-validation and why would you prefer it to a validation set?
This is technique used to compare different models/check performance of the model without
splitting data into test/validation set.
"""