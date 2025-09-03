T = int(input())
for tc in range(1, T + 1):
    orig = list(input())
    N = len(orig)  # 자릿수 파악

    # 구해야 하는 값: 몇 번 고치는가?
    # i번째와 i+1번째가 다르면 cnt += 1
    cnt = 0
    if orig[0] == '1':  # 첫 번째 숫자가 1이면 뒤집기 한 번 진행 후 카운트
        cnt = 1
    for i in range(N-1):
        if orig[i] != orig[i+1]:
            cnt += 1

    print(f"#{tc} {cnt}")
    
'''
4
0011
100
01001
0110001010

1
2
3
6
'''