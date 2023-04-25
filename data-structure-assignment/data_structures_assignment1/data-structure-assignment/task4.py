# A program that creates and displays all combinations of letters, selecting eachletter from a different key in a dictionary.
import itertools
# The itertools.product() function generates all possible combinations of letters by selecting one letter from each key in the dictionary.
# Define the input dictionary
myData = {'1': ['A', 'B', 'Z'], '2': ['c', 'd']}

# Create a list of tuples containing all possible combinations of letters
combinations = list(itertools.product(myData['1'], myData['2']))

# Iterate over the list of combinations and print each one
for combination in combinations:
    print(''.join(combination))
