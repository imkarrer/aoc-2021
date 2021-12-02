

def inputAsList():
    return open("input.txt").readlines()

def findPositionProductPt1():
    commands = inputAsList()
    horizontal = 0
    depth = 0
    for command in commands:
        amount = int(command.split(' ')[1])
        if command.startswith('down'):
            depth += amount
        elif command.startswith('up'):
            depth -= amount
        elif command.startswith('forward'):
            horizontal += amount
    return horizontal * depth

def findPositionProductPt2():
    commands = inputAsList()
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        amount = int(command.split(' ')[1])
        if command.startswith('down'):
            aim += amount
        elif command.startswith('up'):
            aim -= amount
        elif command.startswith('forward'):
            horizontal += amount
            depth += aim * amount
    return horizontal * depth


print("Part 1 Soultion: %s" % findPositionProductPt1())
print("Part 2 Soultion: %s" % findPositionProductPt2())
