import sys
from pathlib import Path
import quick_sorts


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


def main():
    if len(sys.argv) != 2:
        raise ValueError(
            "Error: Wrong usage of arguments\n  \
        Usage: python3 main.py [path/to/file]\n"
        )

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
        ops_qs_1 = quick_sorts.quick_sort_1(arr1)
        ops_qs_rand = quick_sorts.randomized_quick_sort(arr2)
        ops_qs_3pivot = quick_sorts.quick_sort_3_pivot(arr3)
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


if __name__ == "__main__":
    main()
