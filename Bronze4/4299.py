# AFC 윔블던

"""
2021/03/02 6:07 오후
정웅교
문제: https://www.acmicpc.net/problem/4299
"""

a, b = map(int, input().split())
x = (a + b) // 2
y = (a - b) // 2
if (a + b) % 2 or b > a:
    print(-1)
else:
    print(max(x, y), min(x, y))
