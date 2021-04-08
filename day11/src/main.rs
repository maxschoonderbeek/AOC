
use std::fs;

const _RAW_INP1: &str = r"L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL";

fn main() {
    let input = fs::read_to_string("src/input.txt").expect("Something went wrong reading the file");
    
    // let input = _RAW_INP1.to_string();
    
    let seats: Vec<_> = input
        .chars()
        .filter(|c| *c != '\n')
        .map(|c| match c { 'L' => true, '.' => false, _=>panic!() })
        .collect();
    let row_len = input.split('\n').count();
    let col_len = seats.len() / row_len;
    
    
    // Try to create 2D vector
    // let seats2d = seats.chunks(row_len);
    // println!("{:?}", seats2d);
    // let mut occupied:Vec<Vec<bool>> = vec![vec![false;seats.len()]];
    
    let mut occupied_new:Vec<isize> = vec![0;seats.len()];
    let mut occupied:Vec<isize> = vec![0;seats.len()];
    let mut stable = false;
    while !stable {
        for col in 0..col_len{
            for row in 0..row_len{
                let index = idx(col, row, row_len);
                if seats[index] {
                    if occupied[index] == 1
                    {
                        if count_neighbours(&occupied, row, col, row_len, col_len) >= 4 {
                            occupied_new[index] = 0;
                        }  
                    }
                    else
                    {
                        if count_neighbours(&occupied, row, col, row_len, col_len) == 0 {
                            occupied_new[index] = 1;
                        }
                    }
                }
            }
        }
        if occupied == occupied_new {
            stable = true;
        }
        //println!("occupied = {:?}", occupied_new.chunks(10));
        occupied = occupied_new.clone();
    }
    //println!("count = {:?}", occupied);
    println!("count = {}", occupied.iter().filter(|&i|*i == 1).count());
}

fn count_neighbours(occupied:&Vec<isize>, row:usize, col:usize, row_len:usize, col_len:usize) -> isize
{
    let mut neighbour_count=0;
    let row = row as isize;
    let col = col as isize;
    for rw in (row-1)..(row+2) {
        for cl in (col-1)..(col+2) {
            if (0 <= rw && rw < row_len as isize) && (0 <= cl && cl < col_len as isize) {
                if !(rw == row && cl == col) {
                    neighbour_count += occupied[idx(rw as usize, cl as usize, row_len)];
                }
                
            }
            
        }
    }
    return neighbour_count;
}

fn idx(col:usize, row:usize, row_len:usize)->usize
{
    return col * row_len + row;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn verify_count_neighbors() {
        let ret_vec = count_neighbours(&vec![1;9], 2, 1, 3, 3);
        assert_eq!(5, ret_vec);

        let ret_vec = count_neighbours(&vec![0, 0, 0, 0, 0, 0, 1, 1, 1], 1, 1, 3, 3);
        assert_eq!(3, ret_vec);

        let ret_vec = count_neighbours(&vec![1;9], 1, 1, 3, 3);
        assert_eq!(8, ret_vec);



    }

}