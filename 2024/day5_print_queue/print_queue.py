import os
import re
import sys
from pathlib import Path

# Add the parent directory to sys.path so we can import Facilities
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Facilities.reader import reader

def check_before(index, page, pages, rules):
    for before, after in rules:
        if before == page and after in pages[:index]:
            return False
    return True

def check_after(index, page, pages, rules):
    for before, after in rules:
        if after == page and before in pages[index+1:]:
            return False
    return True

def right_order(pages, rules):
    # Check if the pages are in the right order according to the rules
    for index, page in enumerate(pages):
        if not (check_before(index, page, pages, rules) and check_after(index, page, pages, rules)):
            return False
    return True

def sort_using_rules(rules, pages):
    # Sort the pages according to the rules using a bubble sort
    sorted_pages = pages[:]
    n = len(sorted_pages)
    for i in range(n):
        for j in range(0, n-i-1):
            if not check_before(j+1, sorted_pages[j+1], sorted_pages, rules):
                # Swap
                sorted_pages[j], sorted_pages[j+1] = sorted_pages[j+1], sorted_pages[j]
    return sorted_pages

def process_print_queue(rules, print_queue):
    # Process the print queue according to the rules
    processed_queue = []
    incorrect_queue = []
    for pages in print_queue:
        if right_order(pages, rules):
            processed_queue.append(pages)
        else:
            incorrect_queue.append(pages)

    corrected_queue = []
    for pages in incorrect_queue:
        # Try to correct the order by sorting the pages
        sorted_pages = sort_using_rules(rules,pages)
        corrected_queue.append(sorted_pages)

    # Sum the middle page numbers of the processed queue items
    middle_sum = sum_middle_numbers(processed_queue)
    middle_sum_corrected_queue = sum_middle_numbers(corrected_queue)

    return middle_sum, middle_sum_corrected_queue

def sum_middle_numbers(processed_queue):
    middle_sum = 0
    for pages in processed_queue:
        if len(pages) > 2:
            middle_page = pages[len(pages) // 2]
            middle_sum += int(middle_page)
    return middle_sum

def solve_puzzle(data):
    # The data consists of 2 parts: The page ordering rules and the print queue

    split_index = data.index('\n')
    rules = data[:split_index]
    print_queue = data[split_index + 1:]

    # Remove \n characters
    rules = [rule.strip() for rule in rules if rule.strip()]
    print_queue = [item.strip() for item in print_queue if item.strip()]

    # Each rule has two parts separated by | (before and after)
    rules = [rule.split('|') for rule in rules]
    print_queue = [item.split(',') for item in print_queue]


    # Print debug info: firest 5 rules and first 5 print queue items
    print("First 5 rules:")
    for rule in rules[:5]:
        print(rule)
    print("\nFirst 5 print queue items:")
    for item in print_queue[:5]:
        print(item)

    middle_sum = process_print_queue(rules, print_queue)
    print(f"Sum of middle pages: {middle_sum}")


if __name__ == "__main__":
    _ = solve_puzzle(reader("input.txt"))
