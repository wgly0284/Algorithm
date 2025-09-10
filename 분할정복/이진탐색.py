def binary_search_check(arr, target):
    l, r = 0, len(arr) - 1  # 둘은 인덱스 값
    prev_dir = None
    while l <= r:
        m = (l + r) // 2  # 중간값 설정
        if arr[m] == target:
            return True
        elif arr[m] < target:  # 타겟값보다 작다면
            if prev_dir == 'R':  # 이전에 저장했던 값이 오른쪽이었다고 하면
                return False  # 유효하지 않다
            prev_dir = 'R'  # 해당하지 않는다면 R로 저장하고
            l = m + 1  # 그 다음 인덱스 탐색
        else:
            if prev_dir == 'L':  # 반대의 경우
                return False
            prev_dir = 'L'  # 왼쪽으로 저장하고
            r = m - 1  # 왼쪽으로 인덱스 이동하면서 탐색
    return False  # 다 돌았다는 건 못찾았다는 거니까 False


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()  # 정렬 안 되어있으면 정렬 필요

    count = 0
    for b in B:
        # 존재 여부를 이진 탐색으로 확인 후 방향 번갈아 선택 조건 판단
        # 먼저 존재 여부 판단 (binary_search_check 내에서 가능)
        # 만약 미리 존재 여부를 확인하려면 set 사용 가능하지만 메모리 고려 필요
        # 여기서는 조건 내에서 같이 처리하므로 따로 set 불필요
        if binary_search_check(A, b):
            count += 1
    print(f"#{tc} {count}")