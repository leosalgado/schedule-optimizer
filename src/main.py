from utils.utils import *
import numpy as np
from numpy import random
import json


with open("../data/subjects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

subjects = data["subjects"]
workload = data["workload"]
score_mapping = data["score_mapping"]

np.set_printoptions(suppress=True)

classes: int = 6
days: int = 5
population_size: int = 50

population = np.zeros((population_size, days, classes))
new_population = np.zeros((population_size, days, classes), dtype=int)
fitness = np.zeros((population_size, 3))
parents = np.zeros((2, days, classes))
children = np.zeros((2, days, classes))

# random.seed(1)

def initial_population():
  global population
  population = random.randint(low=1, high=13, size=(population_size, days, classes))

def population_fitness():
  global population, fitness

  for p in range(population_size):

    count = np.zeros(12, dtype=int)
    for d in range(days):
      for c in range(classes):
        count[population[p][d][c] - 1] += 1

    score = 0
    score += sum((count[l] - load) ** 4 for l, load in enumerate(workload.values()))

    for d in range(days):
      for c in range(classes):
        if d in score_mapping:
          if population[p][d][c] in score_mapping[d]:
            score += 20

    fitness[p][0] = p 
    fitness[p][1] = score 
    fitness[p][2] = -1 

  fitness = fitness[fitness[:, 1].argsort()]

  for i, value in enumerate(fitness[:, 1]):
    if sum(fitness[:, 1] > 0) and fitness[i][1] > 0:
      fitness[i][2] = 1 / value / sum(fitness[:, 1]) * 100
    else:
      fitness [i][2] = 0

  minsum = sum(fitness[:, 2])

  for i in range(population_size):
    if minsum > 0:
      fitness[i][2] = fitness[i][2] / minsum
    else:
      fitness[i][2] = 0

def selection():

  random_parent0 = random.random_sample(size=None)
  random_parent1 = random.random_sample(size=None)

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
      random_parent1 = random.random_sample(size=None)

def crossover():
  global fitness_sorted, roulette_selected, children
  crossover_probability = random.random_sample(size=None)

  if(crossover_probability < 0.8):
    cut = random.randint(1, days)
    children[0][:cut] = parents[0][:cut]
    children[0][cut:] = parents[1][cut:]
    children[1][cut:] = parents[0][cut:]
    children[1][:cut] = parents[1][:cut]
  else:
    children[0] = parents[0]
    children[1] = parents[1]

def mutate():
  global children

  for i in range(days):
    for j in range(classes):
      mutation_probability = random.random_sample(size=None)
      if(mutation_probability < 0.1):
        mutation = random.randint(1,13)
        while True:
          if not children[0][i][j] == mutation:
            children[0][i][j] = mutation
            break
          else:
            mutation = random.randint(1,13)

  for i in range(days):
    for j in range(classes):
      mutation_probability = random.random_sample(size=None)
      if(mutation_probability < 0.1):
        mutation = random.randint(1,13)
        while True:
          if not children[1][i][j] == mutation:
            children[1][i][j] = mutation
            break
          else:
            mutation = random.randint(1,13)

def elitism(quantity):
  global new_population
  for i in range (quantity):
    new_population[i] = population[fitness[i][0].astype(int)]



if __name__ == '__main__':

  initial_population()

  for i in range(1000):
    print('GERACAO: ', i)
    population_fitness()

    print_scores(fitness)

    if(fitness[0][1] < 1):
      break

    j = 2
    elitism(j)

    while(j < population_size):
      selection()
      crossover()
      mutate()
      new_population[j] = children[0]
      new_population[j+1] = children[1]
      j += 2
    
    population = new_population.copy()
    new_population = np.zeros((population_size, days, classes), dtype=int)

  print_solution(population, subjects, fitness)