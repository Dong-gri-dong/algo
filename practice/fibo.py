def fibo1(n):
    global memo

    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))

    return memo[n]

memo = [0,1]





def fibo2(n):
    f =[0,1]

    for i in range(2, n+1):
        f.append(f[i-1]+ f[i-2])
    return f[n]

def fibo(n):
    if n< 2:
        return n


    else:
        return fibo(n-1) + fibo(n-2)


def second(n):
    if n < 2:
        return n

    else:
        return second(n-1) + second(n-2)

print(second(30))

# c=30
# print(fibo2(c))
# print(fibo1(c))
# print(fibo(c))