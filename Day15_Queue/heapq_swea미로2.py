import sys
sys.stdin = open('input.txt', 'r')

import heapq
T = 10

di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1, T+1):
    input()
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    si, sj = 1, 1
    heap = []
    heapq.heappush(heap, (si, sj))
    visited[si][sj] = 1
    result = 0
    while heap:
        ci, cj = heapq.heappop(heap)

        if maze[ci][cj] == 3:
            result = 1
            break
        for d in range(4):
            ti, tj = ci+di[d], cj+dj[d]
            if 0 <= ti < N and 0 <= tj < N:
                if not visited[ti][tj] and maze[ti][tj] != 1:
                    visited[ti][tj] = 1
                    heapq.heappush(heap, (ti, tj))

    print(f"#{tc} {result}")



'''
Queue 복습

[특징]
1. FIFO: 선입선출
2. heapq: 최소힙을 구현한 라이브러리. 우선순위 큐. 우선순위가 높은(작은 값) 항목을 항상 맨 앞에서 꺼낸다.
3. heap = [], heappush(heap, item), heappop(heap), heap[0]
4. deque과의 차이점: deque은 일반 큐로서, BFS와 슬라이딩 윈도우에서 사용하고 양방향 포인터임.
5. 여러 경로 중 비용이 가장 작은 경로부터 텀색할 때 적절함!
'''




