import sys

sys.stdin = open('input_data/bj_2851.txt')

T = 10
mario=[]
for t in range(1, T + 1):
    super = int(input())
    mario.append(super)


result = 0
for i in mario:
    new_result = result + i

    if abs(100-result) >= abs(100-new_result):
        result = new_result
    else:
        break
print(result)



