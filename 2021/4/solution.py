import numpy as np
import time

def unmarkedSumWinningBoard(winning_board,called_board):
    total_sum = 0
    for i in range(np.shape(called_board)[0]):
        for j in range(np.shape(called_board)[1]):
            if not bool(called_board[i,j]):
                total_sum += winning_board[i,j]
    return total_sum

def checkIfWinner(called_board):
    if sum(called_board.diagonal()) >= 5 or sum(np.fliplr(called_board).diagonal()) >= 5:
        return True
    for i in range(len(called_board)):
        if sum(called_board[i,:]) >= 5 or sum(called_board[:,i])>=5:
            return True
    return False

if __name__ == "__main__":
    with open("4input.txt") as f:
        lines = f.readlines()
    numbers_called = list(map(int,lines[0].rstrip("\n").split(",")))
    winning_number = -1
    unmarked_sum = -1
    boards = []
    called = []
    for i in range(1,len(lines)):
        curr_board = []
        if lines[i] == "\n":
            for j in range(1,6):
                curr_board.append(list(map(int,lines[i+j].rstrip("\n").rstrip().split())))
            boards.append(np.array(curr_board))
            called.append(np.zeros((5,5)))
    for called_number in numbers_called:
        if winning_number >= 0:
            break
        for k in range(len(boards)):
            for i in range(np.shape(boards[k])[0]):
                for j in range(np.shape(boards[k])[1]):
                    if boards[k][i,j] == called_number:
                        called[k][i,j] = 1
        for called_board_pos in range(len(called)):
            if checkIfWinner(called[called_board_pos]):
                winning_number = called_number
                unmarked_sum = unmarkedSumWinningBoard(boards[called_board_pos],called[called_board_pos])
                print("BOARD\n",called[called_board_pos],"WONNNNN!!!!N!!!!`````-`-`-`-`- ")
                break
    print(winning_number,unmarked_sum)
    print(winning_number*unmarked_sum)
    


# t0 = time.time()
# for run in range(1000):
#     with open("3input.txt") as f:
#         data = f.read()
#     diagnostic_list = data.split("\n")
#     mcb = [0 for n in range(len(diagnostic_list[0]))]
#     for line in diagnostic_list:
#         for i in range(len(line)):
#             if line[i] == "0":
#                 mcb[i] -=1
#             elif line[i] == "1":
#                 mcb[i] +=1
#             else:
#                 print("oops",line[i])
#     mcs = ""
#     lcs = ""
#     for b in range(len(mcb)):
#         if(mcb[b] >= 0):
#             mcb[b] = 1
#             mcs+="1"
#             lcs+="0"
#         else:
#             mcb[b] = 0
#             mcs+="0"
#             lcs+="1"
#     gamma = int(mcs,2)
#     epsilon = int(lcs,2)
#     # print(int(mcs,2)*int(lcs,2))
# t1 = time.time()
# print(t1-t0)
