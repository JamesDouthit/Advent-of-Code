
if __name__ == "__main__":
    with open("1input.txt") as f:
        data = f.read()
    measurements_list = list(map(int,data.split("\n")))
    final_answer = 0
    for i in range(len(measurements_list)-1):
        if(measurements_list[i]<measurements_list[i+1]):
            final_answer += 1
    print(final_answer)
    