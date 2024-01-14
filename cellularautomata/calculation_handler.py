import numpy as np
import matplotlib.pyplot as plt


def set_board(size: int) -> np.ndarray:
    """Set 2d board of length size."""

    board = np.zeros(size, dtype=int)
    board[len(board) // 2] = 1
    return board


def set_rule(rule_num: int) -> list:
    """Set board with 8 bits based on rule number."""

    binary_representation = format(rule_num, "08b")
    result = [int(bit) for bit in binary_representation]
    result.reverse()
    return result


def apply_rule(
    rule_board: list, left: np.ndarray, state: np.ndarray, right: np.ndarray
) -> list:
    """Apply state of the new cell based on its neighbours."""

    binary_value = int(f"{left}{state}{right}", 2)
    return rule_board[binary_value]


def evolve(rule_board: list, initial_state: np.ndarray, steps: int) -> list:
    """Evolve board 'steps' times."""

    left_corner = 1
    right_corner = len(initial_state) - 1
    state = initial_state.copy()
    history = [state.copy()]
    for _ in range(steps):
        new_state = np.zeros_like(state)
        for i in range(left_corner, right_corner):
            new_state[i] = apply_rule(rule_board, state[i - 1], state[i], state[i + 1])
        new_state[0] = apply_rule(rule_board, state[-1], state[0], state[1])
        new_state[-1] = apply_rule(rule_board, state[-2], state[-1], state[0])
        state = new_state.copy()
        history.append(state.copy())
    return history


def plot_evolution(history, size, steps):
    """Plot the evolution image."""

    plt.figure(figsize=(size // 10, steps // 10))
    plt.imshow(np.array(history), cmap="binary", interpolation="none", aspect="auto")
    plt.xlabel("Time Step")
    plt.ylabel("Cell")
    plt.title("Cellular Automaton Evolution")
    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()
