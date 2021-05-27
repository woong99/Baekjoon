# FBI

"""
2021/05/27 12:36 오후
정웅교
문제: https://www.acmicpc.net/problem/2875
"""
cnt = 0
for i in range(1, 6):
    s = input()
    if s.find('FBI') != -1:
        print(i, end=' ')
        cnt += 1
if cnt == 0:
    print('HE GOT AWAY!')
