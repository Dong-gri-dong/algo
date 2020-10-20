import sys
sys.stdin = open("input_data/상호의배트필드.txt")

T = int(input())


dx = [0,  0, -1, 1]
dy = [-1, 1,  0, 0]

def tanks(tank, index, state):
    arrs[tank[0]][tank[1]] = '.'
    if 0 <= tank[0] + dy[index] < H and 0 <= tank[1] + dx[index] < W:
        if arrs[tank[0] + dy[index]][tank[1] + dx[index]] != '.':
            arrs[tank[0]][tank[1]] = state
            return
        tank[0] = tank[0] + dy[index]
        tank[1] = tank[1] + dx[index]
    arrs[tank[0]][tank[1]] = state


shoot_pass = ['.', '-']
shoot_state = ['^', 'v', '<', '>']

for test_case in range(1, T+1):
    u = 0
    H, W = map(int,input().split())
    arrs = [list(input()) for _ in range(H)]
    N = int(input())
    actions = list(input())

    for y in range(H):
        for x in range(W):
            if arrs[y][x] == '<':
                tank = [y,x]
                state = '<'
                break
            elif arrs[y][x] == '>':
                tank = [y,x]
                state = '>'
                break
            elif arrs[y][x] == '^':
                tank = [y,x]
                state = '^'
                break
            elif arrs[y][x] == 'v':
                tank = [y,x]
                state = 'v'
                break


    for action in actions:
        if action == 'U':
            state = '^'
            index = shoot_state.index(state)
            tanks(tank, index, state)

        elif action == 'D':
            state = 'v'
            index = shoot_state.index(state)
            tanks(tank, index, state)
        elif action == 'L':
            state = '<'
            index = shoot_state.index(state)
            tanks(tank, index, state)
        elif action == 'R':
            state = '>'
            index = shoot_state.index(state)
            tanks(tank, index, state)

        elif action == 'S':
            shoot = tank[:]
            index = shoot_state.index(state)

            if 0 <= shoot[0] + dy[index] < H and 0 <= shoot[1] + dx[index] < W:
                shoot[0] = shoot[0] + dy[index]
                shoot[1] = shoot[1] + dx[index]

            while 0 <= shoot[0] < H and 0 <= shoot[1] < W:
                if arrs[shoot[0]][shoot[1]] not in shoot_pass:
                    if arrs[shoot[0]][shoot[1]] == '*':
                        arrs[shoot[0]][shoot[1]] = '.'
                        break
                    else:
                        break
                else:
                    if 0 <= shoot[0] + dy[index] < H and 0 <= shoot[1] + dx[index] < W:
                        shoot[0] = shoot[0] + dy[index]
                        shoot[1] = shoot[1] + dx[index]
                    else:
                        break
    print('#{} '.format(test_case), end="")
    for i in arrs:
        sums = ''
        for j in i:
            sums += j
        print(sums)


















#
#
#
#
# for test_case in range(1, T+1):
#     u = 0
#     H, W = map(int,input().split())
#     arrs = [list(input()) for _ in range(H)]
#     N = int(input())
#     actions = list(input())
#
#
#     for y in range(H):
#         for x in range(W):
#             if arrs[y][x] == '<':
#                 tank = [y,x]
#                 state = '<'
#                 break
#             elif arrs[y][x] == '>':
#                 tank = [y,x]
#                 state = '>'
#                 break
#             elif arrs[y][x] == '^':
#                 tank = [y,x]
#                 state = '^'
#                 break
#             elif arrs[y][x] == 'v':
#                 tank = [y,x]
#                 state = 'v'
#                 break
#
#     shoot_pass = ['.', '-']
#     shoot_state = ['^', 'v', '<', '>']
#
#
#     for action in actions:
#         if action == 'U':
#             state = '^'
#             index = shoot_state.index(state)
#             arrs[tank[0]][tank[1]] = '.'
#             if 0 <= tank[0] + dy[index] < H and 0 <= tank[1] + dx[index] < W:
#                 if arrs[tank[0] + dy[index]][tank[1] + dx[index]] != '.':
#                     arrs[tank[0]][tank[1]] = state
#                     continue
#                 tank[0] = tank[0] + dy[index]
#                 tank[1] = tank[1] + dx[index]
#             arrs[tank[0]][tank[1]] = state
#         elif action == 'D':
#             state = 'v'
#             index = shoot_state.index(state)
#             arrs[tank[0]][tank[1]] = '.'
#             if 0 <= tank[0] + dy[index] < H and 0 <= tank[1] + dx[index] < W:
#                 if arrs[tank[0] + dy[index]][tank[1] + dx[index]] != '.':
#                     arrs[tank[0]][tank[1]] = state
#                     continue
#                 tank[0] = tank[0] + dy[index]
#                 tank[1] = tank[1] + dx[index]
#             arrs[tank[0]][tank[1]] = state
#         elif action == 'L':
#             state = '<'
#             index = shoot_state.index(state)
#             arrs[tank[0]][tank[1]] = '.'
#             if 0 <= tank[0] + dy[index] < H and 0 <= tank[1] + dx[index] < W:
#                 if arrs[tank[0] + dy[index]][tank[1] + dx[index]] != '.':
#                     arrs[tank[0]][tank[1]] = state
#                     continue
#                 tank[0] = tank[0] + dy[index]
#                 tank[1] = tank[1] + dx[index]
#             arrs[tank[0]][tank[1]] = state
#         elif action == 'R':
#             state = '>'
#             index = shoot_state.index(state)
#             arrs[tank[0]][tank[1]] = '.'
#             if 0 <= tank[0] + dy[index] < H and 0 <= tank[1] + dx[index] < W:
#                 if arrs[tank[0] + dy[index]][tank[1] + dx[index]] != '.':
#                     arrs[tank[0]][tank[1]] = state
#                     continue
#                 tank[0] = tank[0] + dy[index]
#                 tank[1] = tank[1] + dx[index]
#             arrs[tank[0]][tank[1]] = state
#
#         elif action == 'S':
#             shoot = tank[:]
#             index = shoot_state.index(state)
#             if 0 <= shoot[0] + dy[index] < H and 0 <= shoot[1] + dx[index] < W:
#                 shoot[0] = shoot[0] + dy[index]
#                 shoot[1] = shoot[1] + dx[index]
#
#             while 0 <= shoot[0] < H and 0 <= shoot[1] < W:
#                 if arrs[shoot[0]][shoot[1]] not in shoot_pass:
#                     if arrs[shoot[0]][shoot[1]] == '*':
#                         arrs[shoot[0]][shoot[1]] = '.'
#                         break
#                     else:
#                         break
#                 else:
#                     if 0 <= shoot[0] + dy[index] < H and 0 <= shoot[1] + dx[index] < W:
#                         shoot[0] = shoot[0] + dy[index]
#                         shoot[1] = shoot[1] + dx[index]
#                     else:
#                         break
#
#     print('#{} '.format(test_case), end="")
#     for i in arrs:
#         sums = ''
#         for j in i:
#             sums += j
#         print(sums)
