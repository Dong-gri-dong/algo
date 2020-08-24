x, y = list(map(int, input().split()))

result = 0
count = 0

if x > y:
    x, y = y, x

for i in range(x, y+1):
    if i == 0:
        pass
    elif i % 3 == 0 or i % 5 == 0:
        result += i
        count += 1

print('sum : {}'.format(result))
if count == 0:
    print('avg : {}'.format(result))
else:
    print('avg : {}'.format(round(result / count, 1)))