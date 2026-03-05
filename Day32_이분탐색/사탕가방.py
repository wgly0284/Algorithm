t = int(input())
for tc in range(1, t+1):
    N,M = map(int, input().split())  # N 종류 사탕, M개의 사탕 나눠 넣기
    candies = list(map(int, input().split()))   # N개의 정수들(사탕들)

    # 최대 몇 개의 사탕 가방 만들 수 있는가?


    low = 1  # 이분 탐색 범위 설정

    high = sum(candies) // M   # 최대 가방 개수는 (사탕 총합 // M)

    result = 0

    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue

        # mid개 가방 만들 때, 가방 하나 당 담을 수 있는 사탕 총합    
        total_per_bag = 0

        for count in candies:
            total_per_bag += count // mid
        
        if total_per_bag >= M:
            result = mid
            low = mid + 1

        else:
            high = mid - 1

    print(f"#{tc} {result}")
