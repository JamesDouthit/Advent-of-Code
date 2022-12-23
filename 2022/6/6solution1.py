import time


def findMarker(buffer):
    m_set = set(buffer[0:4])
    if len(m_set) == 4:
        return 4
    
    for i in range(1,len(buffer)-3):
        m_set = set(buffer[i:i+4])
        if len(m_set) == 4:
            return i+4
    
    return -1

if __name__ == "__main__":
    start = time.time()

    with open("6input.txt") as f:
        data = f.read()
    line = data.split("\n")[0]

    answer = findMarker(line)

    end = time.time()

    print(answer)
    print("Calculated in " + str(end - start) + "s")
