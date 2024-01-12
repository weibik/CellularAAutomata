from calculation_handler import set_board, set_rule, apply_rule, evolve, plot_evolution
import numpy as np

if __name__ == "__main__":
    board = set_board(101)
    rule_board = set_rule(30)
    steps = 50
    evolution_history = evolve(rule_board, board, steps)
    plot_evolution(np.array(evolution_history), len(board), steps)
