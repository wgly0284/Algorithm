T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 당근 개수
    carrot = list(map(int, input().split()))
 
    cnt = 1
    max_cnt = -float('inf')
    for i in range(N-1):
        if carrot[i] < carrot[i+1]:  # 어떤 당근과 그 다음 당근 사이즈 비교 시 작다면
            cnt += 1    # 카운트 증가
        else:
            cnt = 1   # 아니면 1로 초기화
         
        if cnt > max_cnt:
            max_cnt = cnt
    print(f"#{tc} {max_cnt}")
                                