'''
지민이는 N마리의 소와 M마리의 말들을 키우고 있다.

 

각 가축들은 3차원 좌표 평면 상의 점으로 표현되는데, 특이하게도 지민이의 모든 소는 x=c1, y=0 직선 상에 존재하고, 지민이의 모든 말들은 x=c2, y=0 직선 상에 존재한다.

 

최근 삼성대학교의 연구 결과에 의하면, 두 소와 말이 가까이 있을 경우 엄청난 이산화탄소가 발생한다고 한다.

 

두 동물간의 거리는 맨하탄 거리로, P=(x1, y1, z1)와 Q=(x2, y2, z2) 간의 거리는 dist (P, Q) = |x2-x1 |+|y2-y1 |+|z2-z1 | 로 정의된다.

 

농부 지민이는 이 소식을 듣고, 농장을 분석하려고 한다.

 

지민이는 모든 소와 말 쌍에 대해서, 가장 가까운 쌍의 거리와, 이러한 최소 거리를 가지는 쌍의 개수를 알고 싶어한다.

 

지민이를 도와주자.

 


[입력]

 

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

 

각 테스트 케이스의 첫 번째 줄에는 소의 수 N, 말의 수 M이 주어진다. (1 ≤ N, M ≤ 500000)

 

그리고 각 테스트 케이스의 두 번째 줄에는 c1, c2가 주어진다. ( -108 ≤ c1, c2 ≤ 108)

 

세 번째 줄에는 N개의 정수로 소들의 위치가 주어진다.

 

입력은 z1, z2, z3, …, zN  의 형태이며, i번째 소는 (c1,0,zi) 에 위치함을 뜻한다. ( -108 ≤ zi ≤ 108)

 

네 번째 줄에는 M개의 정수로 말들의 위치가 주어진다.

 

입력은 z1, z2, z3, …, zM 의 형태이며, j번째 말은 (c2,0,zj) 에 위치함을 뜻한다. ( -108 ≤ zj ≤ 108)

 

각 테스트 케이스에 대해서, 소들의 위치와 말들의 위치는 서로 다르지만, 소와 말이 같은 위치에 있을 수는 있다.

 

 

[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

가장 가까운 소 쌍의 거리와, 그러한 거리를 가지는 소 쌍들의 개수를 공백으로 구분하여 출력하라.
'''


INF = 10**18

def lower_bound(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    c1, c2 = map(int, input().split())

    # 예: 소 z좌표 N개가 한 줄에 주어지는 경우
    cows = list(map(int, input().split()))
    # 예: 말 z좌표 M개가 한 줄에 주어지는 경우
    horses = list(map(int, input().split()))

    cows.sort()
    dx = abs(c1 - c2)

    # 1단계: 최소 맨해튼 거리 구하기
    min_dist = INF
    for hz in horses:
        idx = lower_bound(cows, hz)

        if idx < N:
            d = dx + abs(cows[idx] - hz)
            if d < min_dist:
                min_dist = d

        if idx > 0:
            d = dx + abs(cows[idx - 1] - hz)
            if d < min_dist:
                min_dist = d

    # 2단계: 그 최소 거리를 만드는 쌍의 개수 세기
    cnt = 0
    for hz in horses:
        idx = lower_bound(cows, hz)

        if idx < N:
            d = dx + abs(cows[idx] - hz)
            if d == min_dist:
                cnt += 1

        if idx > 0:
            d = dx + abs(cows[idx - 1] - hz)
            if d == min_dist:
                cnt += 1

    print(f"#{tc} {min_dist} {cnt}")
