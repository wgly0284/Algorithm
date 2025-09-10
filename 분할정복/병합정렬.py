def merge_sort(arr):
    global count
    if len(arr) <= 1:  # 요소 하나씩 길이가 1 이하가 되면 결과값 반환
        return arr

    mid = len(arr) // 2  # 절반으로 나누기
    left = merge_sort(arr[:mid])  # 앞 절반에 대한 재귀(병합)
    right = merge_sort(arr[mid:])  # 뒤 절반에 대한 재귀(병합)

    # 병합 전에 왼쪽 마지막 원소 > 오른쪽 마지막 원소
    if left[-1] > right[-1]:
        count += 1  # 카운트

    return merge(left, right)


def merge(left, right):
    n = len(left) + len(right)
    result = [0] * n  # 결과 리스트를 미리 생성
    i = j = k = 0  # i: left 인덱스, j: right 인덱스, k: result 인덱스

    # 두 배열을 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    # 남은 요소 복사
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1

    return result


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    sorted_arr = merge_sort(arr)

    print(f"#{t} {sorted_arr[N // 2]} {count}")
