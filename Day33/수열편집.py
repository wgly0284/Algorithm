# 테스트 케이스 개수 입력
T_str = input()
if not T_str: # 빈 입력 예외 처리
    T = 0
else:
    T = int(T_str)

for tc in range(1, T + 1):
    # N: 수열 길이, M: 편집 횟수, L: 출력할 인덱스
    line1 = input().split()
    if not line1: continue
    N, M, L = map(int, line1)
    
    # 초기 수열 입력 (정수형 리스트로 변환)
    arr = list(map(int, input().split()))
    
    for _ in range(M):
        cmd = input().split()
        op = cmd[0]
        
        if op == 'I':
            # I {인덱스} {숫자}
            idx, val = int(cmd[1]), int(cmd[2])
            arr.insert(idx, val)
            
        elif op == 'D':
            # D {인덱스}
            idx = int(cmd[1])
            # 삭제할 인덱스가 현재 리스트 범위 내에 있을 때만 실행
            if 0 <= idx < len(arr):
                arr.pop(idx)
                
        elif op == 'C':
            # C {인덱스} {숫자}
            idx, val = int(cmd[1]), int(cmd[2])
            # 수정할 인덱스가 현재 리스트 범위 내에 있을 때만 실행
            if 0 <= idx < len(arr):
                arr[idx] = val 
                
    # 최종 결과 출력
    # L이 리스트의 마지막 인덱스보다 크면 -1 출력
    if 0 <= L < len(arr):
        print(f"#{tc} {arr[L]}")
    else:
        print(f"#{tc} -1")



'''
왜 이전 코드에서 에러가 났을까요?
인덱스 체크 시점: * result = arr[L] if arr[L] else -1 코드는 arr[L]의 값을 먼저 가져오려고 시도합니다.
만약 L이 10인데 리스트 길이가 5라면, 값을 가져오기도 전에 IndexError가 터져서 프로그램이 멈춰버립니다.

반드시 if L < len(arr): 처럼 인덱스 번호와 리스트의 길이를 먼저 비교해야 합니다.

데이터 타입 문제:

처음에 arr = list(input().split())으로 받으면 모든 요소가 문자열입니다.

하지만 명령어에서 추가하는 y는 int(orders[2])로 처리하셨죠? 이렇게 되면 리스트 안에 문자열과 정수가 섞이게 되어 나중에 예기치 못한 문제가 생길 수 있습니다. (전부 int로 통일하는 것이 안전합니다.)

수정(C) 명령어 오류:

기존 코드의 arr[x] = 8은 테스트 케이스의 예시 숫자가 고정된 것이니, 반드시 입력받은 변수 y를 넣어야 합니다.
'''