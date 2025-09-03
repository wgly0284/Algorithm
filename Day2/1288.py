T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []

    # 구하고자 하는 건 몇 번째 배수 즉 cnt?
    cnt = 0
    while True:
        if len(lst) == 10:   # 0~9까지 총 10개가 되면 종료
            break
        cnt += 1    # 1배수부터 시작
        strN = str(N * cnt)   # 문자열로 바꾸고
        for cha in strN:   # 각 자리 문자를 읽어서
            if cha not in lst:   # 리스트에 없으면
                lst.append(cha)   # 추가하기

    print(f"#{tc} {N * cnt}")