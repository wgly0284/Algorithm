T = int(input())
for tc in range(1, T + 1):
    N = 9
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 정답이면 1 출력, 아닌 경우 0 출력
    # 가로 세로 작은 숫자가 모두 1~9까지 중복 없이 들어가야 함
    numbers = set([n for n in range(1, 10)])

    # 열 검사 후
    # 행 검사 후
    # 직은 사각형 검사하기

    # 행 검사

    result = 1
    for i in range(N):
        test1 = []
        for j in range(N):
            test1.append(grid[i][j])
        if set(test1) == numbers:
            continue
        else:
            result = 0
            break
    # 열 검사?
    for j in range(N):
        test2 = []
        for i in range(N):
            test2.append(grid[i][j])
        if set(test2) == numbers:
            continue
        else:
            result = 0
            break

    # 작은 사각형 검사
    for l in range(0, N, 3):
        for m in range(0, N, 3):
            test3 = []
            start = grid[l][m]
            for b in range(3):
                for bb in range(3):
                    test3.append(grid[l + b][m + bb])
            if set(test3) == numbers:
                continue
            else:
                result = 0
                break

    print(f"#{tc} {result}")