import sys
sys.stdin = open("input_data/bj_10870_피보나치수5")

N = int(input())

def pibo(k):
    if k == 1:
        return 1
    if k == 0:
        return 0
    else:
        return pibo(k-1)+pibo(k-2)

print(pibo(N))

