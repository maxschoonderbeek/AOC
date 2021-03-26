use std::{collections::LinkedList, fs, usize};

const _RAW_INP1: &str = r"28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3";

fn main() {
    // let txt_input = fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");
    
    let txt_input = _RAW_INP1.to_string();

    let mut int_input: Vec<_> = txt_input
        .lines()
        .map(|s| s.parse::<usize>().unwrap())
        .collect();

    int_input.sort();

    let mut previous_jolt = 0;
    let mut jumps = vec![0,0,0];
    for jolt in int_input
    {
        let jump_idx: usize = jolt - previous_jolt -1;
        jumps[jump_idx] += 1;
        previous_jolt = jolt;
    }

    // After last one another 3 jump
    jumps[2] += 1;
    println!("jumps = {:?}, multiplication = {}",jumps, jumps[0]*jumps[2])


    
}
