import sys
import pprint
sys.stdin = open('input_data/bj_2628.txt')


x, y = list(map(int, input().split())) #  x 가로 y 세로
num = int(input())
num = 1
paper = [[1 for i in range(x)] for n in range(y)]
pprint.pprint(paper)
print("")
print("")
papers = []
for i in range(num):
    spec = list(map(int, input().split()))

    if spec[0] == 0: # 가로   [세로][가로로]

        #pprint.pprint(paper[:spec[1]])
        #print("")
        #pprint.pprint(paper[spec[1]:])
        #for k in range(x):
        pprint.pprint(paper[:][:spec[1]])
   #elif spec[0] == 1: # 세로
   #     pprint.pprint(paper[spec[1]:])
   #     #paper_num *= 2



