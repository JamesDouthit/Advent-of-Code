
if __name__ == "__main__":
    with open("1input.txt") as f:
        data = f.read()
    measurements_list = list(map(int,data.split("\n")))
    final_answer = 0
    for i in range(len(measurements_list)-3):
        if(sum(measurements_list[i:i+3])<sum(measurements_list[i+1:i+4])):
            final_answer += 1
    print(final_answer)
