use std::{fs, usize};


fn main() {
    let txt_input = fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");

    let jolt_input = interpret_txt_input(txt_input);

    let (jumps, mult) = puzzle1(&jolt_input);
    println!("jumps puzzle 1 = {:?}, multiplication = {}",jumps, mult);
    
    let arrangements = puzzle2(&jolt_input);
    println!("arrangements = {}",arrangements);
}

fn puzzle1(jolt_input: &Vec<usize>) -> (Vec<i32>, i32) {
    let mut previous_jolt = 0;
    let mut jumps = vec![0,0,0];
    for jolt in jolt_input
    {
        if *jolt != 0 {
            let jump_idx: usize = jolt - previous_jolt -1;
            jumps[jump_idx] += 1;
            previous_jolt = *jolt;
        }
    }
    jumps[2] += 1;
    let multiplication = jumps[0]*jumps[2];
    (jumps, multiplication)
}

fn puzzle2(jolt_input: &Vec<usize>) -> i32 {

    let mut  jolt_list = vec![0;jolt_input.len()];
    jolt_list[0] = 1;
    jolt_list[1] = 1;
    jolt_list[2] = 2;

    for jolt_idx in 3..jolt_input.len() {
        for previous_idx in jolt_idx-3..jolt_idx {
            let jump = jolt_input[jolt_idx] - jolt_input[previous_idx]; 
            if jump == 1 || jump == 2 || jump == 3 {
                jolt_list[jolt_idx] += jolt_list[previous_idx];
            }
        }
        
    }
    println!("{:?}",jolt_list);
    let arrangements = *jolt_list.last().unwrap();
    
    return arrangements
}

fn interpret_txt_input(txt_input: String) -> Vec<usize> {
    let mut int_input: Vec<_> = txt_input
        .lines()
        .map(|s| s.parse::<usize>().unwrap())
        .collect();
    // push the wall connection
    int_input.push(0);
    int_input.sort();
    int_input
}

#[cfg(test)]
mod tests {
    use super::*;
    const TST_INP: &str = r"28
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

    #[test]
    fn verify_puzzle_1() {
        
        let txt_input = TST_INP.to_string();

        let int_input = interpret_txt_input(txt_input);

        let (jumps, _mult) = puzzle1(&int_input);
        assert_eq!(jumps[0], 22);
        assert_eq!(jumps[2], 10);
    }

    #[test]
    fn verify_puzzle_2() {
        
        let txt_input = TST_INP.to_string();

        let int_input = interpret_txt_input(txt_input);

        let arrangements = puzzle2(&int_input);
        assert_eq!(arrangements, 19208);
    }
}