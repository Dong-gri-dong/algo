import sys
sys.stdin = open("input_data/이진수.txt")


T = int(input())

sixteen2bin={
    'A': 1010,
    'B': 1011,
    'C': 1100,
    'D': 1101,
    'E': 1110,
    'F': 1111,
}
for test_case in range(1, T+1):
    N, arr = input().split()


    result = ''
    for i in arr:
        if i in sixteen2bin:
            temp = sixteen2bin[i]
        else:
            temp = bin(int(i))[2:]
            while len(temp) < 4:
                temp = '0'+temp
        result += str(temp)

    print('#{} {}'.format(test_case, result))
