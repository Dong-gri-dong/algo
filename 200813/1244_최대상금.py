import sys
import pprint
sys.stdin = open('input_data/1244.txt')



T = int(input())

T = 1
for test_case in range(1, T + 1):


    n, k = list(map(int, input().split()))
    print(n)
    print(k)