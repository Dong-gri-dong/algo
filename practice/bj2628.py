import sys

sys.stdin = open('input_data/bj_2628.txt')


x, y = list(map(int, input().split()))
num = int(input())

paper = [[1 for i in range(x)] for n in range(y)]
print(len(paper))

for i in range(num):
    spec = list(map(int, input().split()))
    print(spec)





