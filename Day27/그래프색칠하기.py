# t = int(input())
# for tc in range(1, t+1):
#     N,E,M = map(int, input().split())
#
#     # 노드 정보 저장(인접행렬, 인접리스트)
#     info = [[] for _ in range(N)]  # 노드 개수 만큼 설정해야 함
#
#     for _ in range(E):
#         s, e = map(int, input().split())
#         info[s-1].append(e)
#         info[e-1].append(s)
#
#     '''
#     인접한 모든 노드 쌍에 대해, 서로 다른 색으로 칠하기 가능?
#
#     색칠 개수는 2,3,4 중 1
#
#     간선이 노드 개수보다 많으면, 2가지 색상 불가.
#     '''
#
#     result = 1
#     for i in range(N):
#         if len(info[i]) > M:
#             result = 0
#
#     print(f"#{tc} {result}")
#
#
#


def can_color(node):
    if node == N:
        return True  # 모든 정점 색칠 성공

    for c in range(1, M+1):    # 색 범위 내에서
        flag = True
        for nxt in info[node]:   # 연결된 노드 탐색
            if color[nxt-1] == c:    # 인접 정점과 색이 같으면 안 됨 (입력이 1-index라면 -1)
                flag = False
                break
        if not flag:
            continue

        color[node] = c
        if can_color(node+1):
            return True
        color[node] = 0  # 백트래킹

    return False

t = int(input())
for tc in range(1, t+1):
    N, E, M = map(int, input().split())
    info = [[] for _ in range(N)]
    for _ in range(E):
        s, e = map(int, input().split())
        info[s-1].append(e)
        info[e-1].append(s)

    color = [0]*N
    result = 1 if can_color(0) else 0
    print(f"#{tc} {result}")
