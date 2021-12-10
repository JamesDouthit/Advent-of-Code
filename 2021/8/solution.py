import re

if __name__ == "__main__":
    total_count = 0
    with open("8input.txt") as f:
        lines = f.readlines()
    for line in lines:
        x = re.search("^.* \| ([abcdefg ]*?)$", line)
        splitted = x[1].split(" ")
        for word in splitted:
            if len(word) == 7 or len(word) == 4 or len(word) == 3 or len(word) == 2:
                total_count += 1
    print(total_count)

