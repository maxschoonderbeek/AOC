

class IndexErrorCustom(Exception):
    def __init__(self, row, col, message="Custom error occurred"):
        self.row = row
        self.col = col
        self.message = message
        super().__init__(self.message)

class StopIterationCustom(Exception):
    def __init__(self, row, col, message="Custom error occurred"):
        self.row = row
        self.col = col
        self.message = message
        super().__init__(self.message)

def convert_to_2d_array(input_data):
    matrix = [list(map(str, line)) for line in input_data.splitlines()]
    return matrix

def find_start_position(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for row_nr in range(rows):
        for col_nr in range(cols):
            if matrix[row_nr][col_nr] == '^':
                # Assuming starting direction is 'N' (North)
                return [row_nr, col_nr, 'N']
    return None  # Return None if start position is not found

def check_limits(matrix, row, col, prev_row, prev_col):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    out_of_bounds = not (0 <= row < rows and 0 <= col < cols)
    if out_of_bounds:
        raise IndexErrorCustom(prev_row, prev_col, "Row or column out of bounds")
    return True

def keep_moving(matrix, row, col, direction):
    start_row, start_col = row, col
    while True:
        next_cell = nextCell(matrix, row, col, direction)
        if next_cell == '#':
            direction = rotate_clockwise(direction)
        else:
            [row, col] = move_forward(row, col, direction)
            if next_cell == '.':
                if direction == 'N':
                    matrix[row][col] = 'N'
                elif direction == 'S':
                    matrix[row][col] = 'S'
                elif direction == 'E':
                    matrix[row][col] = 'E'
                elif direction == 'W':
                    matrix[row][col] = 'W'
            elif (next_cell == 'N' and direction == 'N') \
                  or (next_cell == 'S' and direction == 'S') \
                  or (next_cell == 'E' and direction == 'E') \
                  or (next_cell == 'W' and direction == 'W'):
                raise StopIterationCustom(row,col,"Iteration stopped")  # Stop if we return on a visited path


def nextCell(matrix, row, col, direction):
    if direction == 'N':
        if check_limits(matrix, row-1, col, row, col):
            next_cell = matrix[row-1][col]
    elif direction == 'S':
        if check_limits(matrix, row+1, col, row, col):
            next_cell = matrix[row+1][col]
    elif direction == 'E':
        if check_limits(matrix, row, col+1, row, col):
            next_cell = matrix[row][col+1]
    elif direction == 'W':
        if check_limits(matrix, row, col-1, row, col):
            next_cell = matrix[row][col-1]
    else:
        raise ValueError("Invalid direction")
    return next_cell

def move_forward(row, col, direction):
    if direction == 'N':
        row -= 1
    elif direction == 'S':
        row += 1
    elif direction == 'E':
        col += 1
    elif direction == 'W':
        col -= 1
    return row, col

def rotate_clockwise(direction):
    if direction == 'N':
        direction = 'E'
    elif direction == 'E':
        direction = 'S'
    elif direction == 'S':
        direction = 'W'
    elif direction == 'W':
        direction = 'N'
    return direction

def solve_part1(input_data):
    """
    Args:
        input_data (str): Input data as a string.

    Returns:
        int: Solution to part 1.
    """
    matrix = convert_to_2d_array(input_data)
    start_position = find_start_position(matrix)

    if start_position:
        row, col, direction = start_position
        matrix[row][col] = 'N'  # Mark starting position
        try:
            keep_moving(matrix, row, col, direction)
        except IndexErrorCustom as e:
            pass
        except StopIterationCustom as e:
            pass

        with open('output.txt', 'w') as f:
            for row in matrix:
                f.write(''.join(row) + '\n')    # Count visited cells
        visited_count = sum(1 for row in matrix for cell in row if cell in {'N', 'S', 'E', 'W'})

    return visited_count


def solve_part2(input_data):
    """
    Returns:
        int: Solution to part 2.
    """
    matrix = convert_to_2d_array(input_data)
    start_position = find_start_position(matrix)
    loops_detected = 0
    if start_position:
        row, col, direction = start_position
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '.':
                    adapted_matrix = [row.copy() for row in matrix]
                    adapted_matrix[r][c] = '#'
                    try:
                        keep_moving(adapted_matrix, row, col, direction)
                    except IndexErrorCustom as e:
                        pass
                    except StopIterationCustom as e:
                        loops_detected += 1
                        pass

    return loops_detected


if __name__ == '__main__':
    # Read input from file
    with open('input.txt', 'r') as f:
        input_data = f.read()

    # Solve part 1
    result1 = solve_part1(input_data)
    print(f"Part 1 solution: {result1}")

    # Solve part 2
    result2 = solve_part2(input_data)
    print(f"Part 2 solution: {result2}")