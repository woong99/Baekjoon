# 회전하는 큐

"""
2021/07/19 11:01 오전
정웅교
문제: https://www.acmicpc.net/problem/1021
"""

a, b = map(int, input().split())
ls1 = list(map(int, input().split()))
ls = [i for i in range(1, a + 1)]
cnt = 0
for i in ls1:
    if i == ls[0]:
        del (ls[0])
    else:
        if ls.index(i) > len(ls) // 2:
            while 1:
                ls.insert(0, ls[len(ls) - 1])
                del (ls[len(ls) - 1])
                cnt += 1
                if i == ls[0]:
                    del (ls[0])
                    break
        else:
            while 1:
                ls.append(ls[0])
                del (ls[0])
                cnt += 1
                if i == ls[0]:
                    del (ls[0])
                    break
print(cnt)
