T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 학생 수 N, 학생의 번호 K
     
    # scores = [list(map(int,input().split())) for _ in range(N)]
     
    grade_lst = []
    for _ in range(N):
        mid, last, ass = map(int, input().split())
        # 중간, 기말, 과제 점수 입력 받기
        grade = 0.35*mid + 0.45*last + 0.2*ass
        grade_lst.append(grade)
     
    student = grade_lst[K-1]   # 평점 저장한 후
    new_lst = sorted(grade_lst, reverse=True)  # 오름차순으로 배열
    # 10%만 같은 평점 받을 수 있음
    limit = int(round(N*0.1))
     
    if student in new_lst[0:limit]:   # 상위 10%
        result = 'A+'
    elif student in new_lst[limit:2*limit]:  # 10~ 20%
        result = 'A0'
    elif student in new_lst[2*limit:3*limit]:  # 20~30%
        result = 'A-'
    elif student in new_lst[3*limit:4*limit]:  # ...
        result = 'B+'       
    elif student in new_lst[4*limit:5*limit]:
        result = 'B0'       
    elif student in new_lst[5*limit:6*limit]:
        result = 'B-'
    elif student in new_lst[6*limit:7*limit]:
        result = 'C+'
    elif student in new_lst[7*limit:8*limit]:
        result = 'C0'
    elif student in new_lst[8*limit:9*limit]:
        result = 'C-'
    else:
        result = 'D0'
         
 
    print(f"#{tc} {result}")