"""this is a second try to solve the puzzle 2 of day 2 of the advent of code 2024"""
from reader import Reader

def calculate_diff(numbers):
    diffs = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
    nr_of_positive_diffs = sum(1 for diff in diffs if diff > 0)
    nr_of_negative_diffs = sum(1 for diff in diffs if diff < 0)
    nr_of_zero_diffs = diffs.count(0)
    return diffs, nr_of_positive_diffs, nr_of_negative_diffs, nr_of_zero_diffs

def assert_report_is_safe(numbers):
    diffs, nr_of_positive_diffs, nr_of_negative_diffs, nr_of_zero_diffs = calculate_diff(numbers)
    assert nr_of_zero_diffs == 0, "Zero diffs"
    assert nr_of_positive_diffs == 0 or nr_of_negative_diffs == 0, "Not all positive or negative diffs"
    assert all(1 <= abs(diff) <= 3 for diff in diffs), "Diff is not between 1 and 3"

def assert_is_valid_experiment(experiment):
    try:
        return assert_report_is_safe(experiment)
    except AssertionError:
        pass

    for index in range(len(experiment)):
        try:
            tmp = experiment.copy()
            tmp.pop(index)
            return assert_report_is_safe(tmp)
        except AssertionError:
            pass
    assert False, "No solution found"

def solve_puzzle(data):
    valid_experiments = 0
    for experiment in data:
        try:
            assert_is_valid_experiment(experiment)
            valid_experiments += 1
        except AssertionError as e:
            print(f"Exception: {e}")
            pass
    print(f"Valid experiments: {valid_experiments}")


if __name__ == "__main__":
    solve_puzzle(Reader().load_int_separated_by_space("input.txt"))