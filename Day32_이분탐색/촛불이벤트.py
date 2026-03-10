def find_max_k(n):
    left, right = 1, n
    max_k = 0
    while left <= right:
        mid = (left + right) // 2
        total = mid * (mid + 1) // 2
        if total <= n:   # mid단이 N개 이하면
            max_k = mid   # 가능한 수준이라고 기록
            left = mid + 1   # 더 큰 단수도 확인해보기(right)
        else:
            right = mid - 1   # 작은 단수로 줄여서 다시 확인(left)
    if max_k * (max_k + 1) // 2 == n:   # 정확히 딱 맞는지 확인
        return max_k   # 맞으면 max_k 출력
    return -1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    k = find_max_k(N)
    print(f"#{t} {k}")
