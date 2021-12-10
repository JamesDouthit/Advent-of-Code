
def isLowest(input_array,current_row,current_column,row_zero,row_max,column_zero,column_max):
    # if(input_array == None or current_row == None or current_column==None):
    #     return False
    # lowest_down, lowest_up, lowest_left, lowest_right = False
    lowest_down = False
    lowest_up = False
    lowest_left = False
    lowest_right = False
    if(row_zero):
        lowest_down = True
    else:
        lowest_down = bool(input_array[current_row][current_column]<input_array[current_row-1][current_column])
    if(row_max):
        lowest_up = True
    else:
        lowest_up = bool(input_array[current_row][current_column]<input_array[current_row+1][current_column])
    if(column_zero):
        lowest_left = True
    else:
        lowest_left = bool(input_array[current_row][current_column]<input_array[current_row][current_column-1])
    if(column_max):
        lowest_right = True
    else:
        lowest_right = bool(input_array[current_row][current_column]<input_array[current_row][current_column+1])
    return (lowest_right and lowest_left and lowest_up and lowest_down)

if __name__ == "__main__":
    final_answer = 0
    twoDarray = []
    with open("9input.txt") as f:
        lines = f.readlines()
    for line in lines:
        row = list(line.rstrip("\n"))
        mappedrow = list(map(int,row))
        twoDarray.append(mappedrow)
    # print("rows:",len(twoDarray),"columns:",len(twoDarray[0]))
    for row in range(len(twoDarray)):
        for column in range(len(twoDarray[0])):
            # print("args:",type(twoDarray),twoDarray[0][0:10],type(row),row,type(column),column,type(row==0),row==0,type(row==len(twoDarray)),row==len(twoDarray),type(column==0),column==0,type(column==len(twoDarray[0])),column==len(twoDarray[0]))
            if isLowest(twoDarray,row,column,row==0,row==len(twoDarray)-1,column==0,column==len(twoDarray[0])-1):
                final_answer += twoDarray[row][column] + 1
    print(final_answer)
