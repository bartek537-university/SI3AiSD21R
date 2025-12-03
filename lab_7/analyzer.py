import random
import sys
from datetime import datetime

from lab_7.task_1.task_1 import insertion_sort
from lab_7.task_2.task_2 import bubble_sort
from lab_7.task_3.task_3 import quick_sort
from lab_7.task_4.task_4 import heap_sort
from lab_7.task_5.task_5 import merge_sort


def random_dataset(size: int) -> list[float]:
    return [random.random() * 200 - 100 for _ in range(size)]


dataset_sizes = [25, 50, 75, 100,
                 250, 500, 750, 1000,
                 2500, 5000, 7500, 10_000,
                 25_000, 50_000, 75_000, 100_000,
                 250_000, 500_000, 750_000, 1_000_000]
algorithm_functions = [insertion_sort, bubble_sort, quick_sort, heap_sort, merge_sort]

sys.setrecursionlimit(int(10e6))

for dataset_size in dataset_sizes:
    for algorithm_function in algorithm_functions:
        dataset_values = random_dataset(dataset_size)
        algorithm_name = str(algorithm_function.__name__)

        start_time = datetime.now()
        algorithm_function(dataset_values)
        end_time = datetime.now()

        execution_time_seconds = (end_time - start_time).total_seconds()
        print(f"{algorithm_name},{dataset_size},{execution_time_seconds:f}")
