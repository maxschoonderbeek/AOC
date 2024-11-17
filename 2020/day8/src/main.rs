use std::{collections::{HashSet}, fs, str::FromStr};

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

#[derive(Debug)]

enum Instruction {
    Acc,
    Jmp,
    Nop
}


fn main() {
    let txt_input =
        fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");

    // let txt_input = _RAW_INP1.to_string();
    let txt_input:Vec<&str> = txt_input.split("\n").collect();
    let mut instruction_set:  Vec<(Instruction, i32)> = creat_instruction_list(txt_input);

    let (global, line_nr) = calculate_global(&instruction_set);
    println!("Global with a bug is {} and stopped on line {}",global, line_nr+1);

    let mut solution_found: bool = false;
    let mut global : i32 = 0;
    let mut line_nr: i32 = 0;

    // Just start replacing jmp->nop and nop->jmp one-by-one until a solution is found.
    for line_fix in 0..instruction_set.len() {
        switch_jmp_and_nop(&mut(instruction_set[line_fix].0));
        let out_tuple: (i32, i32) = calculate_global(&instruction_set);
        switch_jmp_and_nop(&mut(instruction_set[line_fix].0));

        global = out_tuple.0;
        line_nr = out_tuple.1;
        // Succesfull run when next line_nr is immediatelly after the last instruction of the file 
        if line_nr == instruction_set.len() as i32 
        {
            solution_found = true;
            break;
        }
    }

    println!("Found fix = {}, Global with a fix = {}, stopped at line {}",solution_found, global, line_nr+1);
}

fn creat_instruction_list(txt_input:Vec<&str>) -> Vec<(Instruction, i32)>{
    let mut instruction_set : Vec<(Instruction,i32)> = Vec::new();
    let re_command = Regex::new(r"^(\w+) ([+|-][0-9]+)").unwrap();
    for command_str in txt_input
    {
        let cap = re_command.captures(command_str).unwrap();
        let number : i32 = FromStr::from_str(&cap[2]).unwrap();
        let mut instruction : Instruction = Instruction::Nop;
        match &cap[1] {
            "acc" => instruction = Instruction::Acc,
            "jmp" => instruction = Instruction::Jmp,
            "nop" => instruction = Instruction::Nop,
            _ => println!("deafult clause"),
        };
        instruction_set.push((instruction,number));
    }
    return instruction_set;
}

fn calculate_global(instruction_set: &Vec<(Instruction, i32)>) -> (i32, i32) {
    let mut executed_lines : HashSet<i32> = HashSet::new();
    let mut global : i32= 0;
    let mut line_nr : i32 = 0;
    let mut infinite_loop = false;
    while !infinite_loop {
        global+=interpret_command(&instruction_set[line_nr as usize], &mut line_nr);
        // Stop when either a loop is entered, or next line is out-of-file.
        if !executed_lines.insert(line_nr) || 
            line_nr >= instruction_set.len() as i32 ||
            line_nr < 0
        {
            infinite_loop = true;
        };
    }
    return (global, line_nr);
}

fn interpret_command(instruction : &(Instruction,i32), line_nr : &mut i32) -> i32 {
    let mut add_to_global = 0;
    match instruction.0 {
        Instruction::Acc => {
            add_to_global += instruction.1;
                *line_nr += 1;
        }
        Instruction::Jmp => *line_nr += instruction.1,
        Instruction::Nop => *line_nr += 1,
    };
    return add_to_global;
}



fn switch_jmp_and_nop(instruction: &mut Instruction)
{
    match *instruction
    {
        Instruction::Jmp => *instruction = Instruction::Nop,
        Instruction::Nop => *instruction = Instruction::Jmp,
        Instruction::Acc => *instruction = Instruction::Acc,
    }
}