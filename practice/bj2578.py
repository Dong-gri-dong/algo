import sys
import pprint
sys.stdin = open('input_data/bj_2578.txt')


bingo = [[i for i in list(map(int, input().split()))] for n in range(5)]

go =[]
for i in range(5):
    go.extend(i for i in list(map(int, input().split())))

final = 0
count = 0

for i in range(len(go)):
    final += 1

    for k in range(len(bingo)):
        if go[i] in bingo[k]:
            idx_1 = k
            break
    idx_2 = bingo[idx_1].index(go[i])
    bingo[idx_1][idx_2] = 0

    sum_x = 0
    sum_y = 0
    sum_d1 = 0
    sum_d2 = 0

    sum_x = sum(bingo[idx_1])

    if idx_1 == idx_2:
        sum_d1 += bingo[0][0]
        sum_d1 += bingo[1][1]
        sum_d1 += bingo[2][2]
        sum_d1 += bingo[3][3]
        sum_d1 += bingo[4][4]
        if sum_d1 == 0:
            count += 1

    if idx_1 + idx_2 == 4:

        sum_d2 += bingo[0][4]
        sum_d2 += bingo[1][3]
        sum_d2 += bingo[2][2]
        sum_d2 += bingo[3][1]
        sum_d2 += bingo[4][0]
        if sum_d2 == 0:
            count += 1

    for n in range(5):
        sum_y += bingo[n][idx_2]

    if sum_y == 0:
        count += 1

    if  sum_x == 0:
        count += 1

    if count >= 3:
        break

print(final)
