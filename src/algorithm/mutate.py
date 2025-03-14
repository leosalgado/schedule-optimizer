from utils import *

def mutate(children, days, classes):
  for i in range(days):
    for j in range(classes):
      mutation_probability = random.random_sample()
      if(mutation_probability < 0.1):
        mutation = random.randint(1,13)
        while True:
          if children[0][i][j] != mutation:
            children[0][i][j] = mutation
            break
          else:
            mutation = random.randint(1,13)

  for i in range(days):
    for j in range(classes):
      mutation_probability = random.random_sample()
      if(mutation_probability < 0.1):
        mutation = random.randint(1,13)
        while True:
          if children[1][i][j] != mutation:
            children[1][i][j] = mutation
            break
          else:
            mutation = random.randint(1,13)