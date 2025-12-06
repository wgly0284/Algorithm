from collections import deque

def BFS(start, end):

# 1. deque 선언
# 2. visited 설정
# 3. 첫 값 deque에 append
# 4. while문 조건 설정
# 5. 무한 돌기

    max_limit = 1000000
    visited = [0] * (max_limit + 1)   # 1차원만 체크
    queue = deque()
    queue.append((start, 0))   # 연산횟수 계속 돌아야 해서 함께 넣어주기
    visited[start] = 1

    while queue:   # queue 있는 동안 계속 탐색할 거임
        current, count = queue.popleft()
        if current == end:
            return count

        lst = [current +1, current -1, current -10, current *2]
        for nxt in lst:   # 차례로 꺼내보기
            if 1 <= nxt < max_limit and not visited[nxt]:
                visited[nxt] = 1
                queue.append((nxt, count + 1))
t = int(input())
for tc in range(1, t+1):
    N,M = map(int, input().split())
    result = BFS(N,M)

    print(f"#{tc} {result}")