def integerize(my_str):
    return int(my_str)

def iterateDay(initial_state):
    final_state = initial_state[:]
    for i in range(len(initial_state)):
        if initial_state[i] == 0:
            final_state[i] = 6
            final_state.append(8)
        else:
            final_state[i] = initial_state[i] - 1
    return final_state

if __name__ == "__main__":
    with open("6input.txt") as f:
        data = f.readline()
    before = list(map(integerize,data.split(",")))
    for i in range(80):
        after = iterateDay(before)
        before = after
    print(len(after))
    print(after)