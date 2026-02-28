from heapq import heappush, heappop


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    my_heap = []  # heap 구조 설정

    cal = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        if len(cal[i]) == 2:
            heappush(my_heap, -cal[i][1])

        elif len(cal[i]) == 1:
            if my_heap:
                result.append(-heappop(my_heap))
            else:
                result.append(-1)

    print(f"#{tc}", *result)

    '''
    heap은 오름차순으로 정렬됨.
    heappop으로 최댓값을 꺼내고 싶다면, 음수로 넣어 최대 힙처럼 활용할 수 있다.
    
    -heaoppop
    heappush(heap, -x)
    '''