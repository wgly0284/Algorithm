T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))   # 입력 받기
    N = 10   # 숫자는 10개로 고정
     
    sum = 0   # 합 초기화
 
    for num in numbers:  # 리스트 내 숫자 순회하면서
        sum += num   # 더하기
     
    average = round(sum/N)   # 소숫점 첫째에서 반올림
    print(f"#{tc} {average}")