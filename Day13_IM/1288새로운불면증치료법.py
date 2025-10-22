t = int(input())
for tc in range(1, t+1):
    N = input()   # 문자열로 받기
    N_copy = N   # 처음엔 N을 문자열로 받아서 복사
    # N, 2N, 3N, ...
    appeared = set()
    check = {i for i in range(10)}

    while True:
        if appeared == check:
            break
        else:
            for n in str(N_copy):
                appeared.add(int(n))
        N_copy = int(N_copy)    # 숫자로 바꾼 N에다가
        N_copy += int(N)   # 값 더하기 -> 2N, 3N, ...
    result = int(N_copy)-int(N)
    print(f"#{tc} {result}")
