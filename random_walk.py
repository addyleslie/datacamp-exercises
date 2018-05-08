# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Initialize all_walks
all_walks = []

# Simulate random walk 10 times
for i in range(1000) :
    
    # Initialize random_walk
    random_walk = [0]
    
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
    
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
    
        # Implement clumsiness
        if np.random.rand(0,1) <= 0.001 :
            step = 0

        # Append step to random_walk
        random_walk.append(step)
        
    all_walks.append(random_walk)

# Print all_walks to verify data
#print(all_walks)

# Convert and transpose all_walks to Numpy array: np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

# Select last row from np_aw_t: ends
ends = np.array(np_aw_t[100,:])

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# Estimate chance that you'll reach 60 steps
over60 = np_aw_t[np_aw_t >= 60]
print(over60.size / np_aw_t.size)