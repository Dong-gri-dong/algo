import sys
import pprint
sys.stdin = open('input_data/bj_2615.txt')


omok = [[i for i in list(map(int, input().split()))] for n in range(19)]

pprint.pprint(omok)


for i in range(19):
    for n in range(19):
        if omok[i][n] != 0:





