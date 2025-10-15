t = int(input())
for tc in range(1, t + 1):
    a, b, n = map(int, input().split())
    # x 저장된 값 A, y 저장된 값 B
    # x += y 혹은 y += x
    # x, y 둘 중 하나 이상에 저장된 값이 n 초과일 경우 그만
    # 최소 연산 횟수?

    cnt = 0
    min_cnt = 0
    while a <= n and b <= n:
        if a < b:
            a += b
            cnt += 1
        else:
            b += a
            cnt += 1

        if cnt > min_cnt:
            min_cnt = cnt

    print(min_cnt)
