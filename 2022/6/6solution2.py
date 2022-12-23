import time


def findMarker(buffer, size):
    m_set = set(buffer[0:size])
    if len(m_set) == size:
        return size
    
    for i in range(1,len(buffer)-size+1):
        m_set = set(buffer[i:i+size])
        if len(m_set) == size:
            return i+size
    
    return -1

if __name__ == "__main__":
    start = time.time()

    with open("6input.txt") as f:
        data = f.read()
    line = data.split("\n")[0]

    answer = findMarker(line, 14)

    end = time.time()

    print(answer)
    print("Calculated in " + str(end - start) + "s")
