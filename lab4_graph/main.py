import random


def is_safe(v, graph, path, pos):
    """
    Check if the vertex v can be added at index 'pos' in the Hamiltonian Cycle.
    """
    # Check if this vertex is an adjacent vertex of the previously added vertex
    if graph[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included in the path
    for i in range(pos):
        if path[i] == v:
            return False

    return True


def ham_cycle_util(graph, path, pos, V):
    """
    A recursive utility function to solve the Hamiltonian cycle problem.
    """
    # Base case: If all vertices are included in the path
    if pos == V:
        # And if there is an edge from the last included vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as a next candidate in Hamiltonian Cycle
    for v in range(1, V):
        if is_safe(v, graph, path, pos):
            path[pos] = v

            # Recursive call
            if ham_cycle_util(graph, path, pos + 1, V):
                return True

            # If adding vertex v doesn't lead to a solution, backtrack
            path[pos] = -1

    return False


def hamiltonian_cycle(graph, V):
    """
    Solves the Hamiltonian Cycle problem using Backtracking.
    """
    # Initialize path array and set the first vertex as 0
    path = [-1] * V
    path[0] = 0

    # Attempt to find a cycle
    if not ham_cycle_util(graph, path, 1, V):
        print("Hamiltonian cycle does not exist.")
        return False

    # Print the resulting cycle
    print("Hamiltonian cycle exists:", " -> ".join(map(str, path + [path[0]])))
    return True


def print_graph(graph):
    """
    Utility function to print the adjacency matrix.
    """
    print("\nGraph Adjacency Matrix:")
    for row in graph:
        print(" ".join(map(str, row)))
    print()


def generate_random_graph(V):
    """
    Generates a random undirected graph represented as an adjacency matrix.
    """
    graph = [[0] * V for _ in range(V)]
    for i in range(V):
        for j in range(i + 1, V):
            edge = random.randint(0, 1)
            graph[i][j] = edge
            graph[j][i] = edge
    return graph


def main():
    print("--- Hamiltonian Cycle Construction ---")

    # Get graph size
    try:
        V_input = input("Enter the number of vertices: ").strip()
        if not V_input:
            print("Input cannot be empty.")
            return
        V = int(V_input)
        if V <= 0:
            print("The number of vertices must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Choose input method
    print("\nChoose input method:")
    print("1. Generate random graph")
    print("2. Enter adjacency matrix manually")
    choice = input("Your choice (1 or 2): ").strip()

    if choice == "1":
        graph = generate_random_graph(V)
    elif choice == "2":
        print(f"\nEnter the adjacency matrix ({V}x{V}) row by row.")
        print("Enter elements separated by spaces (e.g., '0 1 0'):")
        graph = []
        for i in range(V):
            while True:
                try:
                    row_data = input(f"Row {i}: ").split()
                    if len(row_data) != V:
                        print(f"Error: Expected {V} elements, but got {len(row_data)}. Try again.")
                        continue
                    row = list(map(int, row_data))
                    graph.append(row)
                    break
                except ValueError:
                    print("Error: Invalid characters found. Use only 0 and 1.")
    else:
        print("Invalid choice.")
        return

    # Show matrix and run algorithm
    print_graph(graph)
    hamiltonian_cycle(graph, V)


if __name__ == "__main__":
    main()
