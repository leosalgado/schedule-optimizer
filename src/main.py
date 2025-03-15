from utils import *
from algorithm import *
import json

np.set_printoptions(suppress=True)

classes: int = 6
days: int = 5
population_size: int = 50

with open("../data/subjects.json", "r", encoding="utf-8") as f:
    data = json.load(f)

subjects = data["subjects"]
workload = data["workload"]
score_mapping = data["score_mapping"]

if __name__ == '__main__':

  population = initial_population(population_size, days, classes)
  new_population = np.zeros((population_size, days, classes), dtype=int)

  for i in range(1000):
    print('GERACAO: ', i)
    fitness = population_fitness(population, workload, score_mapping, population_size, days, classes)

    print_scores(fitness)

    if(fitness[0][1] < 1):
      break

    j = 2
    elitism(j, population, fitness, new_population)

    while(j < population_size):
      parents = selection(fitness, population, population_size)
      children = crossover(parents, days)
      mutate(children, days, classes)
      new_population[j] = children[0]
      new_population[j+1] = children[1]
      j += 2
    
    population = new_population.copy()
    new_population.fill(0)

  print_solution(population, subjects, fitness)