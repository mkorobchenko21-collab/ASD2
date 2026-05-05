from typing import Callable
from main import gen_arr


class SortAlgorithm:
    def __init__(self, name: str, func: Callable[[list[int]], int]):
        self.name = name
        self.func = func

    def run_sort(self, array: list):
        arrcp = array.copy()
        operations = self.func(arrcp)
        return operations


class SortResult:
    def __init__(self, size: int, data_type: str, algorithm: str, operations: int):
        self.size = size
        self.data_type = data_type
        self.algorithm = algorithm
        self.operations = operations


class SortExperiment:
    def __init__(
        self, algorithms: list[SortAlgorithm], data_types: list[str], sizes: list[int]
    ):
        self.algorithms = algorithms
        self.data_types = data_types
        self.sizes = sizes
        self.results = []

    def run(self):
        for size in self.sizes:
            for data_type in self.data_types:
                base_array = gen_arr(size, data_type)

                for algo in self.algorithms:
                    operations = algo.run_sort(base_array)

                    self.results.append(
                        SortResult(
                            size=size,
                            algorithm=algo.name,
                            data_type=data_type,
                            operations=operations,
                        )
                    )
