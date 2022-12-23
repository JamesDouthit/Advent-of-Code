import time


if __name__ == "__main__":
    start = time.time()

    with open("3input.txt") as f:
        data = f.read()
    sacks_list = data.split("\n")
    badge_list = []
    for i in range(0,len(sacks_list),3):
        # I assume there will only be complete groups of 3
        elf_a = set(sacks_list[i])
        elf_b = set(sacks_list[i+1])
        elf_c = set(sacks_list[i+2])
        badge = elf_a.intersection(elf_b.intersection(elf_c))
        badge_list.append(list(badge)[0])
    
    total_priority = 0
    for badge in badge_list:
        if badge.islower():
            total_priority += ord(badge)-96
        else:
            total_priority += ord(badge)-38

    end = time.time()

    print(total_priority)
    print("Calculated in " + str(end - start) + " s")
