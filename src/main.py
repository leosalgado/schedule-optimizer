from utils import *
from algorithm import *
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

new_population = np.zeros((population_size, days, classes), dtype=int)

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

  population = initial_population(population_size, days, classes)

  for i in range(1000):
    print('GERACAO: ', i)
    fitness = population_fitness(population, workload, score_mapping, population_size, days, classes)

    print_scores(fitness)

    if(fitness[0][1] < 1):
      break

    j = 2
    elitism(j)

    while(j < population_size):
      parents = selection(fitness, population, population_size)
      children = crossover(parents, days)
      mutate()
      new_population[j] = children[0]
      new_population[j+1] = children[1]
      j += 2
    
    population = new_population.copy()
    new_population = np.zeros((population_size, days, classes), dtype=int)

  print_solution(population, subjects, fitness)