import sys
from pathlib import Path
from math import inf


def merge_and_count_split_inversions(arr: list, left: list, right: list):
    n1 = len(left)
    n2 = len(right)
    left.append(inf)
    right.append(inf)
    i = 0
    j = 0
    c = 0

    for k in range(n1 + n2):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            c += n1 - i
    return arr, c


def sort_and_count_inversions(arr: list):
    n = len(arr)
    if n == 1:
        return arr, 0
    else:
        left, x = sort_and_count_inversions(arr[: n // 2])
        right, y = sort_and_count_inversions(arr[n // 2 :])
        arr, z = merge_and_count_split_inversions(arr, left, right)
        return arr, x + y + z


def validate_input_file(filepath: Path): ...


def load_movie_data(filepath: Path):
    users_data = {}

    with open(filepath, "r", encoding="utf-8") as file:
        validate_input_file(filepath)

        first_line = file.readline().split()
        if len(first_line) != 2:
            raise SystemExit("Error: first line of file must contain only 2 values")

        user_number, films_number = map(int, first_line)

        for line in file:
            line = line.strip()
            if not line:
                continue

            row_data = list(map(int, line.split()))

            user_id = row_data[0]
            ratings = row_data[1:]

            users_data[user_id] = ratings

        return user_number, films_number, users_data


def get_name_output_file(path_in: Path):
    if not path_in.suffix:
        path_out = path_in.with_name((f"{path_in}_out.txt"))
    else:
        path_out = path_in.with_name(f"{path_in.stem}_out{path_in.suffix}")

    return path_out


def main():
    # TODO: improve errors raising
    if len(sys.argv) != 2:
        raise SystemExit(
            "Error: Wrong usage of arguments\n  \
            Usage: python3 main.py [path/to/file]\n"
        )

    PATH_IN = Path(sys.argv[1])

    if not PATH_IN.is_file():
        raise SystemExit(f"Error: file {PATH_IN} was not found")

    # TODO: finish logic of the program
    try:
        total_users, total_films, data = load_movie_data(PATH_IN)

        target_user_id = int(input("Enter user id for comparison: "))

        if target_user_id not in data:
            raise SystemExit(f"Error: user with id {target_user_id} was not found")

        target_user_rating = data[target_user_id]

        # creating a pattern of target user
        sorted_target_rating = sorted(
            # makes from [2, 5, 4, 1, 3] (indexe is a number of film, and value is films place in a rating)
            # to true rating [3, 0, 4, 2, 1] (indexe is a place in a rating, and value is a number of film)
            range(len(target_user_rating)),
            key=lambda k: target_user_rating[k],
        )

        comparison_results = []

        for user_id, current_rating in data.items():
            if user_id == target_user_id:
                continue

            # addapting current user ratings to target user pattern
            mapped_current_rating = [current_rating[k] for k in sorted_target_rating]

            _, c = sort_and_count_inversions(mapped_current_rating)

            comparison_results.append((user_id, c))

        comparison_results.sort(key=lambda x: x[1])

        print(f"{target_user_id}")
        for res in comparison_results:
            print(f"{res[0]} {res[1]}")

    except Exception as e:
        raise SystemExit(f"Error ocurred while running program:\n{e}")


if __name__ == "__main__":
    main()
