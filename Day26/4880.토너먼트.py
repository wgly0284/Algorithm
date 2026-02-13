'''
1: 가위
2: 바위
3: 보

1과 3은 1
2와 3은 3
1과 2는 2

같은 카드라면 번호가 작은 쪽을 승자로(<=) 함.
'''

def rsp(x,y):
    x = min(x,y)
    y = max(x,y)
    if (x,y) == (1,3):
        return x
    elif (x,y) == (2,3):
        return y
    elif (x,y) == (1,2):
        return y

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    cards = list(map(int, input().split()))

    candidates = []

    while len(candidates) == 1:
        for i in range(0,2,N):
            result = rsp(cards[i], cards[i+1])
            candidates.append(result)
    print(f"#{tc} {candidates}")