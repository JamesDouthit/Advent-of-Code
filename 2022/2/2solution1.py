
if __name__ == "__main__":
    with open("2input.txt") as f:
        data = f.read()
    round_score_dict = {"AX":3,"BX":0,"CX":6, "AY":6,"BY":3,"CY":0, "AZ":0,"BZ":6,"CZ":3}
    rounds_list = data.split("\n")
    score = 0
    for round in rounds_list:
        moves = round.split(" ")
        score += ord(moves[1])-87
        score += round_score_dict["".join(moves)]
    print(score)