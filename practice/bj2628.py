import sys
import pprint
sys.stdin = open('input_data/bj_2628.txt')


a, b = list(map(int, input().split())) #  x 가로 y 세로
num = int(input())


#paper = [[1]* x for _ in range(y)]
c = []
d = []

for i in range(num):
    select, n = map(int, input().split())
    # 세로
    if select:
        c.append(n)
    # 가로
    else:
        d.append(n)
c.sort(reverse=True) # a
d.sort(reverse=True) # b

print(c)
print(d)

x = []
y = []

for i in c:
     x.append(a - i)
     a = i
x.append(a)

for i in d:
     y.append(b - i)
     b = i
y.append(b)


print(max(x)*max(y))



