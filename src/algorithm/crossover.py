from utils import *

def crossover(parents, days):
  children = np.zeros_like(parents)
  crossover_probability = random.random_sample()

  if(crossover_probability < 0.8):
    cut = random.randint(1, days)
    children[0][:cut] = parents[0][:cut]
    children[0][cut:] = parents[1][cut:]
    children[1][cut:] = parents[0][cut:]
    children[1][:cut] = parents[1][:cut]
  else:
    children[0] = parents[0]
    children[1] = parents[1]
  return children