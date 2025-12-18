from collections import deque

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())

    # 인접 리스트 (무방향 그래프)
    arrows = [[] for _ in range(N+1)]
    info = list(map(int, input().split()))
    for i in range(0, 2*M, 2):
        s = info[i]
        e = info[i+1]
        arrows[s].append(e)
        arrows[e].append(s)   # 양방향

    visited = [False] * (N+1)
    group_cnt = 0

    for start in range(1, N+1):
        if visited[start]:
            continue

        # start에서 BFS 시작 -> 하나의 연결 컴포넌트
        group_cnt += 1
        q = deque([start])
        visited[start] = True

        while q:
            cur = q.popleft()
            for nxt in arrows[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)

    print(f"#{tc} {group_cnt}")
