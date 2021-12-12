import re

if __name__ == "__main__":
    horiz = 0
    depth = 0
    aim = 0
    with open("2input.txt") as f:
        data = f.read()
    commands_list = data.split("\n")
    for line in commands_list:
        x = re.search("^(.*) ([1-9]*?)$", line)
        if x[1] == "forward":
            horiz += int(x[2])
            depth += int(x[2])*aim
        elif x[1] == "down":
            aim += int(x[2])
        elif x[1] == "up":
            aim -= int(x[2])
        else:
            print("whoops, got something other than up/down/forw")
    print("answer is",horiz*depth,"from",horiz,depth)
