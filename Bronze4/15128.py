# Congruent Numbers

"""
2021/03/20 2:36 오후
정웅교
문제: https://www.acmicpc.net/problem/15128
"""
p_1, q_1, p_2, q_2 = map(int, input().split())
area = p_1 * p_2 / q_1 / q_2 / 2
if int(area) == area:
    print(1)
else:
    print(0)
