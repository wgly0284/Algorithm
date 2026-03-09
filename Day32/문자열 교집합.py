t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr1 = set(input().split())
    arr2 = set(input().split())

    print(f"#{tc} {len(arr1 & arr2)}")



    