import math
import random
from typing import Callable

Gene = float
Chromosome = list[Gene]
CostFunction = Callable[[Chromosome], float]


def clamp_position(chromosome: Chromosome, domain: tuple[Chromosome, Chromosome]) -> None:
    for c, component in enumerate(chromosome):
        chromosome[c] = max(min(component, domain[1][c]), domain[0][c])


def tournament_selection(costs: list[float]) -> int:
    indices = [random.randint(0, len(costs) - 1) for _ in range(4)]
    return min(indices, key=lambda index: costs[index])


def arithmetic_crossover(a: Chromosome, b: Chromosome) -> tuple[Chromosome, Chromosome]:
    random_value = random.uniform(0, 1)

    x = [a[i] + random_value * (b[i] - a[i]) for i in range(len(a))]
    y = [b[i] + random_value * (a[i] - b[i]) for i in range(len(b))]

    return x, y


def arithmetic_mutation(chromosome: Chromosome):
    for i in range(len(chromosome)):
        chromosome[i] += random.uniform(-0.5, 0.5)


def genetic_algorithm(population_size: int, iteration_count: int,
                      mutation_probability: float, crossover_probability: float,
                      cost_function: CostFunction, domain: tuple[Chromosome, Chromosome]
                      ) -> tuple[Chromosome, float]:
    population = list[Chromosome]()
    for _ in range(population_size):
        chromosome = [random.uniform(a, b) for a, b in zip(*domain)]
        population.append(chromosome)

    costs = list[float]()
    offspring = list[Chromosome]()

    best_chromosome = population[0]
    lowest_cost = math.inf

    for _ in range(iteration_count):
        costs.clear()
        offspring.clear()

        for chromosome in population:
            cost = cost_function(chromosome)
            costs.append(cost)

            if cost < lowest_cost:
                best_chromosome = chromosome
                lowest_cost = cost

        while len(offspring) < population_size:
            a = population[tournament_selection(costs)]
            b = population[tournament_selection(costs)]

            if random.random() <= crossover_probability:
                a, b = arithmetic_crossover(a, b)

            if random.random() <= mutation_probability:
                arithmetic_mutation(a)
                arithmetic_mutation(b)

            clamp_position(a, domain)
            clamp_position(b, domain)

            offspring.extend((a, b))

        population = offspring[:]

    return best_chromosome, lowest_cost


def sphere(chromosome: Chromosome) -> float:
    return sum(x ** 2 for x in chromosome)


def rastrigin(chromosome: Chromosome) -> float:
    rastrigin_sum = sum(x ** 2 - 10 * math.cos(2 * math.pi * x) for x in chromosome)
    return 10 * len(chromosome) + rastrigin_sum


def rosenbrock(chromosome: Chromosome) -> float:
    rosenbrock_sum = 0
    for i in range(len(chromosome) - 1):
        rosenbrock_sum += 100 * (chromosome[i + 1] - chromosome[i] ** 2) ** 2 + (chromosome[i] - 1) ** 2
    return rosenbrock_sum


if __name__ == "__main__":
    # ([-0.024100310514157144, 0.02378118921189146], 0.001146369927210576)
    print(genetic_algorithm(20, 30, 0.1, 0.9, sphere, ([-10, -10], [10, 10])))

    # ([-0.0076336832180538125, 0.008321319509925878], 0.025293140259201152)
    print(genetic_algorithm(100, 50, 0.035, 0.85, rastrigin, ([-10, -10], [10, 10])))

    # ([1.0399647801675915, 1.0800684427867377], 0.0018098478935037565)
    print(genetic_algorithm(100, 100, 0.025, 0.85, rosenbrock, ([-10, -10], [10, 10])))
