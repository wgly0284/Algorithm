T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_len = -float('inf')
    # 행 검사
    for i in range(N):
        cnt = 0
        for j in range(M):
            if grid[i][j] == 1:   # 순회 돌면서 1 찾으면 카운트 증가
                cnt += 1
                if max_len < cnt:   # 값 찾으면 최댓값 갱신
                    max_len = cnt
            else:    # 아닌 경우, 0으로 초기화
                cnt = 0

    # 열 검사
    for j in range(M):
        cnt = 0
        for i in range(N):
            if grid[i][j] == 1:  # 순회 돌면서 1 찾으면 카운트 증가
                cnt += 1
                if max_len < cnt:   # 값 찾으면 최댓값 갱신
                    max_len = cnt
            else:     # 아닌 경우, 0으로 초기화
                cnt = 0
    print(f"#{tc} {max_len}")