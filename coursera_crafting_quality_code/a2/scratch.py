def return_str_fn(maze_list):
    str_list = ''
    for i in maze_list:
        str_list = str_list + str(i) + '\n'

    return str_list



maze_1 = return_str_fn([['#', '#', '#', '#', '#', '#', '#'],
                            ['#', '.', '.', '.', '.', '.', '#'],
                            ['#', '.', '#', '#', '#', '.', '#'],
                            ['#', '.', '.', '@', '#', '.', '#'],
                            ['#', '@', '#', '.', '@', '.', '#'],
                            ['#', '#', '#', '#', '#', '#', '#']
                            ])

print(maze_1)