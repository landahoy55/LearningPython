#This is an attempted at creating a dice roll simulator
import numpy as np

np.random.seed(2342) #set the seed, to allow for consistency

#print(np.random.rand()) #pseduo random numner!

# Use randint() to simulate a dice
print(np.random.randint(1,7))


#This is the beginning of the dice rolling simulator. If less than two is rolled one step backwards is taken, 3,4,5 is a step forward and a 6 is the business!!

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice < 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)
