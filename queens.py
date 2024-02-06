import random

def generate_random_state(n):
    """Generate a random state for the 8-Queens problem."""
    return [random.randint(0, n - 1) for _ in range(n)]

def calculate_heuristic(state):
    """Calculate the heuristic value for a given state."""
    heuristic = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                heuristic += 1
    return heuristic

def generate_neighbors(state):
    """Generate all possible neighbor states."""
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if j != state[i]:
                new_state = list(state)
                new_state[i] = j
                neighbors.append(new_state)
    return neighbors

def hill_climbing_with_random_restart():
    """Solve the 8-Queens problem using Hill-Climbing with random restarts."""
    current_state = generate_random_state(8)
    restarts = 0
    state_changes = 0

    while True:
        current_heuristic = calculate_heuristic(current_state)
        print(f"Current h: {current_heuristic}\nCurrent State")
        print_state(current_state)
        if current_heuristic == 0:
            print("Solution Found!")
            break

        neighbors = generate_neighbors(current_state)
        next_state = None
        next_heuristic = current_heuristic

        for neighbor in neighbors:
            heuristic = calculate_heuristic(neighbor)
            if heuristic < next_heuristic:
                next_state = neighbor
                next_heuristic = heuristic

        if next_state is None:
            print("RESTART")
            current_state = generate_random_state(8)
            restarts += 1
        else:
            print(f"Neighbors found with lower h: {current_heuristic - next_heuristic}")
            print("-------------------------------")
            print("Setting new current state")
            current_state = next_state
            state_changes += 1

    print(f"State changes: {state_changes}")
    print(f"Restarts: {restarts}")

def print_state(state):
    """Print the current state of the board."""
    n = len(state)
    for row in range(n):
        print(','.join(['1' if state[col] == row else '0' for col in range(n)]))

hill_climbing_with_random_restart()
