import sys
from collections import deque
input = sys.stdin.readling

N = int(input())
queue = deque(map(int, input().split()))
stack = []
i = 1

while queue or stack:
    if queue and queue[0] == i:
        queue.popleft()
        i += 1

    elif stack and stack[-1]:
        stack.pop()
        i += 1

    elif queue:
        stack.append(queue.popleft)
    else:
        print('Sad')
        sys.exit(0)

print('Nice')

# from collections import deque
#
# N = int(input())
# numbers = list(map(int, input().split()))
# queue_num = deque([i for i in range(1, max(numbers) +1)])
# waiting = []
#
# for n in numbers:
#     # queue_num의 첫 값과 같다면,
#     # 그 첫 값을 없애자. 순회하면서 순서대로 돌 테니.
#     if n == queue_num[0]:
#         queue_num.popleft()
#     else:
#         waiting.append(n)
#
# result = ''
# while waiting:
#     check = waiting[-1]
#     if check == queue_num[0]:
#         queue_num.popleft()
#         waiting.pop()
#     else:
#         result = 'Sad'
#         break
#
#
# # while문을 빠져나왔다는 건, queue_num이 모두 처리됐다는 뜻
# if not waiting:
#     result = 'Nice'
#
# print(result)
'''
8 1 4 9 3 5 7 2 6
'''