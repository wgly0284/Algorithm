# 퀵 정렬
# 1. 피봇을 설정한다
# 2. 피봇 두 개 설정 후
# 3. 첫 번째 피봇보다
#   3-1. 큰 값이 나올 때까지 탐색 후,
#   3-2. 자리 바꾸기
# 4. 두 번째 피봇보다
#   4-1. 작은 값이 나올 때까지 거꾸로 탐색 후
#   4-2. 자리 바꾸기


# A: 정렬 대상 배열
# l, r: 시작 인덱스, 종료 인덱스
def quicksort(A, l, r):
    if l < r:  # 왼,오 구분이 있을 때만 진행할 수 있다.
        p = partition(A, l, r)

        quicksort(A, l, p - 1)  # 주어진 A에 대해
        quicksort(A, p + 1, r)


def partition(A, l, r):
    p = A[l]  # A의 가장 왼쪽에 있는 원소로 설정

    i = l  # 앞에서부터 찾는 인덱스. 피봇.
    j = r  # 뒤에서부터 찾는 인덱스. 피봇.

    while i <= j:  # 교차점까지만 찾을게
        while i <= j and A[i] <= p:  # 기준보다 작은 값을 찾을 때까지 인덱스 증가
            i += 1
        while i <= j and A[j] >= p:
            j -= 1  # j는 거꾸로 내려오니까 1씩 감소

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]  # while문을 빠져나왔으면 자리 바꾸기

    return j  # 기준 원소 위치는, 이미 교차가 됐으니 j로 해야 함함


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quicksort(numbers, 0, N - 1)
    print(f"#{tc} {numbers[N // 2]}")