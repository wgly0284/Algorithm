t = int(input())
for tc in range(1, t+1):
    A,B,C = map(int, input().split())
    ate_up = 0
    # 조건 만족 안되면 -1 출력하기
    # 모든 상자는 0이면 안됨
    # 사탕 수는 증가해야 함
    if A < 1 or B < 2 or C < 3:
        print(f"#{tc} -1")
        continue
    if B >= C:
        ate_up = 0
        ate_up += B-C+1
        B = C-1   # 한 칸 작게 설정해두고

    if A >= B:
        ate_up += A - B + 1
        A = B-1

    print(f"#{tc} {ate_up}")



'''
내 오답 코드: 그냥 C >=3 인 경우만 체크해서 일부 케이스 통과 못함

ate_up = -1 
if C >= 3: 
    if A<B<C: 
        ate_up = 0 
    if B >= C: 
        ate_up = B-C+1 
        B = C-1 # 한 칸 작게 설정해두고
'''