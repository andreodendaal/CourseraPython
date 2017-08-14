board_file = "board1.txt"

board_file = open(board_file, 'r')

board_list = []


for line in board_file:

    board_list_elem = []

    for counter, elem in enumerate(line.strip('\n')):
        board_list_elem.append(elem)

    print(board_list_elem)

    board_list.append(board_list_elem)

print(board_list)

board_file.close()




