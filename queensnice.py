import random

def print_board(state):
    for row in state:
        print(",".join(str(cell) for cell in row))

def get_heuristic(state):
    h = 0
    for i in range(len(state)):
        # Check for queens in the same row
        if state[i].count(1) > 1:
            h += state[i].count(1) - 1

        # Check for queens in the same diagonal
        for j in range(len(state)):
            if state[i][j] == 1:
                # Check diagonally upwards
                for k in range(1, len(state)):
                    if i - k >= 0 and j - k >= 0 and state[i - k][j - k] == 1:
                        h += 1
                    if i - k >= 0 and j + k < len(state) and state[i - k][j + k] == 1:
                        h += 1

                # Check diagonally downwards
                for k in range(1, len(state)):
                    if i + k < len(state) and j - k >= 0 and state[i + k][j - k] == 1:
                        h += 1
                    if i + k < len(state) and j + k < len(state) and state[i + k][j + k] == 1:
                        h += 1
    return h

def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[j][i] == 1:
                for k in range(len(state)):
                    if j != k:
                        new_neighbor = [row[:] for row in state]
                        new_neighbor[j][i] = 0
                        new_neighbor[k][i] = 1
                        neighbors.append(new_neighbor)
    return neighbors

def hill_climbing():
    current_state = [[0] * 8 for _ in range(8)]
    for i in range(8):
        current_state[random.randint(0, 7)][i] = 1

    restarts = 0
    state_changes = 0
    while True:
        current_heuristic = get_heuristic(current_state)
        print(f"Current heuristic: {current_heuristic}")
        print("Current State")
        print_board(current_state)
        if current_heuristic == 0:
            break

        neighbors = get_neighbors(current_state)
        next_state = current_state
        next_state = None
        min_heuristic = current_heuristic
        next_heuristic = current_heuristic

        for neighbor in neighbors:
            heuristic_val = get_heuristic(neighbor)
            if heuristic_val < min_heuristic:
                min_heuristic = heuristic_val
                next_state = neighbor

        if next_state == current_state:
            # Restart
            print("RESTART")
            current_state = [[0] * 8 for _ in range(8)]
            for i in range(8):
                current_state[random.randint(0, 7)][i] = 1
            restarts += 1
        else:
            """print(f"Neighbors found with lower h: {current_heuristic - next_heuristic}")"""
            print("-------------------------------")
            print("Setting new current state")
            current_state = next_state
            state_changes += 1

    print("Solution Found!")
    print(f"State changes: {state_changes}")
    print(f"Restarts: {restarts}")

hill_climbing()
