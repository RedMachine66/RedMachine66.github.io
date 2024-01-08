def solutionA(lines):
    score=0
    
    # A for rock, B for paper, C for scissors
    # X for rock, Y for paper, Z for scissors

    for n in range(0,len(lines)):
        round=lines(n)
        if round.endswith('X'):
            score += 1
        elif round.endswith('Y'):
            score += 2
        elif round.endswith('Z'):
            score += 3

        if round == 'A Y' or 'B Z' or 'C X':
            score += 6
        elif round == 'A X' or 'B Y' or 'C Z':
            score += 3

    # stringlist = ''.join(lines)

    # my_rocks=stringlist.count('X')
    # my_papers=stringlist.count('Y')
    # my_scissors=stringlist.count('Z')

    # score += my_rocks
    # score += my_papers*2
    # score += my_scissors*3

    # win1 = lines.count('A Y')
    # win2 = lines.count('B Z')
    # win3 = lines.count('C X')
    # draw1 = lines.count('A X')
    # draw2 = lines.count('B Y')
    # draw3 = lines.count('C Z')

    # score += win1*6
    # score += win2*6
    # score += win3*6
    # score += draw1*3
    # score += draw2*3
    # score += draw3*3

    return score


def solutionB(lines):
    # TODO: replace with code solving the problem
    return -2 # Dummy result, deliberately wrong


# Helper function for loading the problem data
def load_data(fileName):
    with open(fileName, "r") as input_data:
        lines = input_data.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    return lines


if __name__ == "__main__":
    input_file_name = "dummy-input.txt"
    # TODO: Uncomment line below to use real input
    # input_file_name = "input.txt"
  
    print("Loading data")
    lines = load_data(input_file_name)
  
    resultA = solutionA(lines)
    print(f"Solution for part A: {resultA}")

    resultB = solutionB(lines)
    print(f"Solution for part B: {resultB}")