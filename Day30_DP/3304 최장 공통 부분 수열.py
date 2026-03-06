T = int(input())

for tc in range(1, T + 1):
    # 두 문자열 입력 받기
    s1, s2 = input().split()
    
    n = len(s1)
    m = len(s2)
    
    # LCS 길이를 저장할 2차원 테이블 (0으로 초기화)
    # 행은 s1의 길이+1, 열은 s2의 길이+1 만큼 생성
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # s1의 각 문자를 하나씩 확인 (i)
    for i in range(1, n + 1):
        # s2의 각 문자를 하나씩 확인 (j)
        for j in range(1, m + 1):
            # 두 문자가 같다면? 이전까지의 결과(대각선 왼쪽 위)에 +1
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # 두 문자가 다르다면? 왼쪽 혹은 위쪽 값 중 더 큰 값을 가져옴
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]

    print(f"#{tc} {dp[n][m]}")