import re
import time

t0 = time.time()
for i in range(1000):
    if __name__ == "__main__":
        horiz = 0
        depth = 0
        with open("2input.txt") as f:
            data = f.read()
        commands_list = data.split("\n")
        for line in commands_list:
            x = line.split()
            x = re.search("^(.*) ([1-9]*?)$", line)
            if x[1] == "forward":
                horiz += int(x[2])
            elif x[1] == "down":
                depth += int(x[2])
            elif x[1] == "up":
                depth -= int(x[2])
            else:
                print("whoops, got something other than up/down/forw:",x[1])
        # print("answer is",horiz*depth,"from",horiz,depth)
t1 = time.time()

t2 = time.time()
for i in range(1000):
    if __name__ == "__main__":
        horiz = 0
        depth = 0
        with open("2input.txt") as f:
            data = f.read()
        commands_list = data.split("\n")
        for line in commands_list:
            x = line.split()
            # x = re.search("^(.*) ([1-9]*?)$", line)
            if x[0] == "forward":
                horiz += int(x[1])
            elif x[0] == "down":
                depth += int(x[1])
            elif x[0] == "up":
                depth -= int(x[1])
            else:
                print("whoops, got something other than up/down/forw:",x[1])
        # print("answer is",horiz*depth,"from",horiz,depth)
t3= time.time()

print("REGEX took this long!:",t1-t0)
print("SPLIT took this long!:",t3-t2)