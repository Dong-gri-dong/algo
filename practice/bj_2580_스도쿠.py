import sys

sys.stdin = open('input_data/bj_2580')


arrs = [list(map(int, input().split())) for _ in range(9)]

for i in arrs:
    print(*i)


for i in range(9):
    if arrs[i].count(0) == 1:
        check = sorted(arrs[i])
        arrs[i].index(0)
        j = 0
        for n in range(9):
            if check[n] == j:
                j += 1
            else:
                arrs[i][arrs[i].index(0)] = j
                break
print()
for i in arrs:
    print(*i)



