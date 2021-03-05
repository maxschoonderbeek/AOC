use std::{
    collections::{HashSet},
    str::FromStr,
    fs,
};

use regex::Regex;

const _RAW_INP1: &str = r"nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6";

fn interpret_command(line_nr : &mut i32, command : &str) -> i32 {
    let mut global_addition = 0;
    let re_command = Regex::new(r"^(\w+) ([+|-])([0-9]+)").unwrap();
    let cap = re_command.captures(command).unwrap();
    let mut number : i32 = FromStr::from_str(&cap[3]).unwrap();
    if &cap[2] == "-" { number *= -1; };
    match &cap[1] {
        "acc" => {global_addition += number;
                *line_nr += 1;},
        "jmp" => *line_nr += number,
        "nop" => *line_nr += 1,
        _ => println!("deafult clause"),
    };
    return global_addition;
}

fn main() {
    let txt_input =
        fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");

    // The following is not allowed on a single line
    // let txt_input = _RAW_INP1.to_string();
    let txt_input:Vec<&str> = txt_input.split("\n").collect();

    let mut executed_lines : HashSet<i32> = HashSet::new();
    let mut global : i32= 0;
    let mut line_nr : i32 = 0;
    let mut line_nr_copy : i32 = 0;

    loop {
        global+=interpret_command(&mut line_nr, txt_input[line_nr_copy as usize]);
        line_nr_copy = line_nr;
        if !executed_lines.insert(line_nr)
        {
            // I did not find a method to do this in one go
            break;
        };
    }
    println!("Current Global is {}",global)
    // let program = create_program(&txt_input);
}
