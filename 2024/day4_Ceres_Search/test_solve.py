import unittest
import re
from solve import *
class TestCases(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        pass

    def tearDown(self):
        """Call after every test case."""
        pass

    def test_b_diag(self):
        data = ["345", "234", "123", "012"]
        expected = ["0", "11", "222", "333", "44", "5"]
        rows = 4
        col = 3

        ouput = b_diag(rows, col, data)
        self.assertEqual(ouput, expected)

    def test_match_b_diag(self):
        data = ["0", "11", "222", "333", "44", "5"]
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

        r = re.compile(r"(?=(333))")
        rows = 4
        nr_of_matches = 0

        nr_of_matches = match_bdiag(rows, matrix, r, data, nr_of_matches)
        self.assertEqual(matrix, expected)

    def test_match_b_diag_44(self):
        data = ["0", "11", "222", "333", "44", "5"]
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 0]]

        r = re.compile(r"(?=(44))")
        rows = 4
        nr_of_matches = 0

        nr_of_matches = match_bdiag(rows, matrix, r, data, nr_of_matches)
        self.assertEqual(matrix, expected)

    def test_f_diag(self):
        data = ["012", "123", "234", "345"]
        expected = ["0", "11", "222", "333", "44", "5"]
        rows = 4
        col = 3

        ouput = f_diag(rows, col, data)
        self.assertEqual(ouput, expected)

    def test_match_f_diag_0(self):
        data = ["0", "11", "222", "333", "44", "5"]
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        r = re.compile(r"(?=(0))")
        col = 3
        nr_of_matches = 0

        nr_of_matches = match_fdiag(col, matrix, r, data, nr_of_matches)
        self.assertEqual(matrix, expected)

    def test_match_f_diag_11(self):
        data = ["0", "11", "222", "333", "44", "5"]
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[0, 1, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0]]
        r = re.compile(r"(?=(11))")
        col = 3
        nr_of_matches = 0

        nr_of_matches = match_fdiag(col, matrix, r, data, nr_of_matches)
        self.assertEqual(matrix, expected)

    def test_match_f_diag_333(self):
        data = ["0", "11", "222", "333", "44", "5"]
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]
        r = re.compile(r"(?=(333))")
        col = 3
        nr_of_matches = 0

        nr_of_matches = match_fdiag(col, matrix, r, data, nr_of_matches)
        self.assertEqual(matrix, expected)

    #@unittest.skip("skip")
    def test_solve(self):

        data = ["MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX"]
        expected = ["....XXMAS.",
                    ".SAMXMS...",
                    "...S..A...",
                    "..A.A.MS.X",
                    "XMASAMX.MM",
                    "X.....XA.A",
                    "S.S.S.S.SS",
                    ".A.A.A.A.A",
                    "..M.M.M.MM",
                    ".X.X.XMASX"]
        output = solve_puzzle(data)
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main() # run all tests