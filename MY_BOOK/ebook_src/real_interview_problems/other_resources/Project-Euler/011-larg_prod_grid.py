#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import string

def get_grid(filename):
    grid = [ [ 0 for i in range(20) ] for j in range(20) ]
    with open(filename) as file:
        for row, line in enumerate(file):
            line.strip('\n')
            for collumn, number in enumerate(line.split(' ')):
                grid[row][collumn] = int(number)
    return grid


def larg_prod_grid(grid):
    row, col, larg_prod = 0, 0, 0
    up, down, left, right, diag1, diag2, diag3, diag4 = 0, 0, 0, 0, 0, 0, 0, 0
    while row < len(grid):
        while col < len(grid[0]):           
            if col > 2: 
                up = grid[row][col] * grid[row][col-1] * grid[row][col-2] * grid[row][col-3]
            if col <  len(grid[0]) - 3:
                down = grid[row][col] * grid[row][col+1] * grid[row][col+2] * grid[row][col+3]
            if row > 2:
                left = grid[row][col] * grid[row-1][col] * grid[row-2][col] * grid[row-3][col]
            if row <  len(grid) - 3:
                right = grid[row][col] * grid[row+1][col] * grid[row+2][col] * grid[row+3][col]
            
            if col > 2 and row > 2:
                diag1 = grid[row][col] * grid[row-1][col-1] * grid[row-2][col-2] * grid[row-3][col-3]       
            if col > 2 and row <  len(grid) - 3:
                diag2 = grid[row][col] * grid[row+1][col-1] * grid[row+2][col-2] * grid[row+3][col-3]
            
            if col <  len(grid[0]) - 3 and row > 2:
                diag3 = grid[row][col] * grid[row-1][col+1] * grid[row-2][col+2] * grid[row-3][col+3]    
            if col <  len(grid[0]) -3 and   row <  len(grid) - 3:
                down = grid[row][col] * grid[row+1][col+1] * grid[row+1][col+2] * grid[row+1][col+3]
            
            l1 = [up, down, left, right, diag1, diag2, diag3, diag4]
            largest_prod_here = max(l1)
            if largest_prod_here > larg_prod:
                larg_prod = largest_prod_here 
            col += 1
        col = 0
        row += 1
   
    return larg_prod

    
def main():
    import time
    start = time.time() 
     
    filename = 'larg_prod_grid.dat'
    grid = get_grid(filename)
    assert((grid[6][8], grid[7][9], grid[8][10], grid[9][11]) == (26, 63, 78, 14))
    print(larg_prod_grid(grid))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

