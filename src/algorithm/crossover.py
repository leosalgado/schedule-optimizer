from utils import *

def crossover(parents, days):
  children = parents.copy()

  if random.random_sample() < 0.8: # Crossover probability
    cut = random.randint(1, days)
    children[0][:cut], children[1][:cut] = parents[0][:cut], parents[1][:cut]
    children[0][cut:], children[1][cut:] = parents[1][cut:], parents[0][cut:]

  return children