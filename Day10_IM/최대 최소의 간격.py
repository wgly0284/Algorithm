t = int(input())
for tc in range(1,t+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 작은 수는 가장 먼저 나오는 거, 큰 수는 가장 뒤에 나오는 거
    # 최댓값과 최솟값의 위치 차이 절대값으로 출력?
    max_idx = -1
    min_idx = -1

    max_num = max(numbers)
    min_num = min(numbers)

    for idx, number in enumerate(numbers):
        if number == max_num:
            max_idx = idx
    for idx, number in enumerate(numbers):
        if number == min_num:
            # 작은 것만 넣고 빠져야 함
            min_idx = idx
            break
    result = abs(max_idx - min_idx)
    print(f"#{tc} {result}")
