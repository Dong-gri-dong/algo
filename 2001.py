import sys

sys.stdin = open('input_data/2001.txt')

T = int(input())
T = 1
N, M = map(int, input().split())
for test_case in range(1, T+1):
    numbers = []
    for i in range(N):
        numbers.append(list(map(int, input().split())))
    
    for k in range
        for i in range(N-M):
            for n in range(N-M):
                print(sum(numbers[i][n:n+M]))

    