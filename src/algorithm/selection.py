from utils import *

def select_parent(fitness, population, threshold, population_size):
  acum = 0
  for i in range(population_size):
    acum += fitness[i][2]
    if acum >= threshold:
      return population[fitness[i][0].astype(int)]

def selection(fitness, population, population_size):
  parents = np.zeros((2, population.shape[1], population.shape[2]), dtype=int)

  parents[0] = select_parent(fitness, population, random.random_sample(), population_size)

  while np.array_equal(parents[0], parents[1]):
    parents[1] = select_parent(fitness, population, random.random_sample(), population_size)

  return parents