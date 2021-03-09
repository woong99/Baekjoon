# ソーシャルゲーム

"""
2021/03/09 5:30 오후
정웅교
문제: https://www.acmicpc.net/problem/16785
"""
a, b, c = map(int, input().split())
coin_cnt = 0
day_cnt = 0
while 1:
    coin_cnt += a
    day_cnt += 1
    if day_cnt % 7 == 0:
        coin_cnt += b
    if coin_cnt >= c:
        break
print(day_cnt)
