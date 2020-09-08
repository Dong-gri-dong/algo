import sys
sys.stdin = open("input_data/bj_1759")

L, C = map(int, input().split())
arr = list(input().split())

visit = [0] * C
arr = sorted(arr)

check= ['a', 'e', 'i', 'o', 'u']

def password(k, N, C,word):

    if len(word) == N:
        count = 0
        for i in word:
            if i in check:
                count += 1
        if  len(word)-2 >=count >= 1:
            result.append(word)
        return
    else:
        for i in range(k, C):
            if visit[i] == 0:
                visit[i] = 1
                password(i, N , C,word + arr[i])
                visit[i] = 0
result = []
password(0, L, C,'')
for i in result:
    print(i)
