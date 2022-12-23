import time


if __name__ == "__main__":
    start = time.time()

    with open("4input.txt") as f:
        lines = f.readlines()
    overlapped_lines = 0
    for line in lines:
        elves = line.split(",")
        elf_one = elves[0]
        elf_two = elves[1]
        elf_one_start = int(elf_one.split("-")[0])
        elf_one_end = int(elf_one.split("-")[1])
        elf_two_start = int(elf_two.split("-")[0])
        elf_two_end = int(elf_two.split("-")[1])
        elf_one_overlapped = \
            (elf_one_start >= elf_two_start \
            and elf_one_start <= elf_two_end) \
            or \
            (elf_one_end >= elf_two_start \
            and elf_one_end <= elf_two_end)
        elf_two_overlapped = \
            (elf_two_start >= elf_one_start \
            and elf_two_start <= elf_one_end) \
            or \
            (elf_two_end >= elf_one_start \
            and elf_two_end <= elf_one_end)
        if elf_one_overlapped or elf_two_overlapped:
            overlapped_lines += 1
    
    end = time.time()

    print(overlapped_lines)
    print("Calculated in " + str(end - start) + "s")
