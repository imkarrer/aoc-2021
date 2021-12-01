
def findIncreases():
    previous = None
    increases = 0
    with open('input.txt') as input:
        for line in input:
            current = line.rstrip('\n')
            if previous is not None and int(current) > int(previous):
                increases += 1
            previous = current
    return increases


def findSlidingWindowIncreases():
    window = 3
    previousWindowSum = None
    increases = 0
    input_ = inputAsList()
    i = 0
    for item in input_:
        currentWindowSum = computeWindowSum(input_, i, window)
        if previousWindowSum is not None and currentWindowSum > previousWindowSum:
            increases += 1
        previousWindowSum = currentWindowSum
        i += 1
    return increases



def inputAsList():
   return [int(x) for x in open("input.txt").readlines()]

def computeWindowSum(input_, index, windowSize):
    if index < len(input_) - windowSize:
        lookAhead = index + windowSize
        windowSum = sum(input_[index:lookAhead:1])
    else:
        windowSum = sum(input_[index::1])
    return windowSum



print("Part 1 Solution: %s" % findIncreases())
print("Part 2 Solution: %s" % findSlidingWindowIncreases())