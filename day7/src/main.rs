use std::{
    collections::{HashMap},
    collections::{HashSet},
    str::FromStr,
    fs,
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

fn create_bag_rules(content: &String) -> HashMap<String, Vec<(usize, String)>> {
    let mut bag_rules = HashMap::new();
    let re_container_bag = Regex::new(r"^(\w+ \w+) bags contain (.*)").unwrap();
    let re_contained_bags = Regex::new(r"([0-9]) (\w+ \w+)").unwrap();

    for line in content.split("\n") {
        for cap in re_container_bag.captures_iter(line) {
            let container = (&cap[1]).to_string();
            let mut contained_vec: Vec<(usize, String)> = Vec::new();
            for contained_entry in re_contained_bags.captures_iter(&cap[2]) {
                let sub_bag = (&contained_entry[2]).to_string();
                let nr_of_sub_bag : usize = FromStr::from_str(&contained_entry[1]).unwrap_or(0);
                contained_vec.push((nr_of_sub_bag, sub_bag));
            }
            bag_rules.insert(container, contained_vec);
        }
    }
    return bag_rules;
}

// Create an inverted Hashmap to easily search, don't know any trics for this, 
// maybe already create in initial bag_rule creation.
fn invert_bag_rules(bag_rules : &HashMap<String, Vec<(usize, String)>>) -> HashMap<String,Vec<String>> {
    let mut inverted_bags :HashMap<String,Vec<String>> = HashMap::new();
    for (container, contained) in bag_rules {
        for bag in contained {
            // Create an entry for the contained bag, and add container to the list 
            inverted_bags.entry(bag.1.clone()).or_insert(Vec::new()).push(container.clone());
        }
    }
    return inverted_bags;
}

// Recurently count bags in which bag_colour could be
fn find_bag_with_colour(inverted : &HashMap<String, Vec<String>>, outer_set : &mut HashSet<String>, bag_colour : &String) {
    if inverted.contains_key(bag_colour)  {
        for container_colour in inverted[bag_colour].iter() {
            // This bag is put in another bag. Add to the list and continue to check.
            outer_set.insert(container_colour.clone());
            find_bag_with_colour(inverted, outer_set, &container_colour);
        }
    }

}

// Recurently count the bag content
fn count_bags(bag_rules : &HashMap<String, Vec<(usize, String)>>, bag_colour : &String) -> usize {    
    let mut count = 0;
    if bag_rules[bag_colour].len() == 0 {
        // This bag is counted on higher level 
        count = 0;
    }
    else {
        for contained_bags in bag_rules[bag_colour].iter() {
            count += contained_bags.0;
            count += contained_bags.0 * count_bags(bag_rules, &contained_bags.1);
        }
    }
    return count;
}

fn main() {
    let txt_input =
        fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");

    // let txt_input = _RAW_INP1.to_string();
    // let txt_input = _RAW_INP2.to_string();

    let bag_rules = create_bag_rules(&txt_input);
    let inverted = invert_bag_rules(&bag_rules);

    // The outer set will contian all bags that can have a shiny gold bag inside
    let mut outer_set : HashSet<String> = HashSet::new();
    find_bag_with_colour(&inverted, &mut outer_set, &"shiny gold".to_string());
    println!("Shiny Gold bags can be found in {} different bags", outer_set.len());

    // The outer set will contian all bags that can have a shiny gold bag inside
    let count = count_bags(&bag_rules, &"shiny gold".to_string());
    println!("A Shiny Gold bag contains {} different bags", count);    
}
