T = int(input())
for tc in range(1, T+1):
    # N: 마지막 정류장 번호, M: 정류장 개수, K:최대 이동 횟수
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
 
    is_charger = [0]*(N+1)
    for k in charger:
        is_charger[k] = 1  # 정류장 번호를 인덱스로 하는 위치에 = 1 표시
 
    # 한 번 충전했을 때 갈 수 있는 최대 길이 내에서
    # 충전기가 있으면 가장 가까운 충전기로 이동, 근데 왼쪽만 가능함
    charge_cnt = 0
    min_cnt = float('inf')
    i = 0  # 현재 위치
 
    while True:
        if i + K >= N:  # 마지막 정류장에 도달 또는 초과하면
            result = charge_cnt
            break
 
        i += K   # K만큼 이동
        for pi in range(i, i-K, -1):  # 거꾸로 보는 범위 내에서
            if 0 <= pi < N and is_charger[pi] == 1:   # 충전기가 있다면
                i = pi
                charge_cnt += 1
                break
        # 만약 없다면
        else:
            result = 0   # 0 출력하기
            break
    if result < min_cnt:
        min_cnt = result
 
    print(f"#{tc} {min_cnt}")