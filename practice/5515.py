import sys
import pprint
sys.stdin = open('input_data/5515.txt')

T = int(input())

my_dict = {
    '0': 0,
    '1': 31, '2': 29,
    '3': 31, '4': 30,
    '5': 31, '6': 30,
    '7': 31, '8': 31,
    '9': 30, '10': 31,
    '11': 30, '12': 31,
}



for test_case in range(1, T+1):
    days = 4
    M, D = map(int, input().split())


    for i in range(0, M):
        days += my_dict[str(i)]
    days += D-1




    print('#{} {}'.format(test_case, days % 7))


