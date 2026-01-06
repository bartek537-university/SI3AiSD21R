import math
import random
from typing import Callable

Position = list[float]
FitnessFunction = Callable[[Position], float]


def clamp_position(position: Position, domain: tuple[Position, Position]) -> None:
    for c, component in enumerate(position):
        position[c] = max(min(component, domain[1][c]), domain[0][c])


def levy_flight(b: float, y: float, d: float) -> float:
    root = math.sqrt(y / (2 * math.pi))
    nominator = math.exp(-y / (2 * (b - d)))
    denominator = math.pow(b - d, 3 / 2)

    return root * nominator / denominator


def create_nest(position: Position, b: float, y: float, d: float) -> Position:
    result = position[:]
    for i in range(len(result)):
        result[i] += random.uniform(0, 1) * levy_flight(b, y, d)
    return result


def cuckoo_search(population_size: int, iteration_count: int, b: float, y: float, d: float, pa: float,
                  profit_function: FitnessFunction, domain: tuple[Position, Position]) -> tuple[Position, float]:
    cuckoo_population = list[Position]()
    for _ in range(population_size):
        position = [random.uniform(low, high) for low, high in zip(*domain)]
        cuckoo_population.append(position)

    best_nest = min(cuckoo_population, key=profit_function)
    best_fitness = profit_function(best_nest)

    for _ in range(iteration_count):
        for c, current_cuckoo in enumerate(cuckoo_population):
            nest_position = create_nest(current_cuckoo, b, y, d)
            clamp_position(nest_position, domain)

            if profit_function(nest_position) < profit_function(current_cuckoo):
                cuckoo_population[c] = nest_position

        cuckoo_population.sort(key=profit_function)

        if profit_function(cuckoo_population[0]) < best_fitness:
            best_nest = cuckoo_population[0]
            best_fitness = profit_function(best_nest)

        nests_to_abandon = int(pa * population_size)
        for i in range(population_size - nests_to_abandon, population_size):
            position = [random.uniform(low, high) for low, high in zip(*domain)]
            cuckoo_population[i] = position

    return best_nest, best_fitness


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
    # ([-0.0036082754826016507, 0.01566219610835553], 0.00025832403889493126)
    print(cuckoo_search(20, 50, 1.5, 1, 1, 0.6, sphere, ([-10, -10], [10, 10])))

    # ([0.049192125301218304, 0.0011102478746099625], 0.47653605691719036)
    print(cuckoo_search(20, 50, 2.5, 1, 2, 0.6, rastrigin, ([-10, -10], [10, 10])))

    # ([0.8603898473931956, 0.7386667992014623], 0.019748241118999088)
    print(cuckoo_search(20, 50, 10, 0.5, 4, 0.6, rosenbrock, ([-10, -10], [10, 10])))
