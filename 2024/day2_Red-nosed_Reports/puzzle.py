from reader import Reader

def calculate_diff(numbers):
    diffs = []
    previous_number = 0
    nr_of_positive_diffs, nr_of_negative_diffs, nr_of_zero_diffs = 0, 0, 0
    for index, number in enumerate(numbers):
        if index == 0:
            # skip logic on the first number
            pass
        else:
            diff = number - previous_number
            diffs.append(diff)
            if diff == 0:
                nr_of_zero_diffs += 1
            elif diff > 0:
                nr_of_positive_diffs += 1
            else:
                nr_of_negative_diffs += 1

        previous_number = number
    return diffs, nr_of_positive_diffs, nr_of_negative_diffs, nr_of_zero_diffs

def solve_puzzle_1(data):
    valid_experiments = 0
    for numbers in data:
        diffs, nr_of_positive_diffs, nr_of_negative_diffs, nr_of_zero_diffs = calculate_diff(numbers)
        if (nr_of_zero_diffs == 0):
            if(nr_of_positive_diffs == 0 or nr_of_negative_diffs == 0):
                if all(1 <= abs(diff) <= 3 for diff in diffs):
                    print(f"Valid: {numbers}, diffs: {diffs}")
                    valid_experiments += 1
    return valid_experiments

def is_between_1_and_3(diffs):
    return all(1 <= abs(diff) <= 3 for diff in diffs)

def solve_puzzle(data):
    valid_experiments = 0
    valid_with_one_mistake = 0
    removed_diff = 0
    removed_number = 0
    for numbers in data:
        diffs, nr_of_positive_diffs, nr_of_negative_diffs, nr_of_zero_diffs = calculate_diff(numbers)
        if (nr_of_zero_diffs == 0):
            if(nr_of_positive_diffs == 0 or nr_of_negative_diffs == 0):
                if is_between_1_and_3(diffs):
                    print(f"Valid: {numbers}, diffs: {diffs}")
                    valid_experiments += 1
                ### check whether mistake can be corrected. However, this doesn't correct enough mistakes:
                else: # remove one delta mistake
                    mistake_corrected = False
                    for i, diff in enumerate(diffs):
                        if (diff > 3) or (diff < -3) and not mistake_corrected:
                            if i != len(diffs) - 1:
                                diffs[i+1] = diff + diffs[i+1]
                            removed_diff = diff
                            diffs.pop(i)
                            removed_number = numbers[i+1]
                            numbers.pop(i+1)
                            mistake_corrected = True
                    if is_between_1_and_3(diffs):
                        print(f"Valid: {numbers}, diffs: {diffs}. Diff mistake, removed number: {removed_number}, removed_diff: {removed_diff}")
                        valid_with_one_mistake += 1
                    else:
                        print(f"Still invalid: {numbers}, diffs: {diffs}.")

            elif(nr_of_positive_diffs == 1) or (nr_of_negative_diffs == 1): # remove one direction mistake
                for i, diff in enumerate(diffs):
                    if diff > 0 and (nr_of_positive_diffs == 1) or diff < 0 and (nr_of_negative_diffs == 1):
                        if i != len(diffs) - 1:
                            diffs[i+1] = diff + diffs[i+1]
                        removed_diff = diff
                        diffs.pop(i)
                        removed_number = numbers[i+1]
                        numbers.pop(i+1)
                if is_between_1_and_3(diffs):
                    print(f"Valid: {numbers}, diffs: {diffs}. Direction mistake,  removed number: {removed_number}, removed_diff: {removed_diff}")
                    valid_with_one_mistake += 1
                else:
                    print(f"Still invalid: {numbers}, diffs: {diffs}.")

        elif (nr_of_zero_diffs == 1): # remove a single zero diff
            diffs.remove(0)
            if(nr_of_positive_diffs == 0 or nr_of_negative_diffs == 0):
                if is_between_1_and_3(diffs):
                    print(f"Valid: {numbers}, diffs: {diffs}. Zero diff mistake")
                    valid_with_one_mistake += 1
                else:
                    print(f"Still invalid: {numbers}, diffs: {diffs}.")
    print (f"Valid experiments zero mistakes: {valid_experiments}")
    print (f"Valid experiments one mistake: {valid_with_one_mistake}")
    print (f"Total: {valid_experiments + valid_with_one_mistake}")
    return valid_experiments + valid_with_one_mistake



if __name__ == "__main__":
    solve_puzzle(Reader().load_int_separated_by_space("input.txt"))
