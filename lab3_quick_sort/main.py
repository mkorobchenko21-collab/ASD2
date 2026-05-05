import sys
from pathlib import Path
import random

from quick_sorts import quick_sort_1, randomized_quick_sort, quick_sort_3_pivot
from plotData import plot_sort_results

sys.setrecursionlimit(10**5)


def load_file(filepath: Path) -> tuple[int, list]:
    if not filepath.is_file():
        raise FileNotFoundError(f"Error: file {filepath} was not found")

    with open(filepath, "r", encoding="utf-8") as file:
        size_array = int(file.readline().strip())

        if size_array <= 0:
            raise ValueError("Error: size of array must be a positive integer")

        array = []

        for _ in range(size_array):
            array.append(int(file.readline()))

    return size_array, array


def get_name_output_file(path_in: Path) -> Path:
    if not path_in.suffix:
        return path_in.with_name(f"{path_in.name}_out.txt")
    return path_in.with_name(f"{path_in.stem}_out{path_in.suffix}")


def run_benchmark():
    sizes = [10] + list(range(100, 1001, 100)) + list(range(1000, 5001, 250))
    data_types = ["Random", "Sorted", "Reversed"]

    formatted_data = {
        dt: {"QuickSort 1": {}, "Randomized QS": {}, "3-Pivot QS": {}}
        for dt in data_types
    }

    print(
        "Starting benchmark for QuickSort algorithms on various data types and sizes...\n"
    )

    for d_type in data_types:
        for size in sizes:
            print(f"Обробка: {d_type} масив, розмір {size}...")

            if d_type == "Random":
                original_arr = [random.randint(0, size * 10) for _ in range(size)]
            elif d_type == "Sorted":
                original_arr = list(range(size))
            else:  # Reversed
                original_arr = list(range(size, 0, -1))

            arr1 = original_arr.copy()
            ops1 = quick_sort_1(arr1)
            formatted_data[d_type]["QuickSort 1"][size] = ops1

            arr2 = original_arr.copy()
            ops2 = randomized_quick_sort(arr2)
            formatted_data[d_type]["Randomized QS"][size] = ops2

            arr3 = original_arr.copy()
            ops3 = quick_sort_3_pivot(arr3)
            formatted_data[d_type]["3-Pivot QS"][size] = ops3

    print("\nТестування завершено! Будуємо графіки...")

    print_beautiful_output(formatted_data)
    plot_sort_results(formatted_data, logarithmic=True)


def print_beautiful_output(formatted_data: dict) -> None:
    data_types = list(formatted_data.keys())
    algos = list(formatted_data[data_types[0]].keys())
    sizes = sorted(list(formatted_data[data_types[0]][algos[0]].keys()))

    print("\n" + "=" * 50)
    print("ДЕТАЛЬНІ РЕЗУЛЬТАТИ ТЕСТУВАННЯ")
    print("=" * 50 + "\n")

    for size in sizes:
        print(f"Size: {size}")
        for algo in algos:
            print(f"\t{algo}:")
            for d_type in data_types:
                ops = formatted_data[d_type][algo][size]

                type_str = f"Type: {d_type.lower()}"

                print(f"\t\t{type_str:<25} {ops:>10}")
        print()


def main():
    if len(sys.argv) == 2:
        path_in = Path(sys.argv[1])
        path_out = get_name_output_file(path_in)

        # reading the input file
        try:
            size, original_array = load_file(path_in)
        except Exception as e:
            sys.exit(f"Error ocurred while loading file\n{e}")

        # copying arrays
        arr1 = original_array.copy()
        arr2 = original_array.copy()
        arr3 = original_array.copy()

        # sorting
        try:
            ops_qs_1 = quick_sort_1(arr1)
            ops_qs_rand = randomized_quick_sort(arr2)
            ops_qs_3pivot = quick_sort_3_pivot(arr3)
        except Exception as e:
            sys.exit(f"Error ocurred while sorting\n{e}")

        # writing results to output file
        try:
            with open(path_out, "w", encoding="utf-8") as file:
                # Записуємо результати в один рядок через пробіл (як вимагалося у лабі)
                file.write(f"{ops_qs_1} {ops_qs_rand} {ops_qs_3pivot}\n")

            print(f"\nResults were saved to '{path_out}'")
        except Exception as e:
            sys.exit(f"Error ocurred while running program\n{e}")

    else:
        run_benchmark()


if __name__ == "__main__":
    main()
