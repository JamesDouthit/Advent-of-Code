import re

if __name__ == "__main__":
    total_count = 0
    with open("8input.txt") as f:
        lines = f.readlines()
    for line in lines:
        x = re.search("^(.*) \| ([abcdefg ]*?)$", line)
        solver_split = x[1].split(" ")
        segment_dict = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[]}
        for word in solver_split:
            curr_len = len(word)
            for letter in word:
                segment_dict[letter].append(curr_len)
        # sorted_dict = {}
        # for segment, included in segment_dict.values():
        #     sorted_dict[segment] = included.sorted()
        solution_dict = {}
        for segment, included in segment_dict.items():
            if(sum(included)==43):
                solution_dict[segment] = 'A'
            elif(sum(included)==34):
                solution_dict[segment] = 'B'
            elif(sum(included)==38) and (2 not in included):
                solution_dict[segment] = 'C'
            elif(sum(included)==38) and (2 in included):
                solution_dict[segment] = 'D'
            elif(sum(included)==19):
                solution_dict[segment] = 'E'
            elif(sum(included)==44):
                solution_dict[segment] = 'F'
            elif(sum(included)==40):
                solution_dict[segment] = 'G'
            else:
                print("I think I messed up my soup:",sum(included))

        answer_split = x[2].split(" ")
        answer_list = []

        total_count += 1


    print(total_count)

