# This algo was part of a tutorial on how to build a sudoku checker but they left out the final code to get it working
# I still haven't finished it. Came from Youtube. 

INVALID_GRID = [
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9]
]

intended_square = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

VALID_GRID = [
    [4,3,5,2,6,9,7,8,1],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

def check_rows(grid):
    for row in grid:
        if is_valid_row(row) == False:
            return False  
    return True
        
def is_valid_row(row):
    required_numbers = [1,2,3,4,5,6,7,8,9]
    for number in required_numbers:
        if number not in row:
            return False
    return True
    
def check_columns(grid):
    columns = []
    for index in range(9):
        new_column = []
        for row in grid:
            new_column.append(row[index])
        columns.append(new_column)
    return check_rows(columns)
 
def check_squares(grid_9by9):
    rows_of_squares = make_squares(grid_9by9)
    for row_of_squares in rows_of_squares:
        for square in row_of_squares:
            if check_square(square) == False:
                return False       
    return True
    
def check_square(grid_3by3):
    required_numbers = [1,2,3,4,5,6,7,8,9]
    numbers_in_grid = []
    for rows in grid_3by3:
        for number in rows:
            numbers_in_grid.append(number)
    for number in numbers_in_grid:
        if number not in required_numbers:
            return False
    return True
    
def make_square(grid):
    grid_3by3 = []
    for rows in grid:
        for number in row:
            
    
def check_sudoku(grid):
    if check_rows(grid):
        print "Rows look good"
        if check_columns(grid):
            print "Columns look good"
            if check_squares(grid):
                return true
                
#check_sudoku
