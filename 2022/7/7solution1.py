import time


def dictKeysFromList(in_list):
    keys_list = []
    for i in range(1,len(in_list)+1):
        keys_list.append("".join(in_list[:i]))
    return keys_list

if __name__ == "__main__":
    start = time.time()

    with open("7input.txt") as f:
        data = f.read()
    lines  = data.split("\n")
    totals_dict = dict()
    dirs_in_scope = []
    for line in lines:
        line_portion = line.split(" ")
        # Ignore ls and dir lines, irrelevant
        if (line_portion[0] == "$" and line_portion[1] == "ls") or line_portion[0] == "dir":
            continue
        # Each file adds its size to all dirs it's part of
        elif line_portion[0].isnumeric():
            for dir_key in dictKeysFromList(dirs_in_scope):
                dir_total = totals_dict.get(dir_key, 0)
                totals_dict[dir_key] = dir_total + int(line_portion[0])
        # This will segfault if it gets to here and the cmd is not cd
        # cd / means pop everything and push /
        elif line_portion[0] == "$" and line_portion[1] == "cd" and line_portion[2] == "/":
            dirs_in_scope = ["/"]
        # cd .. means pop stack
        elif line_portion[0] == "$" and line_portion[1] == "cd" and line_portion[2] == "..":
            dirs_in_scope.pop()
        # cd to a dir means push to stack
        elif line_portion[0] == "$" and line_portion[1] == "cd":
            dirs_in_scope.append(line_portion[2])

    sum = 0
    for v in totals_dict.values():
        if v <= 100000:
            sum += v
    
    end = time.time()

    print(sum)
    print("Calculated in " + str(end - start) + "s")
