# from collections import deque
#
# def rsp(i, j, cards):
#     a = cards[i]
#     b = cards[j]
#
#     if a == b:
#         return i
#     if (a,b) in [(1,3), (2,1), (3,2)]:
#         return i
#     return j
#
# t = int(input())
# for tc in range(1, t+1):
#     N = int(input())
#     cards = list(map(int, input().split()))
#
#     candidates  =deque(range(N))
#     while len(candidates) > 1:
#         next_round = deque()
#
#         while len(candidates) >= 2:
#             i = candidates.popleft()
#             j = candidates.popleft()
#             winner = rsp(i, j, cards)
#             next_round.append(winner)
#         if candidates:
#             next_round.append(candidates.popleft())
#
#         candidates = next_round
#
#     winner_idx = candidates[0]
#
#     print(f"#{tc} {winner_idx+1}")


'''
문제를 보고 코드로 그대로 풀어내지 못해서, 내 머릿속에서 소설을 써서 코드를 만들어냈다.
분할정복 개념을 잊은지 오래됐지만, 문제 내에서 제시된 부분을 그대로 코드로 옮길 줄만 알았다면 쉽게 풀었을 문제.
이진트리, 분할정복과 관련된 내용이니 재숙지가 필요할 듯함.
'''


def rsp(i, j):
    # i, j는 학생 번호 (1-based index)
    # 같은 카드면 번호 작은 쪽 승
    if arr[i] == arr[j]:
        return i
    # 1: 가위, 2: 바위, 3: 보
    # 가위(1) vs 바위(2) vs 보(3) 규칙
    if arr[i] == 1:          # i: 가위
        if arr[j] == 2:      # 가위 vs 바위
            return j
        else:                # 가위 vs 보
            return i
    elif arr[i] == 2:        # i: 바위
        if arr[j] == 1:      # 바위 vs 가위
            return i
        else:                # 바위 vs 보
            return j
    else:                    # i: 보(3)
        if arr[j] == 1:      # 보 vs 가위
            return j
        else:                # 보 vs 바위
            return i

def tournament(s, e):
    # s, e는 구간의 시작/끝 인덱스 (1-based)
    if s == e:               # 한 명만 남으면 그 사람이 이 구간 승자
        return s
    mid = (s + e) // 2
    left = tournament(s, mid)
    right = tournament(mid + 1, e)
    return rsp(left, right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 인덱스를 1부터 쓰기 위해 앞에 더미 0 추가
    arr = [0] + list(map(int, input().split()))
    winner = tournament(1, N)
    print(f"#{tc} {winner}")
