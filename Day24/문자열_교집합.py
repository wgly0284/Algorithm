t = int(input())
for tc in range(1, t+1):
    N = input()  # 문자열로 받음
    test_set = set()
    cnt = 0

    while len(test_set) < 10:
        cnt += 1
        temp = cnt*int(N)  # 숫자로 바꾸기
        for n in str(temp):
            test_set.add(n)
    print(f"#{tc} {cnt*int(N)}")


'''

# 강사님 코드

testcase = int(input())
total = (1 << 10) - 1

for i in range(1, testcase + 1):
    N = int(input())

    visited = 0
    count = 0
    while True:   # for i in range(0,100)도 가능하다.
        count += 1
        strNum = str(N * count)
        for c in strNum:
            num = int(c)
            visited |= (1 << num)

        if visited == total:
            break

    print(f'#{i} {N * count}')
'''

