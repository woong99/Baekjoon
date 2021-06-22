# 수 정렬하기 4

"""
2021/06/21 9:07 오후
정웅교
문제: https://www.acmicpc.net/problem/11931
"""
import sys

ls = []
for _ in range(int(sys.stdin.readline())):
    ls.append(int(sys.stdin.readline()))
ls.sort(reverse=True)
print(*ls, sep='\n')
