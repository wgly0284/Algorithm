def dfs(current):
    if current > n:
        return
    
    dfs(current * 2)   # 왼쪽 자식 노드
    print(arr[current], end='')
    dfs(current * 2 + 1)  # 오른쪽 자식 노드
    
for tc in range(1, 11):
    print(f"#{tc} ", end='')
    
    n = int(input())
    arr = ['' for i in range(n+1)]
    for i in range(1, n+1):
        input_line = input().split()
        arr[i] = input_line[1]
        
    dfs(1)   # 항상 1부터 시작하는 완전 이진트리니까
    print()
    