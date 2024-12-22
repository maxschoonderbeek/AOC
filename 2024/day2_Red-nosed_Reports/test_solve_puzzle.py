# filepath: /c:/LocalData/Git/AOC/2024/day2_Red-nosed_Reports/test_puzzle.py
import unittest
from puzzle import solve_puzzle

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        pass

    def tearDown(self):
        """Call after every test case."""
        pass

    def test_solve_puzzle(self):
        data = [[1, 2, 3], [4, 5, 6]]
        valid = solve_puzzle(data)
        self.assertEqual(valid, 2)  # this should be correct


if __name__ == "__main__":
    unittest.main() # run all tests