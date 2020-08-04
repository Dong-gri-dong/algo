import sys

sys.stdin = open('input_data/bj_2847.txt')

T = int(input())

rank = []
for t in range(T):
    rank.append((int(input())))

count = 0
for i in range(len(rank)-1, 0, -1):
    while rank[i] <= rank[i-1]:
        rank[i-1] -= 1
        count += 1

print(count)