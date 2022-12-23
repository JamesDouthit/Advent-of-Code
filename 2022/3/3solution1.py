import time


if __name__ == "__main__":
    start = time.time()

    with open("3input.txt") as f:
        data = f.read()
    sacks_list = data.split("\n")
    wrong_item_list = []
    for sack in sacks_list:
        cmptmt1 = set(sack[:int(len(sack)/2)])
        cmptmt2 = set(sack[int(len(sack)/2):])
        try:
            wrong_item_list.append(list(cmptmt1.intersection(cmptmt2))[0])
        except:
            print("Are these the same size bud?", len(cmptmt1), len(cmptmt2))
    
    total_priority = 0
    for wrong_item in wrong_item_list:
        if wrong_item.islower():
            total_priority += ord(wrong_item)-96
        else:
            total_priority += ord(wrong_item)-38

    end = time.time()

    # 16931

    print(total_priority)
    print("Calculated in " + str(end - start) + " s")
