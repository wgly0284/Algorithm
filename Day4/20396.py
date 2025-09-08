T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N은 전체 돌의 개수, M은 뒤집기 횟수

    orig = list(input().split())  # 문자열 그대로 리스트로 밭기
    info = [list(map(int, input().split())) for _ in range(M)]
    # for _ in range(M):
    #     i, j = map(int, input().split())
    copy = orig  # 카피로 받아두기

    for k in range(len(info)):
        i, j = info[k][0], info[k][1]
        # info[k][0] -> i
        # info[k][1] -> j
        # info에서 받은 i번 -> orig[i]번부터 orig[i + j-1]까지 모두 orig[i]번이 되도록 구성
        for t in range(j):
            if 0 <= i - 1 + t < N:
                copy[i - 1 + t] = orig[i - 1]

    print(f"#{tc}", *copy)