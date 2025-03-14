from utils import *

def initial_population(population_size, days, classes):
  population = random.randint(low=1, high=13, size=(population_size, days, classes))
  return population