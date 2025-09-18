'''
정곤이는 자신이 엄청난 수학자임을 증명하기 위해,
어떤 규칙 만족하는 수를 찾아보기로 했다.
그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면
단조 증가하는 수이다.
예를 들어 111566, 233359는 단조 증가하는 수이고,
12343, 999888은 단조 증가하는 수가 아니다.
양의 정수 N 개 A1, …, AN이 주어진다.
 1 ≤ i < j ≤ N 인 두 i, j에 대해,
 Ai x Aj값이 단조 증가하는 수인 것들을 구하고
 그 중의 최댓값을 출력하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.
'''


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))   # 문자열로 받고 인덱스 맞추기
    max_num = -1
    for i in range(n-1):
        for j in range(i+1,n):
            my_num = numbers[i] * numbers[j]
            for p in range(len(str(my_num))-1):
                if str(my_num)[p] <= str(my_num)[p+1]:
                    continue
                else:
                    my_num = 0
                    break
            if my_num:
                if max_num < my_num:
                    max_num = my_num
                    # break하고 나왔다는 건 단조 증가가 아님

    print(f"#{tc} {max_num}")


