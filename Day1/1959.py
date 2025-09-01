T = int(input())
 
def max_pair_sum(A, B):
    # A: 짧은 쪽, B: 긴 쪽이 되도록 함
    if len(A) > len(B):   # 만약 반대라면
        A, B = B, A   # 교체해버리자
    N, M = len(A), len(B)
     
    max_sum = -float('inf')   # 최댓값 초기화
    for i in range(M - N + 1):   # 길이 차 내에서 이동가능하도록 인덱스 정의
        temp_sum = 0   # 한 사이클 돌 때의 값 초기화
        for j in range(N):
            temp_sum += A[j] * B[i + j]   # 마주보는 숫자끼리 곱해서 더하기
        if max_sum < temp_sum:  # 최댓값 구하기
            max_sum = temp_sum
    return max_sum
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
     
    result = max_pair_sum(A, B)
    print(f"#{tc} {result}")