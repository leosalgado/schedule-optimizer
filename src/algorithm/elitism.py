from utils import *

def elitism(quantity, population, fitness, new_population):
  for i in range (quantity):
    new_population[i] = population[fitness[i][0].astype(int)]