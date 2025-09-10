def cube_root_binary_search(N):
    start = 1
    end = 10 ** 6 + 1  # 10^6 ^ 3 = 10^18 이므로 충분한 범위 설정

    while start <= end:
        mid = (start + end) // 2
        cube = mid ** 3

        if cube == N:
            return mid
        elif cube < N:
            start = mid + 1
        else:
            end = mid - 1

    return -1  # 없으면 -1 반환


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = cube_root_binary_search(N)
    print(f"#{tc} {result}")