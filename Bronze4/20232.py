# Archivist

"""
2021/03/24 4:34 오후
정웅교
문제: https://www.acmicpc.net/problem/20232
"""
n = int(input())
if n == 1995 or n == 1998 or n == 1999 or n == 2001 or n == 2002 or n == 2003 or n == 2004 or n == 2005 or n == 2009 or n == 2010 or n == 2011 or n == 2012 or n == 2014 or n == 2015 or n == 2016 or n == 2017 or n == 2019:
    print('ITMO')
elif n == 2006:
    print('PetrSU, ITMO')
else:
    print('SPbSU')
