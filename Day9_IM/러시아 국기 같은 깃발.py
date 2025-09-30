# import sys
# sys.stdin = open('sample_input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    N,M = map(int, input().split())   # 열M, 행N
    colors = [list(input()) for _ in range(N)]

    min_cnt = float('inf')
    
    for w in range(N-2):
        for b in range(w+1, N-1):
            cnt = 0
            for i in range(w+1):
                for j in range(M):
                    if colors[i][j] != 'W':
                        cnt += 1
            for i in range(w+1, b+1):
                for j in range(M):
                    if colors[i][j] != 'B':
                        cnt += 1
            for i in range(b+1, N):
                for j in range(M):
                    if colors[i][j] != 'R':
                        cnt += 1
            if cnt < min_cnt:
                min_cnt = cnt
    print(f"#{tc} {min_cnt}")
    
    
    '''
    영역 설정까지는 했으나, 그 안에서 반복 도는 for문 설정을 안해서
    행 일부만 검사하는 코드로 작성했었음.
    구간을 먼저 잘라두고, 거기서 반복 돌면서 확인하기!!!!
    '''