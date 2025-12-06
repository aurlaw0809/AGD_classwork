number = 20252025

for i in range(2000):
    if number % 2 == 0:
        number = 2 ** 2024 + int(number//2)
    else:
        number = number // 2 + 1
    print(number)

print(number)

#howdy