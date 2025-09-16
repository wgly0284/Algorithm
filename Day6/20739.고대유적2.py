'''
땅속의 구조물을 촬영할 수 있는 특수 위성 카메라에 땅속에 묻힌 고대 구조물이 발견되었다.
구조물은 폭 1m, 길이 Xm의 직선 형태로 서로 평행 또는 직각으로만 자리하고 있어서,
  1mx1m의 해상도의 사진데이터에 구조물이 있는 자리는 1로 나타난다.
사진의 해상도는 NxM이며, 구조물이 있는 곳은 1, 빈 땅은 0으로 표시된다.
위 그림의 경우 가장 긴 구조물은 노란색으로 표시된 영역이며, 길이는 6이다.
교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조만 고려하면 된다.
평행한 모든 구조물은 서로 1m이상 떨어져 있어 빈칸으로 구분되며, 구조물의 최소 크기는 1x2m이다.
만약 다음과 같이 1x1m인 경우는 사진의 노이즈이다.
'''
T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    for i in range(N):
        cnt = 0
        for j in range(M):
            if grid[i][j] == 1:
                cnt += 1
                if cnt > 1:     # 문제에서 '1x1m인 경우는 사진의 노이즈'라고 했으니 1보다 큰 경우만 찾기
                    if max_len < cnt:
                        max_len = cnt
            else:
                cnt = 0   # 0으로 초기화


    for j in range(M):
        cnt = 0
        for i in range(N):
            if grid[i][j] == 1:
                cnt += 1
                if cnt > 1:   # 문제에서 '1x1m인 경우는 사진의 노이즈'라고 했으니 1보다 큰 경우만 찾기
                    if max_len < cnt:
                        max_len = cnt
            else:
                cnt = 0


    print(f"#{tc} {max_len}"



    '''
0 0 0 0 0 0 1 0
0 1 1 1 1 0 1 0
0 0 0 0 0 0 1 0
0 1 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0
'''