# 나는 학급회장이다

"""
2021/06/19 1:13 오전
정웅교
문제: https://www.acmicpc.net/problem/2456
"""
if __name__ == '__main__':
    N = int(input())
    arr1 = [0] * 3  # 후보마다 점수 합산 배열
    arr2 = [0] * 3  # 점수 같을 경우를 쉽게 파악하기 위해 선호도 점수를 제곱해서 합산한 배열

    for _ in range(N):
        x, y, z = map(int, input().split())
        # 후보마다 점수 더해주기
        arr1[0] += x
        arr1[1] += y
        arr1[2] += z
        # 제곱해서 더해주기
        arr2[0] += (x * x)
        arr2[1] += (y * y)
        arr2[2] += (z * z)

    max_value = max(arr1)
    if arr1.count(max_value) == 1:
        for i in range(len(arr1)):
            if arr1[i] == max_value:
                print(i + 1, max_value)
                break;
    else:
        pow_max_value = max(arr2)
        idx = 0
        for i in range(len(arr2)):
            if arr2[i] == pow_max_value:
                idx = i
                break;

        # 회장 선출 불가능한 경우
        if arr2.count(pow_max_value) > 1:
            print(0, arr1[idx])

        # 가능한 경우
        else:
            print(idx + 1, arr1[idx])
