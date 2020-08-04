import sys

sys.stdin = open('input_data/bj_8979.txt')

num, rank = list(map(int, input().split()))

score = []
for i in range(num):
    scores = list(map(int, input().split()))
    score.append(scores)

### 0:금 1:은 2:동 ###
for idx, n in enumerate(score):
    if n[0] == rank:
        target_idx = idx


count = 0
for i in range(num):
    if score[target_idx][1] < score[i][1]:
        count+=1
    elif score[target_idx][1] == score[i][1]:
        if score[target_idx][2] < score[i][2]:
            count += 1
        elif score[target_idx][2] == score[i][2]:
            if score[target_idx][3] < score[i][3]:
                count += 1

print(count+1)