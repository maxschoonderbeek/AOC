
use std::{fs};

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
    println!("row length = {}, collumn length = {}", row_len, col_len);
    
    // Try to create 2D vector
    // let seats2d = seats.chunks(row_len);
    // println!("{:?}", seats2d);
    // let mut occupied:Vec<Vec<bool>> = vec![vec![false;seats.len()]];
    
    let mut occupied_new:Vec<isize> = vec![0;seats.len()];
    let mut occupied:Vec<isize> = vec![0;seats.len()];
    let mut stable = false;
    let mut run_id = 0;
    while !stable {
        for col in 0..col_len{
            for row in 0..row_len{
                let index = idx(col, row, col_len);
                if seats[index] {
                    if occupied[index] == 1
                    {
                        if count_neighbours(&occupied, col, row, row_len, col_len) >= 4 {
                            occupied_new[index] = 0;
                        }  
                    }
                    else
                    {
                        if count_neighbours(&occupied, col, row, row_len, col_len) == 0 {
                            occupied_new[index] = 1;
                        }
                    }
                }
            }
        }
        if occupied == occupied_new {
            stable = true;
        }
        run_id+=1;
        println!("{}",run_id);
        occupied = occupied_new.clone();
    }
    //println!("seat occupation = {:?}", occupied);
    println!("count = {}", occupied.iter().filter(|&i|*i == 1).count());

    // -------------
    // Puzzle 2
    // -------------
    // reset occupancy
    occupied_new = vec![0;seats.len()];
    occupied = vec![0;seats.len()];
    stable = false;
    run_id = 0;
    while !stable {
        for col in 0..col_len{
            for row in 0..row_len{
                let index = idx(col, row, col_len);
                if seats[index] {
                    if occupied[index] == 1
                    {
                        if count_neighbours_in_sight(&seats, &occupied, col, row, row_len, col_len) >= 5 {
                            occupied_new[index] = 0;
                        }  
                    }
                    else
                    {
                        if count_neighbours_in_sight(&seats, &occupied, col, row, row_len, col_len) == 0 {
                            occupied_new[index] = 1;
                        }
                    }
                }
            }
        }
        if occupied == occupied_new {
            stable = true;
        }
        run_id+=1;
        println!("{}",run_id);
        occupied = occupied_new.clone();
    }
    println!("count = {}", occupied.iter().filter(|&i|*i == 1).count());
}

fn count_neighbours(occupied:&Vec<isize>, col:usize, row:usize, row_len:usize, col_len:usize) -> isize
{
    let mut neighbour_count=0;
    let row = row as isize;
    let col = col as isize;
    for rw in (row-1)..=(row+1) {
        for cl in (col-1)..=(col+1) {
            if (0 <= rw && rw < row_len as isize) && (0 <= cl && cl < col_len as isize) {
                if !(rw == row && cl == col) {
                    neighbour_count += occupied[idx(cl as usize,rw as usize,  col_len)];
                }
                
            }
            
        }
    }
    return neighbour_count;
}

fn count_neighbours_in_sight(seats:&Vec<bool>, occupied:&Vec<isize>, col:usize, row:usize, row_len:usize, col_len:usize) -> isize
{
    let mut neighbour_count=0;
    // create clockwise directions (col,row)
    let direction_tuple: [(isize,isize);8] = [(-1,-1), (0,-1), (1,-1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)];
    for direction in direction_tuple.iter(){
        neighbour_count += search_in_direction(seats, occupied, col, row, row_len, col_len, direction);
    }
    return neighbour_count;
}

fn search_in_direction(seats:&Vec<bool>, occupied:&Vec<isize>, col:usize, row:usize, row_len:usize, col_len:usize, direction:&(isize, isize)) -> isize
{
    let mut at_edge = false;
    let mut rw = row as isize;
    let mut cl = col as isize;
    while !at_edge {
        cl += direction.0;
        rw += direction.1;
        if (0 <= rw && rw < row_len as isize) && (0 <= cl && cl < col_len as isize) 
        {
            if seats[idx(cl as usize, rw as usize, col_len)] 
            {
                if occupied[idx(cl as usize, rw as usize, col_len)] == 1
                {
                    return 1;
                }
                else
                {
                    return 0;
                }
            }
        }
        else
        {
            at_edge = true;
        }
    }
    return 0;
}

fn idx(col:usize, row:usize, col_len:usize)->usize
{
    return row * col_len + col;
}

#[cfg(test)]
mod tests {
    use super::*;

    
    #[test]
    fn verify_count_neighbors_in_sieght() {
        // Test design:
        //  # L # L L
        //  L . . . L
        //  L L T L #
        //  L L L L L
        //  L L L L L
        let col_len = 5;
        let row_len = 5;
        let mut seats = vec![true;25];
        seats[6] = false;
        seats[7] = false;
        seats[8] = false;
        let mut occupied = vec![0;25];
        
        occupied[0] = 1;
        occupied[2] = 1;
        occupied[idx(4, 2, col_len)];
        let neighbours = count_neighbours_in_sight(&seats, &occupied, 2, 2, row_len, col_len);
        assert_eq!(2, neighbours);
    }

    #[test]
    fn verify_count_neighbors() {
        // Test design:
        //  TL TP TR
        //   L MM  R
        //  BL BT BR
        // row length

        // bottom row
        let neighbours = count_neighbours(&vec![1;9], 2, 1, 3, 3);
        assert_eq!(5, neighbours);

        // top row
        let neighbours = count_neighbours(&vec![1;9], 0, 1, 3, 3);
        assert_eq!(5, neighbours);

        // top left corner
        let neighbours = count_neighbours(&vec![1;9], 0, 0, 3, 3);
        assert_eq!(3, neighbours);

        // top left corner
        let neighbours = count_neighbours(&vec![1;9], 2, 2, 3, 3);
        assert_eq!(3, neighbours);

        // Exactly in the middle
        let neighbours = count_neighbours(&vec![1;9], 1, 1, 3, 3);
        assert_eq!(8, neighbours);
        
        // Subset of data
        let neighbours = count_neighbours(&vec![0, 0, 0, 0, 0, 0, 1, 1, 1], 1, 1, 3, 3);
        assert_eq!(3, neighbours);
    }


    #[test]
    fn verify_matrix_equality() {
        // 1 2 3 
        // 4 5 6
        let mut a = vec![0, 1, 2, 3, 4];
        let b = a.clone();

        assert_eq!(a, b);

        a[2]=-1;
        assert_ne!(a, b);
    }

    #[test]
    fn verify_index() {
        let a = vec![1, 2, 3, 4, 5, 6];
        let row_length = 3;

        assert_eq!(2, a[idx(1,0,row_length)]);
        assert_eq!(4, a[idx(0,1,row_length)]);
    }
}