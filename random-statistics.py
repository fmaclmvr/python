import random
A = [1,4,6,9,13]

# Draw 1 sample from list A 
print(random.choice(A))
# Draw a sample of size 3 from list A without replacement 
print(random.sample(A,3))
# Randomly take one permutation of list A
# Note that the shuffle function return void, and the list A has been shuffled
print(random.shuffle(A))
print(A)
# Get a random number from interval [0,1]
print(random.random())
# Another way to get the same result
print(random.uniform(0.0,1.0))
# Get a random number from a normal distribution N(mean,stdev)
print(random.normalvariate(30,4))

print("--------------------------")

# Note: when importing statistics, use "python3" to execute 
import statistics as stat
B = [1,2,3,4,5,6,7,8,9,10]

# Compute the mean of list B
print(stat.mean(B))
# Compute the median of list B
print(stat.median(B))
# Compute the standard deviation of list B
print(stat.stdev(B))

