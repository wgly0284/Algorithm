# import sys
# from collections import deque
# input = sys.stdin.readline()

# 명령
'''
1 X: 정수 X를 스택에 넣음.
2: 스택에 정수가 있따면, 맨 위 정수 빼고 출력
3: 스택에 들어있는 정수 개수 출력
4: 스택이 비었다면 1, 아니면 0
5: 스택에 정수가 있다면 맨 위의 정수 출력. 없으면 -1.
'''

N = int(input())
# orders = []
stack = []

for _ in range(N):
    val = list(map(int, input().split()))
    # orders.append(val)

    if len(val) != 1 and val[0][0] == 1:   # 1이라면 무조건 정수 X를 스택에 넣는다
        stack.append[0][1]



'''[[4], [1, 3], [1, 5], [3], [2], [5], [2], [2], [5]]'''
