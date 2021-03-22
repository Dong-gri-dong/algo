import sys

sys.stdin = open("input_data/11387.txt.txt")


T = int(input())

for test_case in range(1, T+1):

    D, L, N = map(int, input().split())
    # D(1 + nㆍL %)

    def damage(k, total):
        if k == N:
            print('#{} {}'.format(test_case, int(total)))
            return
        else:

            damage(k+1, total+D*(1+k*(L/100)))

    damage(0, 0.0)