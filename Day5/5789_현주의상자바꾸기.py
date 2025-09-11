# 2789
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * (N + 1)  # Q개만큼 깔아두기

    for i in range(1, Q + 1):  # Q번째 작업에 대해서
        L, R = map(int, input().split())  # 바꿀 상자 시작과 끝

        for k in range(L, R + 1):  # L과 R 모두 포함해서 바꿔야 함
            box[k] = i  # 그 사이 범위에 있는 박스 값들을 모두 i로 변경
    print(f"#{tc}", *box[1:])