import numpy as np
import pandas as pd
import math
import random


M = int(input("Enter Number of Chromosomes you want"))
N = int(input("Enter Number of Genes"))


population = np.random.randint(2,size=(M,N))
print(population)

#Defining a Fitness Function
def fitness_function(X):
    return (sum(X))

fitness_values=np.ndarray(shape=(M,1))
fitness_values.shape

for i in range(M):
    fitness_value=fitness_function(population[i])
    fitness_values[i]=fitness_value    

np.hstack((population,fitness_values))


#Roulette Wheel implementation
normalized_fitness_values= fitness_values/sum(fitness_values)

sorted_fitness_values= sorted(normalized_fitness_values,reverse=True)
sorted_fitness_values

#Calculating Cumulative Sum
cum_sum=np.cumsum(sorted_fitness_values)

cum_sum=sorted(cum_sum,reverse=True)

r= random.uniform(0,1) #Generate Random number

#Selecting Parent1 and Parent2
for i in range(M):     #N is the no of Genes):
    if r>cum_sum[i]:
        idx=i-1
        break
        
print(cum_sum[idx])        
print(idx)

R= random.uniform(0,1) #Generate Random number
R


#Selecting Parent1 and Parent2
for i in range(M):
    if R>cum_sum[i]:
        idx2=i-1
        break
print(cum_sum[idx2])
print(idx2)

#Single PointCrossOver
parent1=population[idx, :]
parent2=population[idx2, :]
print(parent1,parent2)
pt1 = random.randint(1,len(parent1)-1) 

print(pt1)
#print(parent1[ : pt1])
#print(parent2[pt1:])

child1= np.concatenate((parent1[ :pt1],parent2[pt1:]),axis=0)
child2= np.concatenate((parent1[pt1:],parent2[: pt1]))
print(child1,child2)


#Double Point Crossover
pt1 = random.randint(1,len(parent1)-1)
#pt2 = pt1
pt2= random.randint(1,len(parent1)-1)
 
if pt2>pt1:
    temp =pt1
    pt1=pt2
    pt2=temp

child1 = np.concatenate((parent1[ :pt1],parent2[pt1:pt2],parent1[pt2:]),axis=0)
child1 = np.concatenate((parent2[ :pt1],parent1[pt1:pt2],parent2[pt2:]),axis=0)

#print(child1,child2)

#probability of crossover
Pc=0.5
R1=random.uniform(0,1)
if R1<=Pc:
   child1=child1
else:
   child1=parent1


R2=random.uniform(0,1)
if R2<=Pc:
   child2=child2
else:
   child2 = parent2

#Mutation
pm=0.7
mutationpt=random.randint(0,N) 
R3=random.uniform(0,1)
if R3>=pm:
    child1[mutationpt]=(child1[mutationpt] + 1)%2;
    print('Mutation Occurred')
    print(child1)

