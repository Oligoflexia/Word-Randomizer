# Word Randomizer
#
# 1.0
# Souvik Maiti
# smaiti@alumni.ubc.ca
# Oct 20, 2021
#
# I didn't wan't to study a bunch of words in lexicographical order so I decided to code a quick script to randomize
# them, and remember where I left off.


# Import dependencies
import pandas as pd
import random
import pickle
from collections import deque

# Import the list of words
# Words should be in a CSV file format in the Data folder. Change the name below to whatever you called it!
df = pd.read_csv('Data/Words.csv')

# Load the queue of randomized words and if not present, create one.
try:
    queue = pickle.load(open("Data/rand_queue.pickle", "rb"))
except (OSError, IOError) as e:
    word_count = len(df.index)
    queue = deque([i for i in range(0, word_count)])
    pickle.dump(queue, open("Data/rand_queue.pickle", "wb"))

# Load the queue of reviewed words and if not present, create it.
try:
    used = pickle.load(open("Data/used_queue.pickle", "rb"))
except (OSError, IOError) as e:
    used = deque([])
    pickle.dump(used, open("Data/used_queue.pickle", "wb"))

# Initialize empty list to keep track of each round of review
indices = []

## Functions
# Pops the required number of indecies off the randomized queue
def popper(number):
    for x in range(number):
        popped = queue.popleft()
        picker(popped, df)
        used.append(popped)
    printer(indices)

# Appends the indices together to make a nice list
def picker(number, df):
    indices.append(number)

# Prints a nice table of the subset of the larger words CSV
def printer(list):
    df1 = df.iloc[list]
    print(df1.to_markdown())

## Main Script
number = int(input("How many words would you like to review today?"))
random.shuffle(queue)
popper(number)
print('You have: ' + str(len(queue)) + ' words remaining in the queue!')
pickle.dump(used, open("Data/used_queue.pickle", "wb"))
pickle.dump(queue, open("Data/rand_queue.pickle", "wb"))