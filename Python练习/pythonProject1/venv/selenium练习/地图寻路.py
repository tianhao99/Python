import queue as que

def get_param():

    x = int(input())

    y = int(input())

    x1 = int(input())

    y1 = int(input())

    return {'x': x, 'y': y}, {'x': x1, 'y': y1}, [

        [0, 0, 1, 0],

        [0, 0, 0, 0],

        [0, 0, 1, 0],

        [0, 1, 0, 0],

        [0, 0, 0, 1],

        ]

def main():

    start, end, maze = get_param()

    width = len(maze[0])

    height = len(maze)

    looked = [[-1] * width for i in range(height)] # 标记节点是否已经走过，和已经走过的步数，-1表示没走过

    moves = [

    {'x': 0, 'y': -1},# 向上移动一位

    {'x': 1, 'y': 0},  # 向右移动一位

    {'x': 0, 'y': 1},  # 向下移动一位

    {'x': -1, 'y': 0}, # 向左移动一位

    ]

    looked[start['x']][start['y']] = 0
    q = que.Queue(width * height)
    q.put(start)

    flag = True # 跳出外层循环的标志

    while q.empty() is False and flag:

        current_node = q.get()

        for node in moves:

            # 边不越界

            x = current_node['x'] + node['x']

            y = current_node['y'] + node['y']

            # python 真够人性化的了

            # 先保证不越界，看是否走过，还要看看是否能走



            if (0 <= x < width) and (0 <= y < height) and (looked[y][x] == -1)  and (maze[y][x] == 0):

                looked[y][x] = looked[current_node['y']][current_node['x']] + 1 # 标记已经往前面走了一步

                q.put({'x': x, 'y': y})

            # if x == end['x'] and y == end['y']:
            #
            #      flag = False
            #
            #      break
            #
            # for i in range(height):
            #
            #     print(looked[i])

    return looked[end['x']][end['y']]

print(main())
