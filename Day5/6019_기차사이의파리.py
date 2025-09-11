# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    D,A,B,F = map(int, input().split())
    # D: 전면부 사이 거리, 즉 이동 거리, A: 기차 속력, B: 기차 속력, F: 파리 속력

    # 서로 마주보고 있고, 시작 전 거리는 D
    # 250 - (A + B) * time = 0이 되면 파리는 죽음

    time = D/(A + B)

    result = F * time

    print(f"#{tc} {result}")