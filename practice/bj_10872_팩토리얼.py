import sys
sys.stdin = open("input_data/bj_10872_팩토리얼")

N = int(input())

def fac(k, result):
    global facs
    if k == N+1:
        facs = result
    else:
        fac(k+1, result * k)

facs = 0
fac(1, 1)
print(facs)