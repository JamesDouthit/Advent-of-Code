
if __name__ == "__main__":
    with open("1input.txt") as f:
        data = f.read()
    elves_list = data.split("\n\n")
    elf_calorie_list= []
    for elf in elves_list:
        calories_list = list(map(int,elf.split("\n")))
        elf_calorie_list.append(sum(calories_list))

    elf_calorie_list.sort()

    # print(elf_calorie_list)
    print(sum( [elf_calorie_list[-1], elf_calorie_list[-2], elf_calorie_list[-3]] ))
