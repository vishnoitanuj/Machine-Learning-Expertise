# Kernel Support Vector Machine

Used when data is not linearly seperable. It is possible to draw a bpundary but not linearly. It helps choose optimal decision boundary/multiple decision boundary.


#### Note: Other type of kernels used when the data is not linearly seperable.

### A higher dimensional space

![](high.png)  

Similarly, we can have many mapping functions like

![](k1.png) ![](k2.png)

########## Problem here is mapping to a higher dimensional space can be  highly compute-intensive

## The Gaussian RBF kernel


 K (x, l<sup>i</sup>) = e <sup>-(||x -  l<sup>i<sup>||<sup>2</sup>) / (2*sigma<sup>2</sup>)</sup>

 ![](K3.png)
 ![](k4.png)

 Sigma defines how wide is the circle.
 It appears to happen in higher dimensional space but mathematically(computationally) it just calculating through formulae. If the K less than 0 it appears one region and other will have another value.

 ![](k5.png)

 ### Other types of kernels are:
 Sigmoid Kernel
 Polynomial Kernel


