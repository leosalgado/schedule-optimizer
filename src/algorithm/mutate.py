from utils import *

def mutate(children, days, classes):
  for child in children:
    for i in range(days):
      for j in range(classes):
        if random.random_sample() < 0.1: # Mutation Probability
          new_value = random.randint(1,13)
          while new_value == child[i][j]:
            new_value = random.randint(1, 13)
          child[i][j] = new_value