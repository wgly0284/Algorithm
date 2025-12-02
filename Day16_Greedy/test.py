# Greedy

t = int(input())
for tc in range(1, t+1):
    N,M = map(int, input().split())

    total = 0
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)

    tare = list(map(int, input().split()))
    tare.sort(reverse=True)

    for w in range(N):
        for t in range(M):
            if weights[w] and tare[t] >= weights[w]:
                total += weights[w]
                tare[t] = 0
                weights[w] = 0
    print(f"#{tc} {total}")



