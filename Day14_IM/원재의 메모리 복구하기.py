t = int(input())
for tc in range(1, t + 1):
    orig = list(map(int, input()))  # 원래 상태, 문자열
    init = [0] * len(orig)  # 빈 문자열로 초기화
    cnt = 0

    for i in range(len(orig)):
        if orig[i] != init[i]:
            for j in range(i, len(orig)):
                init[j] = orig[i]
            cnt += 1
    print(f"#{tc} {cnt}")


"""
한 달 전에 푼 풀이는 도대체 무슨 말인지 이해하기가 어렵다...
위의 풀이는 메모리, 실행시간, 코드길이 모두 개선돼서 다행이다!
"""
