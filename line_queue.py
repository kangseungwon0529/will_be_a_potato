#큐 초기화
size = 10
q = [0]*size
front = rear = -1

# 삽입연산
def enqueue(item):
    global rear
    #삽입을하기전에 큐가 가득찼는지 확인
    if isFull():
        print("Full")
        return
    rear += 1
    q[rear] = item

#삭제 연산
def dequeue():
    global front
    if isEmpty():
        print("empty")
        return -1
    else:
        front += 1
        return q[front]

#큐가 가득 찼는지 확인하는 연산
def isFull():
    return  rear == size-1

# 큐가 비어있는지 확인 하는 함수
def isEmpty():
    return front == rear

for i in range(10):
    enqueue(i)

print(q)
print(isEmpty())
print(isFull())


for i in range(10):
    print(dequeue(), end = " ")
print()

print(q)
print(isEmpty())
print(isFull())