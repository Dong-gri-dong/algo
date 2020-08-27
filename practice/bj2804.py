import sys

sys.stdin = open('input_data/bj_2804.txt')




word = list(input().split())

word[0], word[1] = word[1], word[0]



for i in word[0]:
    if i in word[1]:
        idx = i
        break




for i in range(M):
    for n in range(N):
        if i == int(word[1].index(idx)):
            print(word[0][n],end='')
        elif n == int(word[0].index(idx)):
            print(word[1][i], end='')
        else:
            print('.',end='')
    print('')
