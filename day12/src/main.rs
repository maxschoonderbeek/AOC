use std::{fs};

fn main() {
    let txt_input = fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");
    let data_struct = interpret_text(txt_input);
    let distance = puzzle1(&data_struct);
    println!("Manhatten distance = {}", distance);
    let distance = puzzle2(&data_struct);
    println!("Manhatten distance puzzle 2 = {}", distance);
}

fn interpret_text(input: String) -> Vec<(char, i32)> {
    let data_struct: Vec<(char, i32)> = input
        .lines()
        .map(|s| {
            let mut c = s.chars();
            let dir: char = c.next().unwrap();
            let nr: i32 = c.as_str().parse::<i32>().unwrap();
            (dir, nr)
        })
        .collect();
    data_struct
}

fn puzzle1(input :&Vec<(char, i32)>) -> i32 {
    let mut ship_dir = 90;
    let mut north_units:i32 = 0;
    let mut east_units:i32 = 0;

    for instruction in input {
        match instruction.0 {
            'N' => north_units += instruction.1,
            'E' => east_units += instruction.1,
            'S' => north_units -= instruction.1,
            'W' => east_units -= instruction.1,
            'L' => ship_dir = (ship_dir - instruction.1 + 360) % 360,
            'R' => ship_dir = (ship_dir + instruction.1) % 360,
            'F' => {
                match ship_dir {
                    0 => north_units += instruction.1,
                    90 => east_units += instruction.1,
                    180 => north_units -= instruction.1,
                    270 => east_units -= instruction.1,
                    _ => panic!("ship_dir = {}", ship_dir),
                }
            }
            _ => panic!(),
        }
    }
    // 44294 is too low...
    let distance = north_units.abs() + east_units.abs();
    distance
}

fn puzzle2(input :&Vec<(char, i32)>) -> i32 {
    let mut ship_north:i32 = 0;
    let mut ship_east:i32 = 0;
    let mut wp_north:i32 = 1;
    let mut wp_east:i32 = 10;

    // Rotation matrix
    // [ cos(theta) sin(theta);]
    let rot090:Vec<i32> = vec![ 0, -1,  1,  0];
    let rot180:Vec<i32> = vec![-1,  0,  0, -1];
    let rot270:Vec<i32> = vec![ 0,  1, -1,  0];

    for instruction in input {
        match instruction.0 {
            'N' => wp_north += instruction.1,
            'E' => wp_east += instruction.1,
            'S' => wp_north -= instruction.1,
            'W' => wp_east -= instruction.1,
            'L' => {
                match instruction.1 {
                     90 => rotate(&rot270, &mut wp_north, &mut wp_east),
                    180 => rotate(&rot180, &mut wp_north, &mut wp_east),
                    270 => rotate(&rot090, &mut wp_north, &mut wp_east),
                    _ => panic!("ratation = {} could not be handled", instruction.1),
                }
            },
            'R' => {
                match instruction.1 {
                     90 => rotate(&rot090, &mut wp_north, &mut wp_east),
                    180 => rotate(&rot180, &mut wp_north, &mut wp_east),
                    270 => rotate(&rot270, &mut wp_north, &mut wp_east),
                    _ => panic!("ratation = {} could not be handled", instruction.1),
                }
            },
            'F' => {
                ship_north += instruction.1 * wp_north;
                ship_east += instruction.1 * wp_east;
            },
            _ => panic!(),
        }
    }
    let distance = ship_north.abs() + ship_east.abs();
    distance
}

fn rotate(a: &Vec<i32>, wp_north: &mut i32, wp_east: &mut i32) {
    let wp_north_temp = *wp_north;
    let wp_east_temp = *wp_east;
    *wp_north = wp_north_temp * a[0] + wp_east_temp * a[1];
    *wp_east = wp_north_temp * a[2] + wp_east_temp * a[3];
}


#[cfg(test)]
mod tests {
    use super::*;
    const TST_INP: &str = r"F10
N3
F7
R90
F11";

    #[test]
    fn verify_puzzle_1() {
        
        let txt_input = TST_INP.to_string();

        let data_struct = interpret_text(txt_input);
        
        let distance = puzzle1(&data_struct);

        assert_eq!(distance, 25);
    }

    #[test]
    fn verify_puzzle_2() {
        
        let txt_input = TST_INP.to_string();

        let data_struct = interpret_text(txt_input);
        
        let distance = puzzle2(&data_struct);

        assert_eq!(distance, 286);
    }
}