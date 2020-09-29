import numpy as np

# Time complexity - O(N + log N) = O(N)
def run(input):
    output = []
    for inputElement in input:
        output.append(inputElement * inputElement)
    return np.sort(output)

# Time complexity - O(N ^ 2)
def runInOnePass(input):
    output = []
    isFirstElement = True
    for inputElement in input:
        inputElementSquared = inputElement * inputElement
        if isFirstElement:
            output.append(inputElementSquared)
            isFirstElement = False
            continue
        if inputElementSquared == 0:
            output.insert(0, inputElementSquared)
        else:
            appendLastElementAsMax = True
            x = 0
            for outputElementSquared in output:
                if inputElementSquared > outputElementSquared:
                    x += 1
                    continue
                else:
                    output.insert(x, inputElementSquared)
                    appendLastElementAsMax = False
                    break
            if appendLastElementAsMax:
                output.append(inputElementSquared)
    return output