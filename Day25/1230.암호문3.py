t = 10
for tc in range(1,11):

    N = int(input())
    dummy = list(map(int, input().split()))
    M = int(input())
    orders = list(input().split())

    '''
    I x,y,s: x번째 바로 다음에 y개 삽입. s는 덧붙일 암호문들.
    D x,y: x번째 바로 다음부터 y개 삭제.
    A y,s: 맨 뒤에 y개 덧붙이기.
    '''
    for i in range(len(orders)):
        if orders[i] == "I":
            x = int(orders[i+1])  # x번째 
            y = int(orders[i+2])  # y번째
            s = orders[i+3:i+3+y]
            rvsd_dummy = dummy[:x+1] + s + dummy[x+1:]
        elif orders[i] == "D":
            # 기존 데이터 삭제
            x = int(orders[i+1])
            y = int(orders[i+2])
            rvsd_dummy = dummy[:x] + dummy[x+y:]
        elif orders[i] == "A": 
            # 끝에 주어진 문자들 삽입
            y = int(orders[i+1])  # y번째
            s = orders[i+2:i+2+y]
            rvsd_dummy = dummy + s
        dummy = rvsd_dummy

    print(f"#{tc}", *dummy[1:11])