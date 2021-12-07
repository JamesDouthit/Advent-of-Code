import copy

def iterateDay(initial_state):
    final_state = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
    for age, number in initial_state.items():
        if int(age) == 0:
            final_state["6"] += number
            final_state["8"] += number
        else:
            final_state[str(int(age)-1)] += number
    return final_state

if __name__ == "__main__":
    with open("6input.txt") as f:
        data = f.readline()
    listed = data.rstrip("\n").split(",")
    before = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
    for fish in listed:
        before[str(fish)] += 1
    for i in range(256):
        after = iterateDay(before)
        before = after
    final_count = 0
    for population in after.values():
        final_count += population
    print(final_count)
    print(after)
