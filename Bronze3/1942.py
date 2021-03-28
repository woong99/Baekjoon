# 디지털시계

"""
2021/03/28 12:15 오후
정웅교
문제: https://www.acmicpc.net/problem/1942
"""
a, b = (input().split())
c = "".join(a.split(':'))
d = "".join(b.split(':'))
n1 = int(c)
n2 = int(d)
ls1 = []
while n1 < 5960:
    if n1 == n2 + 1:
        break
    ls1.append(n1)
    n1 += 1

print(int(c))
print(int(d))
print(ls1)
