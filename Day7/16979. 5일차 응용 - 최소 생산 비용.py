# 모든 경우의 수를 다 보는 거니까 dfs를 선택
def find_cnt(i,cnt):
    global min_sum, visited
    if i == N:
        if min_sum > cnt:
            min_sum = cnt
        return
    if cnt >= min_sum:
        return

    for j in range(N):
        if not visited[j]:   # 선택된 적 없다면
            visited[j] = 1   # 선택 표시하고
            find_cnt(i+1,cnt + grid[i][j])   # 전체 카운트에 더해주기, 그리고 다음 이동
            visited[j] = 0    # 선택 표시한 건 근데 초기화 시켜줘야 함

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    visited = [0] * N

    find_cnt(0,0)

    print(f"#{tc} {min_sum}")

