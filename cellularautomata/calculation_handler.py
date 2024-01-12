import numpy as np
import matplotlib.pyplot as plt


def set_board(size: int):
    board = np.zeros(size, dtype=int)
    board[len(board)//2] = 1
    return board


def set_rule(rule_num: int) -> list:
    binary_representation = format(rule_num, '08b')
    result = [int(bit) for bit in binary_representation]
    result.reverse()
    return result


def apply_rule(rule_board, left, state, right):
    binary_value = int(f"{left}{state}{right}", 2)
    return rule_board[binary_value]


def evolve(rule_board, initial_state, steps: int):
    left_corner = 1
    right_corner = len(initial_state) - 1
    state = initial_state.copy()
    history = [state.copy()]
    for _ in range(steps):
        new_state = np.zeros_like(state)
        for i in range(left_corner, right_corner):
            print(rule_board)
            new_state[i] = apply_rule(rule_board, state[i-1], state[i], state[i+1])
        state = new_state.copy()
        history.append(state.copy())
    return history


def plot_evolution(history, size, steps):
    plt.figure(figsize=(size//10, steps//10))
    plt.imshow(np.array(history), cmap="binary", interpolation="nearest")
    plt.xlabel("Time Step")
    plt.ylabel("Cell")
    plt.title("Rule 30 Cellular Automaton Evolution")
    plt.show()
