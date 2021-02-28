# 타임 카

"""
2021/02/28 5:39 오후
정웅교
문제: https://www.acmicpc.net/problem/5575
"""
for i in range(3):
    fh, fm, fs, lh, lm, ls = map(int, input().split())
    first = (fm * 60) + (fh * 3600) + fs
    last = (lm * 60) + (lh * 3600) + ls
    time = last - first
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60
    print("%d %d %d" % (h, m, s))
