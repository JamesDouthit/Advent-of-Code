def findCost(xpos,listpos):
    finalcost = 0
    for crabpos in listpos:
        dist = abs(crabpos-xpos)
        finalcost += ((1/2)*dist*(dist+1))
#     print("found cost",finalcost,"at",xpos)
    return finalcost

if __name__ == "__main__":
    with open("7input.txt") as f:
        data = f.readline()
    stripped = data.rstrip("\n").split(",")
    listed = list(map(int, stripped))
    listed.sort()
    list_of_costs = []
    for position in range(listed[-1]):
        list_of_costs.append(findCost(position,listed))
    print(min(list_of_costs))
