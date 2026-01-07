import math
import random
from typing import Callable

Position = list[float]
CostFunction = Callable[[Position], float]


def clamp_position(position: Position, domain: tuple[Position, Position]) -> None:
    for c, component in enumerate(position):
        position[c] = max(min(component, domain[1][c]), domain[0][c])


def mutate(i: int, population: list[Position], mutation_control: float) -> Position:
    random_indices: list[int] = random.sample(range(len(population)), 4)

    if i in random_indices:
        random_indices.remove(i)
    else:
        random_indices = random_indices[:-1]

    r1, r2, r3 = random_indices
    result = population[r1][:]

    for i in range(len(result)):
        result[i] += mutation_control * (population[r2][i] - population[r3][i])

    return result


def crossover(base_position: Position, mutated_position: Position, crossover_probability: float) -> Position:
    result = base_position[:]

    copied_index = random.randrange(len(result))
    for j in range(len(result)):
        if random.random() <= crossover_probability or j == copied_index:
            result[j] = mutated_position[j]

    return result


def differential_evolution(population_size: int, iteration_count: int,
                           mutation_control: float, crossover_probability: float,
                           cost_function: CostFunction, domain: tuple[Position, Position]
                           ) -> tuple[Position, float]:
    current_population = list[Position]()
    for _ in range(population_size):
        position = [random.uniform(a, b) for a, b in zip(*domain)]
        current_population.append(position)

    new_population = list[Position]([[]] * population_size)

    for _ in range(iteration_count):
        for i, current_position in enumerate(current_population):
            mutated_position = mutate(i, current_population, mutation_control)
            crossover_position = crossover(current_position, mutated_position, crossover_probability)

            clamp_position(crossover_position, domain)

            if cost_function(crossover_position) < cost_function(current_position):
                new_population[i] = crossover_position
            else:
                new_population[i] = current_position

        current_population = new_population[:]

    best_position = min(current_population, key=cost_function)
    lowest_cost = cost_function(best_position)

    return best_position, lowest_cost


def sphere(position: Position) -> float:
    return sum(x ** 2 for x in position)


def rastrigin(chromosome: Position) -> float:
    rastrigin_sum = sum(x ** 2 - 10 * math.cos(2 * math.pi * x) for x in chromosome)
    return 10 * len(chromosome) + rastrigin_sum


def rosenbrock(position: Position) -> float:
    rosenbrock_sum = 0
    for i in range(len(position) - 1):
        rosenbrock_sum += 100 * (position[i + 1] - position[i] ** 2) ** 2 + (position[i] - 1) ** 2
    return rosenbrock_sum


if __name__ == "__main__":
    # ([3.3897400084988106e-05, -5.8718528898799674e-06], 2.3479949362581465e-07)
    print(differential_evolution(20, 50, 0.4, 0.1, rastrigin, ([-10, -10], [10, 10])))

    # ([0.0013159086447297082, -0.0015128941759976408], 0.0007976229677737479)
    print(differential_evolution(30, 75, 0.7, 0.85, rastrigin, ([-10, -10], [10, 10])))

    # ([1.1008489140771138, 1.2125848246572821], 0.010221839697098261)
    print(differential_evolution(20, 60, 0.5, 0.95, rosenbrock, ([-10, -10], [10, 10])))
