import sys
from pathlib import Path
import quick_sorts


def load_file(filepath: Path) -> tuple[int, list]:
    if not filepath.is_file():
        raise FileNotFoundError(f"Error: file {filepath} was not found")

    with open(filepath, "r", encoding="utf-8") as file:
        size_array = int(file.readline().strip())

        if size_array <= 0:
            raise ValueError("Error: first line of file must contain only 1 value")

        array = []

        for _ in range(size_array):
            array.append(int(file.readline()))

    return size_array, array


def get_name_output_file(path_in: Path) -> Path:
    if not path_in.suffix:
        return path_in.with_name(f"{path_in.name}_out.txt")
    return path_in.with_name(f"{path_in.stem}_out{path_in.suffix}")


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError(
                "Error: Wrong usage of arguments\n  \
            Usage: python3 main.py [path/to/file]\n"
            )

        path_in = Path(sys.argv[1])
        path_out = get_name_output_file(path_in)

        size, array = load_file(path_in)

        with open(PATH_OUT, "w", encoding="utf-8") as file:
            print(
                f"{operation_count_qs} {operation_count_qs_randomized} {opearion_count_qs_3pivot}\n"
            )
            file.write(f"{target_user_id}\n")

        print(f"\nResults were saved to '{PATH_OUT}'")

    except Exception as e:
        raise SystemExit(f"Error ocurred while running program:\n{e}")


if __name__ == "__main__":
    main()
