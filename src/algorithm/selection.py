from utils import *

def selection(fitness, population, population_size):
  parents = np.zeros((2, population.shape[1], population.shape[2]), dtype=int)

  random_parent0 = random.random_sample()
  random_parent1 = random.random_sample()

  acum = 0
  for i in range(population_size):
    acum += fitness[i][2]
    if(acum >= random_parent0):
      parents[0] = population[fitness[i][0].astype(int)]
      break

  while True:
    acum = 0
    for i in range(population_size):
      acum += fitness[i][2]
      if acum >= random_parent1: 
        parents[1] = population[fitness[i][0].astype(int)]
        break

    if not np.array_equal(parents[0], parents[1]):
      break
    else:
      random_parent1 = random.random_sample()
  return parents