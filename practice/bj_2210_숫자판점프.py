import sys
sys.stdin = open("input_data/bj_2210")

arr = [list(map(int, input().split())) for _ in range(5)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def jump(k, y, x, value, result):
    if k == 5:
        result.add(value)
        return
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == 5 or ty < 0 or ty == 5:
                continue
            jump(k+1, ty, tx, value + arr[ty][tx]*(10**(6 - k)), result)
result = set()
for y in range(5):
    for x in range(5):
        jump(0, y,x, arr[y][x], result)
print(len(result))