t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 흰색 1번, 검은색 2번

    # 가로 검사
    avail = 0
    for i in range(N):
        cnt = 0
        for j in range(N):   # 가로 검사하면서
            if matrix[i][j] == 1:   # 흰색이면
                cnt += 1    # 카운트 증가
            else:   # 검은색 나왔다면
                if cnt == K:   # 이 때까지 센 숫자가 3일 때
                    avail += 1   # 3까지 개수인 avail 추가하고
                    cnt = 0    # 초기화
                cnt = 0
        if cnt == K:    # 끝열까지 검사하고 나왔는데 3이라면
            avail += 1   # 추가하자


    for j in range(N):
        cnt = 0
        for i in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    avail += 1
                    cnt = 0
                cnt = 0
        if cnt == K:
            avail += 1

    print(f"#{tc} {avail}")
