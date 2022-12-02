
if __name__ == "__main__":
    with open("1input.txt") as f:
        data = f.read()
    max_cals = 0
    elves_list = data.split("\n\n")
    for elf in elves_list:
        calories_list = list(map(int,elf.split("\n")))
        if max_cals < sum(calories_list):
            max_cals = sum(calories_list)

    print(max_cals)
