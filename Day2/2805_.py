T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    cnt = 0

    for j in range(N):
        # N//2를 인덱스로 가지는 행에서는 전체 다 더한다.
        cnt += farm[N // 2][j]
        # +-1 행에서는 1부터 N-2 열까지 더한다.
        # +-2 행에서는 2부터 N-3 열까지 더한다.
        # ...
        # +-k 행애서는 k부터 N-1-k열까지 더한다.
        # k가 N//2가 될 때까지.
    for m in range(1, N // 2 + 1):  # N//2 포함해야 함.
        # 인덱스 작은 절반 행에 대해서
        for n in range(m, N - m):
            cnt += farm[N // 2 - m][n]
            # 인덱스 큰 절반 행에 대해서
            cnt += farm[N // 2 + m][n]

    print(f"#{tc} {cnt}")