import os
import re

def reader(filename):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, filename)
    with open(abs_file_path) as f:
        lines = f.readlines()

    return lines

def writer(data):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, "out.txt")
    with open(abs_file_path, 'w') as f:
        f.writelines(data)

def place_dots(rows, cols, data, matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                data[i] = data[i][:j] + '.' + data[i][j+1:]
    return data



def b_diag(rows, cols, data):
    bdiag = [[] for _ in range(rows + cols - 1)]
    min_bdiag = -rows + 1
    for i in range(rows):
        for j in range(cols):
            bdiag[j-i-min_bdiag].append(data[i][j])
    bdiag = [''.join(x) for x in bdiag]
    return bdiag

def match_bdiag(rows, matrix, r, bdiag, nr_of_matches):
    for i, line in enumerate(bdiag):
        for match in r.finditer(line):
            nr_of_matches += 1
            start, end = match.span(1)
            for j in range(start, end):
                if i < rows:
                    matrix[(rows-1)-i+j][j] = 1
                else:
                    matrix[j][i-(rows-1)+j] = 1
    return nr_of_matches

def f_diag(rows, cols, data):
    fdiag = [[] for _ in range(rows + cols - 1)]
    min_fdiag = -rows + 1
    for i in range(rows):
        for j in range(cols):
            fdiag[i+j].append(data[i][j])
    fdiag = [''.join(x) for x in fdiag]
    return fdiag

def match_fdiag(cols, matrix, r, fdiag, nr_of_matches):
    for i, line in enumerate(fdiag):
        for match in r.finditer(line):
            nr_of_matches += 1
            start, end = match.span(1)
            for j in range(start, end):
                if i < cols:
                    matrix[0+j][i-j] = 1
                else:
                    matrix[i-(cols-1)+j][(cols-1)-j] = 1
    return nr_of_matches

def solve_puzzle(data):
    nr_of_matches = 0
    rows = len(data)
    cols = len(data[0].strip()) if rows > 0 else 0
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    r = re.compile(r"(?=(XMAS|SAMX))")

    for i, line in enumerate(data):
        for match in r.finditer(line):
            nr_of_matches += 1
            start, end = match.span(1)
            for j in range(start, end):
                matrix[i][j] = 1

    for j in range(cols):
        col_data = ''.join(data[i][j] for i in range(rows))
        for match in r.finditer(col_data):
            nr_of_matches += 1
            start, end = match.span(1)
            for i in range(start, end):
                matrix[i][j] = 1

    bdiag = b_diag(rows, cols, data)
    nr_of_matches = match_bdiag(rows, matrix, r, bdiag, nr_of_matches)

    fdiag = f_diag(rows, cols, data)
    nr_of_matches = match_fdiag(cols, matrix, r, fdiag, nr_of_matches)

    place_dots(rows, cols, data, matrix)
    writer(data)
    print(f"Matches: {nr_of_matches}")
    return data

if __name__ == "__main__":
    _ = solve_puzzle(reader("input.txt"))