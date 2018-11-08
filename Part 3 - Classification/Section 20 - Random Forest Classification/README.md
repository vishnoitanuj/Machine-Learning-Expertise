# Random Forest Classification

Step 1: Pick at random K data points from the training set.

Step 2: Build the decision tree associated to these K data points.

Step 3: Choose the number Ntree of trees you want to build and repeat Steps 1 & 2.

Step 4: For a new data point, make each one of your Ntree trees predict the category to which the data points belongs, and assign the new data point to the category that wins the majority vote.