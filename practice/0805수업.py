### 델타를 이용한 2차원 List 탐색
'''
arr =[
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,1,1,1,1]
]

dx=[0,0,-1,1]
dy=[-1,1,0,0]
result = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            textX = x+dx[i]
            textY = y+dy[i]
            if 0 <= textX < 5 and 0 <= textY < 5:
                result += abs(arr[x][y] - arr[textX][textY])
print(result)
'''

# 전치 행렬
'''
arr =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(arr) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''

'''
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)
print((1<<1))

print(3 & (1<<0))

for i in range(1<<n):  # 1<<n 의 의미는 총 부분집합의 갯수 부분집합의 갯수는 2^n 개
    for j in range(n+1): # 원소의 갯수만큼 범위를 지정해서 원소를 다 보기 위한것

        if i & (1<<j):
            #print(i & (1<<j))
            print(arr[j], end=", ")
        #print()
    print()
'''

arr = [3, 6, 7, 1, 5, 4]


for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j
        arr[i], arr[min] = arr[min], arr[i]
print(arr)
