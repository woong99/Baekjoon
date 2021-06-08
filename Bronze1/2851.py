# 슈퍼 마리오

"""
2021/06/08 1:09 오후
정웅교
문제: https://www.acmicpc.net/problem/2851
"""
m = []
score = 0
for i in range(10):
    m.append(int(input()))
for j in m:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)
