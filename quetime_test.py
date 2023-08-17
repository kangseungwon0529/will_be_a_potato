import time
from  collections import  deque

n = 200000
start = time.time()

q1 = []
for i in range(n):
    q1.append(i)

for i in range(n):
    q1.pop(0)

end = time.time()
print(f"리스트 구현 큐 걸린시간 : {end-start:.5f}")