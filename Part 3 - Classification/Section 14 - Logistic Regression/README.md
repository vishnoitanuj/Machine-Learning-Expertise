# Logistic Regression

Linear Regression: y = b<sub>0</sub> + b<sub>1</sub>*x
Sigmoid Function: p = 1/(1+e<sup>-y</sup>) 
Logistic Regression: ln(p/(1-p)) = b<sub>0</sub> + b<sub>1</sub>*x

LR is basically used when there is a probabilistic distribution. It usually predicts probabilities. Then we can select a threshold and classify it to be happening or not happening.

#### Confusion Matrix
A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known. The confusion matrix itself is relatively simple to understand, but the related terminology can be confusing.

 Correct_prediction    Incorrect_prediction
 Incorrect_prediction  Correct_prediction

