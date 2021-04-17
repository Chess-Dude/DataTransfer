# This Document generates 1000 numbers!
# For the random generated numbers to 1000, simply change line 15's 10,000 to 1000

# Importing the Random Module
import random

# Creating an empty list to fill with numbers
numbers = []


# For loop randomizing 1000 numbers
for i in range(1000):

    # Randomization
    temp = str(random.randint(1, 1000))
    numbers.append(temp)

# Printing the List Full of Numbers
print(numbers)