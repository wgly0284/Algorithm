import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K_min, K_max = map(int, input().split())
# N 학생 수, K_min 최소 인원, K_max 최대 인원

    scores = list(map(int, input().split()))
    scores.sort()   # 오름차순 정리
    score_set = list(set(scores))
    result = -1

    len_lst = []   # 각 원소별 개수 저장하기   (인접행렬 사용 가능한가?)
    for num in score_set:   # 원소 하나 꺼내서
        cnt = 0
        for i in range(N):   # 전체 점수 개수랑 비교해서
            if scores[i] == num:
                cnt += 1
        len_lst.append(cnt)

    # 최소/최대 길이가 주어진 조건을 만족한다면
    # if max(len_lst) <= K_max and min(len_lst) >= K_min:
    if len(score_set) == 3:
        if max(len_lst) <= K_max and min(len_lst) >= K_min:
            result = max(len_lst) - min(len_lst)
    elif len(score_set) > 3:   # 길이가 3보다 긴 경우,
        len_lst.sort()   # 다시 오름차순 정렬

        # 차례로 큰 값들 뽑기
        b1 = len_lst.pop()  # 길이 최댓값
        b2 = len_lst.pop()   # 두 번째 최댓값
        b3 = len_lst.pop()   # 세 번째 최댓값

        max_lst = [b3, b2, b1]   # 오름차순으로 저장
        i = 0
        while len_lst:  # 남은 리스트 값들 중에서
            max_lst[i] += len_lst.pop()  # 큰 값을 게중에서 작은 값에 더하기
            if i >= 3:
                i = 0
            i += 1

        if max(max_lst) <= K_max and min(max_lst) >= K_min:
            result = max(max_lst) - min(max_lst)
        else:   # 아니라면 불가능한 거임
            result = -1

    print(f"#{tc} {result}")
    
# -----------------------------------
# 지피티로 보완한 코드
        '''
        # Conter 사용법
        from collections import Counter

        data = ['a', 'b', 'a', 'c', 'b', 'a']
        counter = Counter(data)

        print(counter)
        
        # 출력
        Counter({'a': 3, 'b': 2, 'c': 1})

        '''
    '''    
    import sys
    sys.stdin = open("input.txt", "r")

    T = int(input())
    for tc in range(1, T+1):
        N, K_min, K_max = map(int, input().split())
        from collections import Counter

        scores.sort()
        score_set = list(set(scores))
        result = -1
        tc = 1  # 테스트 케이스 번호 예시

        len_lst = list(Counter(scores).values())

        if len(score_set) == 3:
            if max(len_lst) <= K_max and min(len_lst) >= K_min:
                result = max(len_lst) - min(len_lst)
        elif len(score_set) > 3:
            len_lst.sort()

            if len(len_lst) < 3:
                result = -1  # pop() 3번 못하니까
            else:
                b1 = len_lst.pop()
                b2 = len_lst.pop()
                b3 = len_lst.pop()
                max_lst = [b3, b2, b1]

                i = 0
                while len(len_lst) > 0:
                    max_lst[i] += len_lst.pop()
                    i = (i + 1) % 3

                if max(max_lst) <= K_max and min(max_lst) >= K_min:
                    result = max(max_lst) - min(max_lst)
                else:
                    result = -1

        print(f"#{tc} {result}")
    '''