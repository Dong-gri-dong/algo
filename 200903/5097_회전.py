import sys

sys.stdin = open("input_data/5097.txt")


from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Q = deque()



    data = list(map(int, (input().split())))

    for i in data:
        Q.append(i)

    for i in range(M):

        Q.append(Q.popleft())



    print('#{} {}'.format(test_case, Q[0]))