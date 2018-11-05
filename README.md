# Random Forest

Ensemble Learning: Take multiple algorithms or an algo multiple times to make a more powerful model

### Steps:
1) Pick at random K data points from the training set
2) Build the DT associated to these K data points
3) Choose the number Ntree of tree you want to build and repeat steps 1 & 2
4) For a new data point, make each one of your Ntree trees predict the value of Y to for the data point in question, and assign the new data point the average across all of the predicted Y values

Random Forest is a team of Decision Trees.
#### Note: The number of steps does not depend on the number of tress. The average of decision of each tree is noted.

# Evaluation Regression Models

## R-Squared

SS<sub>res</sub> = SUM (y<sub>i</sub> - y<sub>pred<sub>i</sub></sub>)<sup>2</sup>
SS<sub>tot</sub> = SUM (y<sub>i</sub> - y<sub>avg<sub>i</sub></sub>)<sup>2</sup>

R<sup>2</sup> = 1 - (SS<sub>res</sub>/SS<sub>tot</sub>)

It tells how good is our best fit line compared to average line
Ideal: R<sup>2</sup> = 1
R<sup>2</sup> can be negative when SS<sub>res</sub> fits daughter worse than the average line. It means model is completely broken

## Adjusted R-Squared

Whenever a third variable or more variable is added to the regression model, SS<sub>res</sub> keeps minimizing and R<sup>2</sup> will never decrease, even if the third variable does not affect the prediction or negatively affect the prediction as there is always a co-relation between data. So problem is we can add variable and we will not know if it helped our model or not.

Adjusted R<sup>2</sup> = 1 - (1 - R<sup>2</sup>)((n-1)/(n-p-1))

 p = number of regressors
 n = sample size

 Adjusted R<sup>2</sup> has a penalizing factor, it penalizes for adding a factor that dont help the model 
