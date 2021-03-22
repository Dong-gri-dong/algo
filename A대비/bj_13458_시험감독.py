import sys
sys.stdin = open("input_data/bj_13458_시험감독")

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total_viewers = 0
for i in A:
    i -= B
    if  i > 0:
        if i/C <= 1:
            total_viewers += 1 + 1
        else:
            if i/C == i//C:
                total_viewers += 1 + int(i/C)
            else:
                total_viewers += 1 + int(i / C) + 1

    else:
        total_viewers += 1

print(total_viewers)