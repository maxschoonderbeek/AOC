import unittest
from print_queue import *

rules = [
    (47, 53),
    (97, 13),
    (97, 61),
    (97, 47),
    (75, 29),
    (61, 13),
    (75, 53),
    (29, 13),
    (97, 29),
    (53, 29),
    (61, 53),
    (97, 53),
    (61, 29),
    (47, 13),
    (75, 47),
    (97, 75),
    (47, 61),
    (75, 61),
    (47, 29),
    (75, 13),
    (53, 13)
]
data_1 = [75,47,61,53,29]
data_2 = [97,61,53,29,13]
data_3 = [75,29,13]
data_4 = [75,97,47,61,53]
data_5 = [61,13,29]
data_6 = [97,13,75,29,47]


# Simple cases
simple_rules = [(1,2), (1,4), (2,3), (3,4), (2,4)]

data_10 = [1,2,3,4]
data_11 = [4,3,2,1]

class TestCases(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        pass

    def tearDown(self):
        """Call after every test case."""
        pass

    def test_data_10_array_on_before(self):
        isBefore = check_before(2, 2, data_10, simple_rules)
        self.assertEqual(isBefore, True)

    def test_data_11_array_page_2_not_before_3(self):
        isBefore = check_before(3, 2, data_11, simple_rules)
        self.assertEqual(isBefore, False)

    def test_data_10_array_not_on_after(self):
        isAfter = check_after(2, 2, data_10, simple_rules)
        self.assertEqual(isAfter, True)

    def test_data_11_array_4_not_after_2(self):
        isAfter = check_after(2, 2, data_11, simple_rules)
        self.assertEqual(isAfter, False)

    def test_data_11_array_3_not_after_2(self):
        isAfter = check_after(1, 3, data_11, simple_rules)
        self.assertEqual(isAfter, False)

    def test_data_10_array_on_right_order(self):
        rightOrder = right_order(data_10, simple_rules)
        self.assertEqual(rightOrder, True)

    def test_data_11_array_not_on_right_order(self):
        rightOrder = right_order(data_11, simple_rules)
        self.assertEqual(rightOrder, False)

    def test_data_1_array_on_right_order(self):
        rightOrder = right_order(data_1, rules)
        self.assertEqual(rightOrder, True)

    def test_data_2_array_on_right_order(self):
        rightOrder = right_order(data_2, rules)
        self.assertEqual(rightOrder, True)

    def test_data_3_array_on_right_order(self):
        rightOrder = right_order(data_3, rules)
        self.assertEqual(rightOrder, True)

    def test_data_4_array_not_on_right_order(self):
        rightOrder = right_order(data_4, rules)
        self.assertEqual(rightOrder, False)
    def test_data_5_array_not_on_right_order(self):
        rightOrder = right_order(data_5, rules)
        self.assertEqual(rightOrder, False)
    def test_data_6_array_not_on_right_order(self):
        rightOrder = right_order(data_6, rules)
        self.assertEqual(rightOrder, False)

    def test_solve_puzzle(self):
        sum,_ = process_print_queue(rules, [data_1, data_2, data_3, data_4, data_5, data_6])
        self.assertEqual(sum, 143)

    def test_solve_puzzle(self):
        _,sum = process_print_queue(rules, [data_1, data_2, data_3, data_4, data_5, data_6])
        self.assertEqual(sum, 123)


if __name__ == "__main__":
    unittest.main() # run all tests