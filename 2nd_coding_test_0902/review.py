'''
T: 테스트케이스 입력값
N, K_min, K_max: 공백과 함께 주어지는 직원 수, 팀 당 인원 최솟값, 팀 당 인원 최댓값
공백으로 구분되는 직원들의 점수
3개의 반으로 나누기
=> 당근 문제와 유사...
'''

'''
아래는 당근 코드 활용해서 대입한 것
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K_min, K_max = map(int, input().split())
    # N 학생 수, K_min 최소 인원, K_max 최대 인원

    scores = list(map(int, input().split()))
    scores.sort() 
    
    min_v = float('inf')
    
    for i in range(N-2):   # 팀은 3개여야 하니까 N-2까지만
        for j in range(i+1, N-1):  # i 다음 번째부터, 마지막 한 개 남은 때까지
            if scores[i] == scores[i+1]:  # 그런데 경계 부분에 같은 점수대 사람이 나뉘어졌다면
                continue   # 넘어가기
            if scores[j] == scores[j+1]:  # 그 다음 그룹에서도 마찬가지
                continue
            
            group1 = i + 1 # 0~i까지
            group2 = j - i  # i+1 ~ N-1까지
            group3 = N-(j+1)
            
            if group1 == 0 or group2 == 0 or group3 == 0:   # 그룹에는 한 사람 이상이 존재하며
                continue
            
            if min(group1, group2, group3) < K_min or max(group1, group2, group3) > K_max:
                # 주어진 최솟값, 최댓값의 조건을 만족하지 못한다면 넘어간다
                continue
            
            result = max(group1, group2, group3) - min(group1, group2, group3)
            min_v = min(min_v, result)
    if min_v == float('inf'):
        min_v = -1
        
    print(f"#{tc} {min_v}")