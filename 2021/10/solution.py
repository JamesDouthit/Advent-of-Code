
if __name__ == "__main__":
    final_answer = 0
    lookup_values = {')':3,']':57,'}':1197,'>':25137}
    lookup_opens = {')':'(',']':'[','}':'{','>':'<'}
    with open("10input.txt") as f:
        lines = f.readlines()
    for line in lines:
        stripped_line = list(line.rstrip("\n"))
        # The entries here represent, respectively, (paren), [bracket], {curly}, and <tick>
        opens_stack = []
        for char in stripped_line:
            if(char=='(' or char=='[' or char=='{' or char=='<'):
                opens_stack.append(char)
            elif(char==')' or char==']' or char=='}' or char=='>'):
                open = opens_stack.pop()
                if(open != lookup_opens[char]):
                    final_answer += lookup_values[char]
            else:
                print("I messed up my soup")

    print(final_answer)
