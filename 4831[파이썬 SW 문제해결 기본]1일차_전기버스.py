import sys

sys.stdin = open('input_data/4831.txt')

T = int(input())


for t in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    # K: 갈수있는거리 N: 총 정류장 수 M: 충전기 설치 정류장 수
    charge_station = list(map(int, input().split()))

    bus = 0
    charge_count = 0
    while bus <= N:  # 버스의 위치가 N(총 정류장)이상이면 while문 탈출
        stop_charge = [] # 버스가 갈수있는 충전기 설치 정류장 수

        for i in range((bus+1), (bus+K+1)):  # 갈수 있는 정류장 수
            if (bus+K) >= N:
                bus = N
                break
            else:
                for charge in charge_station:
                    if i == charge:
                        stop_charge.append(charge)

        if stop_charge:
            bus = stop_charge[-1]
            charge_count += 1

        elif bus == N:
            break

        else:
            charge_count = 0
            break

    print('#{} {}'.format(t, charge_count))




# for t in range(1, T + 1):
#     K, N, M = list(map(int, input().split()))
#     # K: 갈수있는거리 N: 총 정류장 수 M: 충전기 설치 정류장 수
#     numbers = list(map(int, input().split()))
#     bus = 0
#     result = 0
#     while bus < N:
#         stop = []
#         for i in range((bus+1), (bus+K+1)):
#             if (bus+K+1) > N:
#                 bus = N
#                 break
#             else:
#                 for number in numbers:
#                     if i == number:
#                         stop.append(i)
#
#         if stop:
#             bus = stop[-1]
#             result += 1
#         elif bus == N:
#             break
#         else:
#             result = 0
#             break
#
#     print('#{} {}'.format(t, result))