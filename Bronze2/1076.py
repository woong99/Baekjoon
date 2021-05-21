# 저항

"""
2021/05/21 1:15 오후
정웅교
문제: https://www.acmicpc.net/problem/1076
"""
dic = {'black': [0, 1], 'brown': [1, 10], 'red': [2, 100], 'orange': [3, 1000], 'yellow': [4, 10000],
       'green': [5, 100000], 'blue': [6, 1000000], 'violet': [7, 10000000], 'grey': [8, 100000000],
       'white': [9, 1000000000]}

a = str(input())
b = str(input())
c = str(input())
sum = ''
sum += str(dic.get(a)[0])
sum += str(dic.get(b)[0])
sum = int(sum)
sum *= dic.get(c)[1]
print(sum)
