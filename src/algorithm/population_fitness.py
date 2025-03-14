from utils import *

def population_fitness(population, workload, score_mapping, population_size, days, classes):
  fitness = np.zeros((population_size, 3))

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
  return fitness