use std::{collections::LinkedList, fs, str::FromStr, vec};

const _RAW_INP1: &str = r"35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576";

fn main() {
    let  list_length: i32 = 25;
    let txt_input = fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");
    
    // let list_length: i32 = 5;
    // let txt_input = _RAW_INP1.to_string();

    let int_input: Vec<_> = txt_input
        .lines()
        .map(|s| s.parse::<isize>().unwrap())
        .collect();
    
    let mut list: LinkedList<isize> = LinkedList::new();

    let mut input_iter = int_input.clone().into_iter();

    // Create preample
    for _start_list in 0..list_length 
    {
        list.push_back(input_iter.next().unwrap());
    }

    // Find the value which is incorrectly encoded
    let mut incorrect_preamble = -1;
    for next_value in input_iter 
    {
        if !preamble_correct(&list, &next_value)
        {
            incorrect_preamble = next_value;
            break;
        }
        list.pop_front();
        list.push_back(next_value);
    }

    let encryption_weakness = find_contiguous_range(&int_input, &incorrect_preamble);

    println!("next value = {}, encryption weakness = {}",incorrect_preamble, encryption_weakness);
}

fn preamble_correct(list: &LinkedList<isize>, next_value:&isize) -> bool
{
    for (iter_first_value, first_value) in list.iter().enumerate()
    {
        for (iter_second_value,second_value) in list.iter().enumerate()
        {
            if iter_first_value != iter_second_value
            {
                let sum_preamble_pair = first_value+second_value;
                if *next_value == sum_preamble_pair
                {
                    return true;
                }
            }
        }
    }
    return false;
}

fn find_contiguous_range(list: &Vec<isize>, incorrect_preamble:&isize) -> isize
{
    let mut contiguous_set:LinkedList<isize> = LinkedList::new();

    for item in list
    {
        contiguous_set.push_back(*item);
        // let sum : isize = contiguous_set.iter().sum();
        while contiguous_set.iter().sum::<isize>() > *incorrect_preamble
        {
            contiguous_set.pop_front();
        }
        if contiguous_set.iter().sum::<isize>() == *incorrect_preamble
        {
            break;
        }    
    }
    let smallest = contiguous_set.iter().min().unwrap(); 
    let largest = contiguous_set.iter().max().unwrap();
    return *smallest + *largest;
}