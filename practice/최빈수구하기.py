import sys
sys.stdin = open("input_data/최빈수구하기.txt")

T = int(input())
T = 1

for test_case in range(1, T+1):
    _ = input()




















    scores = list(map(int, (input().split())))

    score = [0] * 101
    for i in scores:
         score[i] += 1


    max_value = 0
    max_index = 0
    for i in range(len(score)):

        if max_value <= score[i]:
            max_value = score[i]
            max_index = i
    print('#{} {}'.format(test_case, max_index))
