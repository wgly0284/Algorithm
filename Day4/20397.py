T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N은 전체 돌의 개수, M은 뒤집기 횟수

    orig = list(input().split())  # 문자열 그대로 리스트로 밭기
    info = [list(map(int, input().split())) for _ in range(M)]
    # for _ in range(M):
    #     i, j = map(int, input().split())
    # copy = orig  # 카피로 받아두기

    for k in range(len(info)):
        i, j = info[k][0], info[k][1]
        # info[k][0] -> i
        # info[k][1] -> j
        # info에서 받은 i번 -> 마주보는 j개의 돌에 대해
        # 즉, orig[i]번부터 orig[i + j-1], orig[i - j+1]까지
        # orig[i]번과 같으면 뒤집기
        # 아니면 그대로 두기
        for t in range(1, j + 1):
            rp, rm = i - 1 + t, i - 1 - t
            if 0 <= rp < N and 0 <= rm < N:  # 벜위 내에서
                if orig[rp] == orig[rm] == '1':  # 마주보는 두 돌이 모두 1이라면
                    orig[rp] = orig[rm] = '0'  # 뒤집어라
                elif orig[rp] == orig[rm] == '0':  # 모두 0이라면
                    # 뒤집어라
                    orig[rp] = orig[rm] = '1'
            else:  # 색이 다르다면
                break  # 중지

    print(f"#{tc}", *orig)


'''
뒤집는 걸 어떻게 표현할지 몰라서 1과 0인 경우로 일일이 나눴는데,
근영님의 코드를 보고 좋은 방법을 배웠다. (1-값)
다음에는 꼭 아래처럼 활용해봐야겠다.

if arr[m-step] == arr[m+step]:     # 마주보는 돌의 색이 같으면 뒤집기
    arr[m-step] = 1 - arr[m-step]
    arr[m+step] = 1 - arr[m+step]
    
'''