T = int(input())
for tc in range(1, T+1):
    orig = list(input())
    N = len(orig)  # 자릿수 파악
    
    # 구해야 하는 값: 몇 번 고치는가?
    # 조약돌? 문제랑 같네
    # 진행 방향 왼->오
    # 0000 -> 0011  1번
    # 100 -> 2번
    # i번째부터 끝까지 바뀜
    # 00000 -> 01010 이라면
    # i번째부터 +1
    # 그 다음 다른 수 나오면 +1
    # i번째와 i+1번째가 다르면 cnt += 1
    cnt = 0
    for i in range(N-1):
        if orig[i] != orig[i+1]:
            cnt += 1
            
    print(f"#{tc} {cnt}")