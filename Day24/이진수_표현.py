t = int(input())
for tc in range(1, t+1):
    N,M = map(int, input().split())
    Nbit = (1<<N) - 1
    result = "OFF"

    if Nbit == (Nbit & M):
        result = 'ON'

    print(f"#{tc} {result}")s