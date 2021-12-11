import copy
import pprint
import numpy as np

def updateSurrounding(surr_slice):
    new_surr_slice = copy.deepcopy(surr_slice)
    for row in range(len(new_surr_slice)):
        for col in range(len(new_surr_slice[0])):
            if(new_surr_slice[row][col] > 0):
                new_surr_slice[row][col] += 1
    return new_surr_slice

def handleEdges(curr_row,curr_col,max_row,max_col):
    row_bounds = []
    col_bounds = []
    if (curr_row == 0):
        row_bounds = [0, curr_row+2]
    elif (curr_row == max_row):
        row_bounds = [curr_row-1, max_row+1]
    else:
        row_bounds = [curr_row-1, curr_row+2]
    if (curr_col == 0):
        col_bounds = [0, curr_col+2]
    elif (curr_col == max_col):
        col_bounds = [curr_col-1, max_col+1]
    else:
        col_bounds = [curr_col-1, curr_col+2]
    if not row_bounds or not col_bounds:
        print(" 8) This is error handling (bounds not filled):",row_bounds,col_bounds)
    return row_bounds, col_bounds

def checkContainsNines(state_board):
    has_nines = False
    for row in range(len(state_board)):
        for col in range(len(state_board[0])):
            if (state_board[row][col] >= 9):
                has_nines = True
                return has_nines
    return has_nines

def executeStep(state_board,prettyprinter):
    flashes = 0
    new_state_board = copy.deepcopy(state_board)
    for row in range(len(new_state_board)):
        for column in range(len(new_state_board[0])):
            new_state_board[row, column]+=1
    while checkContainsNines(new_state_board):
        for row in range(len(new_state_board)):
            for column in range(len(new_state_board[0])):
                if(new_state_board[row][column]>=9):
                    flashes += 1
                    new_state_board[row][column]=0
                    row_bounds, col_bounds = \
                        handleEdges(row,column,len(new_state_board)-1,len(new_state_board[0])-1)
                    # print("relevant part of board before propagating:")
                    # prettyprinter.pprint(new_state_board[row_bounds[0]:row_bounds[1], col_bounds[0]:col_bounds[1]])
                    new_state_board[row_bounds[0]:row_bounds[1], col_bounds[0]:col_bounds[1]] = \
                        updateSurrounding(new_state_board[row_bounds[0]:row_bounds[1], col_bounds[0]:col_bounds[1]])
                    # print("relevant part of board AFTER propagating:")
                    # prettyprinter.pprint(new_state_board[row_bounds[0]:row_bounds[1], col_bounds[0]:col_bounds[1]])
    return new_state_board, flashes

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    total_flashes = 0
    python_array = []
    with open("11input.txt") as f:
        lines = f.readlines()
    for line in lines:
        stripped_line = list(map(int,line.rstrip("\n")))
        python_array.append(stripped_line)
    game_state = np.array(python_array)
    print("Game Board ",0,":",sep='')
    pp.pprint(game_state)
    for i in range(100):
        new_game_state, step_flashes = executeStep(game_state,pp)
        game_state = new_game_state
        total_flashes += step_flashes
        print("Game Board ",i+1,":",sep='')
        pp.pprint(new_game_state)
    print("\n----Total Flashes:----\n   ",total_flashes,"\n")
