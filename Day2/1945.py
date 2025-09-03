T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lst = [2,3,5,7,11]  # 총 다섯 개
    # 주어진 숫자를 리스트 속 숫자로 나누면서 카운트 증가?
    answer_lst = []

    for i in range(5):
        cnt = 0
        while N % lst[i] == 0:   # 인수가 없어질 때까지 나누면서
            cnt += 1    # 개수 세기
            N /= lst[i]   # N은 나눈 값으로 갱신
        answer_lst.append(cnt)   # 다 셌으면 리스트에 추가

    print(f"#{tc}", *answer_lst)

'''
피드백
리스트로 묶어서 하니깐 여러개 돌릴필요없이 깔끔하게 나오네요.
다음에 할땐 저도 저렇게 해봐야겠어요.
'''