
if __name__ == "__main__":
    with open("2input.txt") as f:
        data = f.read()
    round_score_dict = {"AX":3,"BX":0,"CX":6, "AY":6,"BY":3,"CY":0, "AZ":0,"BZ":6,"CZ":3}
    move_choice_dict = {"AX":"Z","BX":"X","CX":"Y", "AY":"X","BY":"Y","CY":"Z", "AZ":"Y","BZ":"Z","CZ":"X"}
    correct_move = {}
    rounds_list = data.split("\n")
    score = 0
    for round in rounds_list:
        moves = round.split(" ")
        "X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win."
        moves[1] = move_choice_dict["".join(moves)]
        score += ord(moves[1])-87
        score += round_score_dict["".join(moves)]
    print(score)