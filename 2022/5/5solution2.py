import time


def findIndex(lines):
    for i in range(len(lines)):
        stripped = lines[i].lstrip()
        if stripped[0] == "1":
            # Found the labels line!
            return i
        else:
            # This line is not the labels line
            continue

if __name__ == "__main__":
    start = time.time()

    answer = ""

    with open("5input.txt") as f:
        data = f.read()
    lines = data.split("\n")
    # map(lambda s: s.rstrip(), lines)
    # map(str.rstrip, lines)

    lb_index = findIndex(lines)
    if lb_index == -1 or lb_index == None:
        raise Exception("oops")
    
    stack_stacks = []
    initial_stacks_input = lines[:lb_index]
    instructions = lines[lb_index+2:]

    # Prime the stacks with the first row of items
    for i in range(int(lines[lb_index].rstrip()[-1])):
        if initial_stacks_input[-1][1+(4*i)] == " ":
            # If final item in stack is none, stack is empty
            stack_stacks.append( [] )
            continue
        stack_stacks.append([ initial_stacks_input[-1][1+(4*i)] ])

    # Add all the rest of the initial items to their stacks
    for init_line in initial_stacks_input[:-1][::-1]:
        for i in range(int(lines[lb_index].rstrip()[-1])):
            if init_line[1+(4*i)] == " ":
                # Nothing in this place of this stack
                continue
            # We're on stack i
            stack_stacks[i].append( init_line[1+(4*i)] )
    
    for instr in instructions:
        instr_pieces = instr.split(" ")
        to_move = []
        for i in range(int(instr_pieces[1])):
            to_move.append( stack_stacks[ int(instr_pieces[3]) -1 ].pop() )
        stack_stacks[ int(instr_pieces[5]) -1 ] += to_move[::-1]
    
    # Enumerate the answer
    for stack in stack_stacks:
        answer = answer + stack[-1]
    
    end = time.time()

    print(answer)
    print("Calculated in " + str(end - start) + "s")
