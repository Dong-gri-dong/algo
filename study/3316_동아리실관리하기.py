import sys
sys.stdin = open("input_data/3316_동아리실관리하기.txt")

T = int(input())
T = 1
for test_case in range(1, T+1):
    arr = list(input())
    N = len(arr)
    people = ['A', 'B', 'C', 'D']

    def dongari(k, room):
        if k == N:
            return
        else:
            for i in range(0, 4):
                for j in range(0, 4):
                    if i == j:
                dongari(k+1, room)

