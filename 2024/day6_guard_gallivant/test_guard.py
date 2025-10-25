import unittest
from guard import *

class TestGuardPuzzle(unittest.TestCase):
    def setUp(self):
        # Read test input
        with open('test.txt', 'r') as f:
            self.test_input = f.read()

    def test_solve_part1(self):
        """Test part 1 solution with test input"""
        result = solve_part1(self.test_input)
        self.assertEqual(result, 41)

    def test_solve_part2(self):
        """Test part 2 solution with test input"""
        result = solve_part2(self.test_input)
        self.assertEqual(result, 6)

    def test_find_start_position(self):
        """Test finding the start position in the matrix"""
        matrix = convert_to_2d_array(self.test_input)
        [row, col, direction] = find_start_position(matrix)
        self.assertEqual(row, 6)
        self.assertEqual(col, 4)
        self.assertEqual(direction, 'N')  # Starting direction is North

if __name__ == '__main__':
    unittest.main()