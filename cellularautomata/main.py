from calculation_handler import set_board, set_rule, apply_rule, evolve, plot_evolution
import numpy as np
import argparse


def start_cellular_automata(board_size, rule, steps):
    board = set_board(board_size)
    rule_board = set_rule(rule)
    evolution_history = evolve(rule_board, board, steps)
    plot_evolution(np.array(evolution_history), len(board), steps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cellular Automata Simulation")
    parser.add_argument("board_size", type=int, help="Size of the board.")
    parser.add_argument("rule", type=int, help="Rule number for cellular automata.")
    parser.add_argument("num_of_steps", type=int, help="Number of simulation steps.")

    args = parser.parse_args()
    start_cellular_automata(args.board_size, args.rule, args.num_of_steps)
