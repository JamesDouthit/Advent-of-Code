import time


if __name__ == "__main__":
    start = time.time()

    with open("4input.txt") as f:
        lines = f.readlines()
    encapsulated_lines = 0
    for line in lines:
        elves = line.split(",")
        elf_one = elves[0]
        elf_two = elves[1]
        elf_one_assignment_start = int(elf_one.split("-")[0])
        elf_one_assignment_end = int(elf_one.split("-")[1])
        elf_two_assignment_start = int(elf_two.split("-")[0])
        elf_two_assignment_end = int(elf_two.split("-")[1])
        elf_one_encapsulated = \
            (elf_one_assignment_start >= elf_two_assignment_start) \
            and (elf_one_assignment_end <= elf_two_assignment_end)
        elf_two_encapsulated = \
            (elf_two_assignment_start >= elf_one_assignment_start) \
            and (elf_two_assignment_end <= elf_one_assignment_end)
        if elf_one_encapsulated or elf_two_encapsulated:
            encapsulated_lines += 1
    
    end = time.time()

    print(encapsulated_lines)
    print("Calculated in " + str(end - start) + "s")
