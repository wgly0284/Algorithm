import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bi_num = list(input())  # 이진법이라 문자열 그대로 받는데, 연속을 조회해야 하니까 인덱스를 써보자.

    # 연속 1의 개수 중 최댓값 구하기
    # 1이 나오면
    max_cnt = -1
    cnt = 0
    for i in range(N):
        if bi_num[i] == '1':
            cnt += 1
        elif bi_num[i] != '1':
            cnt = 0

        if max_cnt < cnt:
            max_cnt = cnt

    # 그 때부터 연속된 1의 개수를 세고
    # 0이 나오면
    # 초기화를 시키자
    print(f"#{tc} {max_cnt}")
