def solutionA(lines):
    n=len(lines)
    indexNumber=0
    seperator=''
    elfCal=0
    highestElfCal=0
    while indexNumber < n:
        elfCal=0
        while indexNumber < n:
            if seperator == lines[indexNumber]: 
                indexNumber += 1
                break
            elfCal=elfCal + int(lines[indexNumber])
            indexNumber += 1
        if elfCal > highestElfCal:  
                highestElfCal=elfCal
    return highestElfCal


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
    input_file_name = "input.txt"
  
    print("Loading data")
    lines = load_data(input_file_name)
  
    resultA = solutionA(lines)
    print(f"Solution for part A: {resultA}")

    resultB = solutionB(lines)
    print(f"Solution for part B: {resultB}")