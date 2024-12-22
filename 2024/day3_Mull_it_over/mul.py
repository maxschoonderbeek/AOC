import re
import os

def reader(filename):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, filename)
    with open(abs_file_path) as f:
        lines = f.readlines()

    return ''.join(line.strip() for line in lines)

def solve_puzzle(data):
    r = re.compile(r"((mul\([0-9]{0,3},[0-9]{0,3}\))|(do(n\'t)?\(\)))")
    expressions = r.findall(data)
    expressions = [expr[0] for expr in expressions]
    print(expressions)
    enabled = True
    total = 0
    for expr in expressions:
        if expr.startswith("do("):
            enabled = True
            print(f"Enable: {enabled}")
        elif expr.startswith("don't("):
            enabled = False
            print(f"Enable: {enabled}")
        elif enabled:
            a, b = expr[4:-1].split(",")
            mul = int(a) * int(b)
            total += mul
            print(f"{a} * {b} = {mul}")
    print(f"Total: {total}")

if __name__ == "__main__":
    solve_puzzle(reader("input.txt"))