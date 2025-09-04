T = int(input())
for tc in range(1, T+1):
    N = int(input())
    As = list(map(int, input().split()))   # 리스트로 받기
    # A1 ~ A4 중에 택 2, 곱한 수에 대해서
    # 두 수를 곱한 값은 어떻게 효율적으로 구할까? -> for문 안쓰고,,,, 다음에 고민해보기
 
    my_set = set()
    max_num = -1
    for i in range(N):
        for j in range(i+1, N):
            my_set.add(As[i] * As[j])
 
    # {70, 8, 40, 14, 20, 28}
    for num in my_set:    # 세트 속 숫자에서
        temp = num
        check = []   # 각 자릿수 저장할 리스트
        while temp > 0:   # 숫자가 0이 될 때까지
            check.append(temp % 10)   # 나머지로 각 자릿수 저장하기
            temp //= 10  # 몫으로 갱신하기
         
        check.reverse()
         
        valid = True
        for idx in range(len(check)-1):   # 구해둔 나머지 리스트에 대해서
            if check[idx] <= check[idx+1]:   # 내림차순이면 ok
                continue
            else:    # 아닌 경우
                valid = False
                break
        if valid:
            if max_num < num:   # if num >= 10 and max_num < num:
                max_num = num
 
    print(f"#{tc} {max_num}")
 