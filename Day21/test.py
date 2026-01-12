import sys

arr = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
m = len(bomb)

for ch in arr:
    stack.append(ch)
    # 스택에 차곡차곡 쌓다가
    if len(stack) >= m:
        # 스택의 길이가 m 이상이 된 경우,
        if ''.join(stack[-m:]) == bomb:
            # 뒤에서 m길이까지 세어본 결과가 bomb오 같다면
            for _ in range(m):
                stack.pop()   # 없애버리자
# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')
