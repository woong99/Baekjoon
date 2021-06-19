# 최대공약수와 최소공배수

"""
2021/06/20 12:16 오전
정웅교
문제: https://www.acmicpc.net/problem/2609
"""
import math

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))
