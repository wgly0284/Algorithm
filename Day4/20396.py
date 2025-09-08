T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N은 전체 돌의 개수, M은 뒤집기 횟수

    orig = list(input().split())  # 문자열 그대로 리스트로 밭기
    info = [list(map(int, input().split())) for _ in range(M)]
    # for _ in range(M):
    #     i, j = map(int, input().split())
    copy = orig  # 카피로 받아두기

    for k in range(len(info)):
        i, j = info[k][0], info[k][1]
        # info[k][0] -> i
        # info[k][1] -> j
        # info에서 받은 i번 -> orig[i]번부터 orig[i + j-1]까지 모두 orig[i]번이 되도록 구성
        for t in range(j):
            if 0 <= i - 1 + t < N:
                copy[i - 1 + t] = orig[i - 1]

    print(f"#{tc}", *copy)


'''
피드백
1) copy = orig << 이거 안하고 그냥 바꾸면 작동안하는가요 ???
  -> 안해도 바뀌네요! 불필요한 코드였던 것 같아요. 피드백 감사합니다!
2) 마지막줄 for t in range(j)면..  문제가 i부터 j개의 돌을 바꾸는 건데 range(j)로 하면 j번째 돌은 안바뀌는것 아닌가요???
  -> i번째를 포함해서 j번째이기 때문에 j번째는 포함 안되는 게 맞습니다.
   ex. 0110010101의 예제에서 i=5, j=3일 때 뒤집은 결과,
       5번째인 '0'을 포함해서 1, 0까지 모두 0으로 덮어써서 0110000101이 됨.
       j까지 포함하게 되면 1, 0 다음의 1까지 모두 바꾸게 되므로
       011000001 이 돼야 함.
'''