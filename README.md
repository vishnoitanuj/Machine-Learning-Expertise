# Random Forest

Ensemble Learning: Take multiple algorithms or an algo multiple times to make a more powerful model

### Steps:
1) Pick at random K data points from the training set
2) Build the DT associated to these K data points
3) Choose the number Ntree of tree you want to build and repeat steps 1 & 2
4) For a new data point, make each one of your Ntree trees predict the value of Y to for the data point in question, and assign the new data point the average across all of the predicted Y values

Random Forest is a team of Decision Trees.
#### Note: The number of steps does not depend on the number of tress. The average of decision of each tree is noted.
