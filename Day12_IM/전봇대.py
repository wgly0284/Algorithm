t = int(input())
for tc in range(1, t + 1):

    N = int(input())  # 전선 개수

    first = [0] * N
    second = [0] * N

    """
    처음 전선 기준으로
    1. 교차하는 경우
        2) 하강 교차인 경우
        3) 상승 교차인 경우
    2. 교차하지 않는 경우
    """

    for n in range(N):
        a, b = map(
            int, input().split()
        )  # 첫 번째 전봇대 높이 a cm, 두 번째 전봇대 높이 b cm
        first[n] = a
        second[n] = b

    cnt = 0
    for i in range(1, N):
        for j in range(i):
            # 하강 교차인 경우
            if first[i] > first[j] and second[i] < second[j]:
                cnt += 1
            # 상승 교차인 경우
            elif first[i] < first[j] and second[i] > second[j]:
                cnt += 1

    print(f"#{tc} {cnt}")


"""
접근방법은 옳았으나, if문마다 break 처리를 걸어 카운트가 제대로 되지 않았다.
아래는 원래 내가 작성했던 코드.

t = int(input())
for tc in range(1, t+1):

    N = int(input())  # 전선 개수

    first = [0] * N
    second = [0] * N


    
    # 처음 전선 기준으로
    # 1. 교차하는 경우
    #     2) 하강 교차인 경우
    #     3) 상승 교차인 경우
    # 2. 교차하지 않는 경우


    for n in range(N):
        a, b = map(int, input().split())  # 첫 번째 전봇대 높이 a cm, 두 번째 전봇대 높이 b cm
        first[n] = a
        second[n] = b

    cnt = 0
    for i in range(1, N):
        for j in range(i):
            # 하강 교차인 경우
            if first[i] > first[j]:
                if second[i] < second[j]:
                    cnt += 1
                    continue
                else:
                    break
            # 상승 교차인 경우
            if first[i] < first[j]:
                if second[i] > second[j]:
                    cnt += 1
                    continue

    print(f"#{tc} {cnt}")
"""
