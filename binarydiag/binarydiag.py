def inputAsList():
    return [line.rstrip() for line in open("input.txt")]


def computePowerConsumption():
    diags = inputAsList()
    gamma = ''
    epsilon = ''
    for i in range(len(diags[0])):
        zeros = 0
        ones = 0
        for diag in diags:
            if diag[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)

print("Part 1 Solution: %s" % computePowerConsumption())


def computeLifeSupportRating():
    diags = inputAsList()
    diagsO2 = diags.copy()
    diagsCo2 = diags.copy()
    for i in range(len(diags[0])):
        if len(diagsO2) == 1:
            break
        zeros = 0
        ones = 0
        for diag in diagsO2:
            if diag[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            diagsO2 = [x for x in diagsO2 if x[i] == '1']
        else:
            diagsO2 = [x for x in diagsO2 if x[i] == '0']

    for i in range(len(diags[0])):
        if len(diagsCo2) == 1:
            break
        zeros = 0
        ones = 0
        for diag in diagsCo2:
            if diag[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            diagsCo2 = [x for x in diagsCo2 if x[i] == '0']
        else:
            diagsCo2 = [x for x in diagsCo2 if x[i] == '1']
    return int(diagsO2[0],2) * int(diagsCo2[0],2)

print("Part 2 Solution: %s" % computeLifeSupportRating())

