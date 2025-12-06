def thing(p_message):
    rails = 3
    message = p_message
    n_message = ''
    n_message_grid = []

    for i in range(rails):
        n_message_grid.append([])

    for item in n_message_grid:
        for i in range(len(message)):
            item.append(' ')

    #there are rails number rows
    #there are len message number columns

    row = 0
    column = 0
    reset_column = 1
    gap = rails*2-2

    n_message_grid[row][column] = message[0]

    message = message[1:]
    option = 0

    for item in message:

        if row == 0 or row == rails-1:
            gap = rails*2-2

        else:
            if option == 0:
                gap = rails * 2 - 2 - row * 2
            else:
                gap = row * 2

            option += 1
            if option >= 2:
                option = 0

        column += gap

        if column > len(message):
            row += 1
            column = reset_column
            reset_column += 1
            option = 0

        n_message_grid[row][column] = item

    column = 0
    row = 0

    for column in range(len(message)+1):
        letter = ''
        row = 0
        for row in range(rails):
            if n_message_grid[row][column] != ' ':
                letter = n_message_grid[row][column]
                n_message += letter

    return n_message

text = input('Enter your message: ')
correct = 0
total = 0

if test(text) == text:
    correct += 1
else:
    total += 1