# 그래프 활용 문제

'''
수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출함.
한 조의 인원에 제한이 없어서, 한 사람이 여러 장의 종이 제출 혹은 여러 사람이 한 사람 지목 가능.
1인 1조 가능.
출석 번호는 1~N까지, M장의 신청서가 있음.
몇 개의 조가 만들어지는가?

-> 그래프 방향 제한X
-> N은 노드, M은 화살표
'''

'''
1. deque 설정
2. visited 설정
3. 초기값 append
4. while queue 동안 하나씩 꺼내기: popleft()
'''
from collections import deque

t = int(input())
for tc in range(1, t+1):
    N,M = map(int, input().split())

    # 방향 표시하기(인접 리스트)
    arrows = [[]*(N+1) for _ in range(N+1)]

    # M개 만큼 주어지는 쌍
    info = list(map(int, input().split()))
    for n in range(0,2*M,2):
        s = info[n]
        e = info[n+1]
        arrows[s].append(e)
    # 짝수 인덱스는 s, 홀수 인덱스는 e
    # 입력 값을 쌍으로 info에 저장
    # print(arrows)

    '''
    1
    5 3
    1 2 2 3 4 5
    [[], [2], [3], [], [5], []]
    
    0,0은 버리는 값
    1 검사 후 값이 있다면, 그 값을 기준으로 또 검사 -> 공집합일 때까지.
    
    재귀함수?
    1. 종료 조건
    2. 반복 조건
    '''

    myq = deque()
    cnt = 0

    for i, mini_list in enumerate(arrows):
        if i == 0:
            continue
        myq.append((i, *mini_list))

    # print(myq)
    leftover = []

    temp = []
    while myq:
        current = myq.popleft()
        for nxt in myq:
            for num in current:
                if num in nxt:
                    current += nxt
                    myq.remove(nxt)
    print(leftover)
