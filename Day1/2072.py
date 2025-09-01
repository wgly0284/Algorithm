T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))  # 입력받기
     
    # 합 초기화
    sum = 0
     
    for num in numbers:
        # 홀수만 꺼내서
        if num % 2 != 0:
            # 더하기
            sum += num
             
    print(f"#{tc} {sum}")