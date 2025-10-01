t = int(input())
for tc in range(1, t+1):
    N = int(input())
    cards = list(input().split())

    result = []
    half = N//2
    if N%2 == 0:
        first_half = cards[:half]
        second_half = cards[half:]
    else:
        first_half = cards[:half+1]
        second_half = cards[half+1:]

    if len(first_half) >= len(second_half):
        for i in range(len(second_half)):
            result.append(first_half[i])
            result.append(second_half[i])
        if N % 2 != 0:
            result.append(first_half[-1])

    if len(first_half) < len(second_half):
        for i in range(len(first_half)):
            result.append(first_half[i])
            result.append(second_half[i])
        if N % 2 != 0:
            result.append(second_half[-1])

    print(f"#{tc}", *result)
