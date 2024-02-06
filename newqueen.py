import random

def print_board(state):
    for row in state:
        print(" ".join(str(cell) for cell in row))
    print()  # Extra newline for clarity

def get_h(state):
    h = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 1:
                # Check row and column conflicts
                for k in range(len(state)):
                    if state[i][k] == 1 and k != j:
                        h += 1
                    if state[k][j] == 1 and k != i:
                        h += 1
                # Check diagonal conflicts
                for k in range(1, len(state)):
                    if i + k < len(state) and j + k < len(state) and state[i + k][j + k] == 1:
                        h += 1
                    if i + k < len(state) and j - k >= 0 and state[i + k][j - k] == 1:
                        h += 1
                    if i - k >= 0 and j + k < len(state) and state[i - k][j + k] == 1:
                        h += 1
                    if i - k >= 0 and j - k >= 0 and state[i - k][j - k] == 1:
                        h += 1
    return h // 2  # Each pair of queens conflict is counted twice

def get_neighbors(state):
    neighbors = []
    for col in range(len(state)):
        for row in range(len(state)):
            if state[row][col] == 1:
                for new_row in range(len(state)):
                    if new_row != row:
                        new_state = [r[:] for r in state]
                        new_state[row][col] = 0
                        new_state[new_row][col] = 1
                        neighbors.append(new_state)
    return neighbors

def hill_climbing():
    current_state = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        row = random.randint(0, 7)
        current_state[row][i] = 1

    restarts = 0
    state_changes = 0
    while True:
        current_h = get_h(current_state)
        print("-------------------------------")
        print(f"Current hueristic: {current_h}")
        print("Current State:")
        print_board(current_state)

        if current_h == 0:
            break

        neighbors = get_neighbors(current_state)
        next_state = min(neighbors, key=get_h)
        next_h = get_h(next_state)
        lower_h_neighbors = sum(1 for neighbor in neighbors if get_h(neighbor) < current_h)

        print(f"Neighbors found with lower hueristic: {lower_h_neighbors}")

        if next_h >= current_h:
            print("RESTART")
            current_state = [[0 for _ in range(8)] for _ in range(8)]
            for i in range(8):
                current_state[random.randint(0, 7)][i] = 1
            restarts += 1
        else:
            current_state = next_state
            state_changes += 1
            print("Setting new current state")

    print("-------------------------------")
    print("Solution Found!")
    print_board(current_state)
    print(f"State changes: {state_changes}")
    print(f"Restarts: {restarts}")

hill_climbing()
