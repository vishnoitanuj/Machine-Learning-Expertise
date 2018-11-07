# Kernel Support Vector Machine

Used when data is not linearly seperable. It is possible to draw a bpundary but not linearly. It helps choose optimal decision boundary/multiple decision boundary.

### A higher dimensional space

![](high.png)  

Similarly, we can have many mapping functions like

![](k1.png) ![](k2.png)

########## Problem here is mapping to a higher dimensional space can be  highly compute-intensive

## The Gaussian RBF kernel

 K (x, l<sup>i</sup>) = e <sup>-(||x -  l<sup>i<sup>||<sup>2</sup>) / (2*sigma<sup>2</sup>)</sup>

 ![](K3.png)