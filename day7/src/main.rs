use std::{
    collections::{HashMap},
    fs,
    str::FromStr,
};

use regex::Regex;
const _RAW_INP1: &str = r"light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.";

const _RAW_INP2: &str = r"shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.";

fn create_data_struct(content: &String) -> HashMap<String, Vec<(i32, String)>> {
    let mut data_struct = HashMap::new();
    let re_whole = Regex::new(r"^(\w+ \w+) bags contain (.*)").unwrap();
    let re_sub = Regex::new(r"([0-9]) (\w+ \w+)").unwrap();

    for line in content.split("\n") {
        for cap in re_whole.captures_iter(line) {
            let key = (&cap[1]).to_string();
            let mut value: Vec<(i32, String)> = Vec::new();
            for (i, sub_cap) in re_sub.captures_iter(&cap[2]).enumerate() {
                let sub_bag = (&sub_cap[2]).to_string();
                value.push((FromStr::from_str(&sub_cap[1]).unwrap_or(0), sub_bag));
            }
            data_struct.insert(key, value);
        }
    }
    return data_struct;
}

fn main() {
    let contents =
        fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");

    let mut total_related_bags = 0;
    let _cur_inp = _RAW_INP1.to_string();

    let data_struct = create_data_struct(&_cur_inp);



    println!("Total shiny bags are {}", total_related_bags);
}
