from collections import  deque
#데큐라고 쓰고 덱이라 읽는다.
q = deque()

q.append(1)
q.append(2)
q.append(3)
print(q.popleft())
print(q.popleft())
print(q.popleft())