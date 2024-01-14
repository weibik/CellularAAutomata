import unittest
import numpy as np
from cellularautomata.calculation_handler import (
    set_board,
    set_rule,
    apply_rule,
    evolve,
    plot_evolution,
)


class TestCellularAutomaton(unittest.TestCase):
    def test_set_board(self):
        size = 10
        board = set_board(size)
        self.assertEqual(len(board), size)
        self.assertEqual(np.sum(board), 1)

    def test_set_rule(self):
        rule_num = 30
        rule_board = set_rule(rule_num)
        self.assertEqual(len(rule_board), 8)
        self.assertEqual(set(rule_board), {0, 1})
        self.assertEqual(rule_board, [0, 1, 1, 1, 1, 0, 0, 0])

    def test_apply_rule(self):
        rule_board = [0, 1, 1, 0, 1, 0, 0, 1]
        left = np.array(0)
        state = np.array(1)
        right = np.array(0)
        result = apply_rule(rule_board, left, state, right)
        self.assertEqual(result, 1)

    def test_evolve(self):
        rule_board = [0, 1, 1, 0, 1, 0, 0, 1]
        initial_state = np.array([0, 1, 0, 1, 0, 1, 0, 1])
        steps = 3
        history = evolve(rule_board, initial_state, steps)
        self.assertEqual(len(history), steps + 1)
        self.assertEqual(len(history[0]), len(initial_state))

    def test_plot_evolution(self):
        rule_board = [0, 1, 1, 0, 1, 0, 0, 1]
        initial_state = np.array([0, 1, 0, 1, 0, 1, 0, 1])
        steps = 3
        history = evolve(rule_board, initial_state, steps)
        plot_evolution(history, len(initial_state), steps)


if __name__ == "__main__":
    unittest.main()
