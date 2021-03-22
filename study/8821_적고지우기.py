import sys
sys.stdin = open("input_data/8821_적고지우기")

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input()))


    temp = []
    for i in arr:
        if i in temp:
            temp.remove(i)
        else:
            temp.append(i)

    print("#{} {}".format(test_case, len(temp)))

