import sys

sys.stdin = open("input_data/bj_2309")


arr = [int(input()) for _ in range(9)]


visit = [0] * 9

def ki(k, N, ki_list, ki_value):
    global result
    if ki_value > 100:
        return
    if result:
        return

    if k == 7:
        if ki_value == 100:
            result = ki_list
            return

    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                ki(k+1, N, ki_list+[arr[i]], ki_value+int(arr[i]))
                visit[i] = 0

result = 0
ki(0, 9, [], 0)
for i in sorted(result):
    print(i)