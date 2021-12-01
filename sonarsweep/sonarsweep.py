
previous = None
increases = 0
with open('input.txt') as input:
    for line in input:
        current = line.rstrip('\n')
        if previous is not None and int(current) > int(previous):
            increases += 1
        previous = current

print(increases)