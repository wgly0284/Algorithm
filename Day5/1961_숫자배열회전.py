# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(input().split()) for _ in range(N)]    # 문자열로 받음

        #   90도, 180도, 270도
        #   열     행     열
# 시작점  N-1,0   N-1, N-1  0, N-1
    print(f"#{tc}")

    # 90도
    for j in range(N):
        row = ''
        for i in range(N):
            row += grid[N-1-i][j]
        row += ' '
        # 0, 1, 2, ... , N-1까지
        # 180도
        for n in range(N):
            row += grid[N-1-j][N-1-n]
        row += ' '

        # 270도
        for k in range(N):
            row += grid[k][N-1-j]
        row += ' '

        print(row)
