import sys

sys.stdin = open('input_data/bj_2953.txt')

T = 5

rank = []
for t in range(T):
    rank.append(sum(list(map(int, input().split()))))

result = rank[0]
result_idx = 0
for idx, n in enumerate(rank):
    if result <= n:
        result = n
        result_idx = idx+1
count = 0
for i in rank:
    if result == i:
        count += 1

if count > 1:
    None

else:
    print(result_idx, result)