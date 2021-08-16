# 수열

"""
2021/08/16 12:41 오후
정웅교
문제: https://www.acmicpc.net/problem/2559
"""
n, k = map(int, input().split())
ls1 = list(map(int, input().split()))
ls = []
ls_res = []
sum = 0
for i in ls1:
    sum += i
    ls.append(sum)
left, right = 0, k
ls_res.append(ls[k - 1])
while right < len(ls):
    ls_res.append(ls[right] - ls[left])
    left += 1
    right += 1
print(max(ls_res))
