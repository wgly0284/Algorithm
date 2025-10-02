t = int(input())
for tc in range(1, t+1):
    psr = [0] + list(input())

    # 15번째 경기까지 진행 시 자신이 이길 경우?
    # 가능성이 있다면 YES, 없다면 NO

    # 8번 이상 이길 가능성이 있는지 체크하기
    # 주어지는 값은 1이상 15 이하

    # 7 14 / 6 13 ...  차이는 7
    # 근데 지면
    # 7 15 / 6 15 ... 차이는 8 이상
    # 한 번 지면 8 14
    # 두 번 지면 8 13
    poss = 8  # 기회는 단 8번
    total = 15
    for i in range(1, len(psr)):
        if psr[i] == 'o':
            poss -= 1
            total -= 1
        else:
            total -= 1

    if poss <= total:   # 기회가 전체 남은 횟수보다 적으면 가능성 있음
        result = 'YES'
    else:
        result = 'NO'

    print(f"#{tc} {result}")