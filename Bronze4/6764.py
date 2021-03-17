# Sounds fishy!

"""
2021/03/17 8:17 오후
정웅교
문제: https://www.acmicpc.net/problem/6764
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b and b < c and c < d:
    print('Fish Rising')
elif d < c and c < b and b < a:
    print('Fish Diving')
elif a == b and b == c and c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')
