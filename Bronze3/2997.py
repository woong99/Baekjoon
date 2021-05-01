# 네 번째 수

"""
2021/05/01 10:04 오후
정웅교
문제: https://www.acmicpc.net/problem/2997
"""

a, b, c = map(int, input().split())
ls = [a, b, c]
ls.sort()
diff1 = ls[1] - ls[0]
diff2 = ls[2] - ls[1]
if diff1 == diff2:
    print(ls[2] + min(diff1, diff2))
elif diff1 < diff2:
    print(ls[1] + diff1)
else:
    print(ls[0] + diff2)
