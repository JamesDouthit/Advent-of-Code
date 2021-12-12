
if __name__ == "__main__":
    final_scores = []
    lookup_scores = {')':1,']':2,'}':3,'>':4}
    lookup_opens = {')':'(',']':'[','}':'{','>':'<'}
    lookup_closes = {'(':')','[':']','{':'}','<':'>'}
    with open("10input.txt") as f:
        lines = f.readlines()
    for line in lines:
        running_score = 0
        should_include = True
        stripped_line = list(line.rstrip("\n"))
        opens_stack = []
        for char in stripped_line:
            if(char=='(' or char=='[' or char=='{' or char=='<'):
                opens_stack.append(char)
            elif(char==')' or char==']' or char=='}' or char=='>'):
                open = opens_stack.pop()
                if(open != lookup_opens[char]):
                    should_include = False
                    continue
            else:
                print("I messed up my soup")
        print(opens_stack)
        if(should_include):
            while opens_stack:
                open = opens_stack.pop()
                running_score *= 5
                running_score += lookup_scores[lookup_closes[open]]
            final_scores.append(running_score)
        
    print(sorted(final_scores)[int(len(final_scores)/2)])
