t = int(input())
for tc in range(1, t + 1):
    A, B, K = map(int, input().split())

    seen = {}

    for i in range(K):
        # A가 항상 작은 쪽, B가 항상 큰 쪽으로 정규화
        if A > B:
            A, B = B, A

        # A==0이면 변화 없음 → 바로 종료
        if A == 0:
            break

        state = (A, B)

        if state in seen:
            cycle_start = seen[state]
            cycle_len = i - cycle_start
            remaining = (K - i) % cycle_len
            for _ in range(remaining):
                if A > B:
                    A, B = B, A
                A, B = 2 * A, B - A
            break

        seen[state] = i
        A, B = 2 * A, B - A  # 항상 A가 작으니 A에게 A개를 줌

    print(f"#{tc} {min(A, B)}")
