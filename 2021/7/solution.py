def findCost(xpos,listpos):
    finalcost = 0
    for crabpos in listpos:
        finalcost += abs(crabpos-xpos)
#     print("found cost",finalcost,"at",xpos)
    return finalcost

def probe(xpos,cost,direction,listpos):
    if(findCost(xpos+direction,listpos)<cost):
        return probe(xpos+direction,findCost(xpos+direction,listpos),direction,listpos)
    else:
        return cost

if __name__ == "__main__":
    with open("7input.txt") as f:
        data = f.readline()
    stripped = data.rstrip("\n").split(",")
    listed = list(map(int, stripped))
    maxi = 0
    mini = 999
    for crab in listed:
        if(crab>maxi):
            maxi = crab
        if(crab<mini):
            mini = crab
    mid = int((maxi+mini)/2)
    print(min(probe(mid,findCost(mid,listed),-1,listed),probe(mid,findCost(mid,listed),1,listed)))
