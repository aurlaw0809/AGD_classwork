n = int(input())

num_powers = 0
valid = True
i = 0

while valid:
    if n/(2**i) > 1:
        num_powers += 1

print(num_powers)