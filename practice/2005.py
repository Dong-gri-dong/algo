import sys

sys.stdin = open('input_data/2005.txt')

T = int(input())
result = ''




for i in range(1, T+1):
    num = int(input())
    
    print('#{}'.format(i))
    a = [1]
    for n in range(num):
        result = ''
        c = []
        if n == 0:
            result += '1'
        
        else:

            a.append(0)

            for n in range(0, len(a)):
                if n == 0:
                    c.append(a[n])

                else:
                    c.append(a[n]+a[n-1])

            a = c[:]
            
            for i in a:
                result += '{} '.format(str(i))
        print(result)


    #print(result)