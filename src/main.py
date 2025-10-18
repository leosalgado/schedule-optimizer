import os
import json

from utils import *
from algorithm import *

np.set_printoptions(suppress=True)

classes: int = 6
days: int = 5
population_size: int = 50

base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "..", "data", "subjects.json")

with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

subjects = data["subjects"]
workload = data["workload"]
score_mapping = data["score_mapping"]


def main():
    population = initial_population(population_size, days, classes)
    new_population = np.zeros((population_size, days, classes), dtype=int)

    for i in range(1000):
        print("GERACAO: ", i)
        fitness = population_fitness(
            population, workload, score_mapping, population_size, days, classes
        )

        print_scores(fitness)

        if fitness[0][1] < 1:
            break

        j = 2
        elitism(j, population, fitness, new_population)

        while j < population_size:
            parents = selection(fitness, population, population_size)
            children = crossover(parents, days)
            mutate(children, days, classes)
            new_population[j] = children[0]
            new_population[j + 1] = children[1]
            j += 2

        population = new_population.copy()
        new_population.fill(0)

    print_solution(population, subjects, fitness)


if __name__ == "__main__":
    main()

