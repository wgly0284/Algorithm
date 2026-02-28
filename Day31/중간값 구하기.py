from heapq import heappush, heappop

t = int(input())
for tc in range(1, t+1):
    n, default = map(int, input().split())

    lower = [-default]  # 최대힙: 파이썬은 최소힙만 지원하므로
                        # 음수로 넣어서 최대힙처럼 사용
    upper = []          # 최소힙: 그대로 사용
    val_sum = 0

    for _ in range(n):
        a, b = map(int, input().split())

        # --- a 삽입 ---
        if a <= -lower[0]:       # a가 현재 중앙값보다 작으면
            heappush(lower, -a)  # lower에 넣기 (음수로!)
        else:                    # a가 현재 중앙값보다 크면
            heappush(upper, a)   # upper에 넣기

        # a 넣으면 lower와 upper 개수가 같아짐(짝수)
        # → lower로 1개 당겨서 홀수로 만들기
        if len(lower) <= len(upper):
            heappush(lower, -heappop(upper))

        # --- b 삽입 ---
        if b <= -lower[0]:
            heappush(lower, -b)
        else:
            heappush(upper, b)

        # b 넣으면 lower가 2개 많아짐
        # → upper로 1개 보내서 홀수로 만들기
        if len(lower) > len(upper) + 1:
            heappush(upper, -heappop(lower))

        # 이 시점에 lower[0]이 중앙값! (음수로 저장했으니 -를 붙여 복원)
        val_sum = (val_sum + (-lower[0])) % 20171109

    print(f"#{tc}", val_sum)