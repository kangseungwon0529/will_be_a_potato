def enq(data):
    global rear
    if (rear+1)%size == front:
        print("cq is Full")
        (front+1)%size # 데이터가 오래되서 삭제해도 되면 앞의것을 밀어서 덮어씀
    rear = (rear+1) %size
    cq[rear] = data

def deq():
    global  front
    front = (front+1)%size
    return  cq[front]

size = 4
cq = [0] * size
front = 0
rear = 0

enq(1)
enq(2)

enq(3)

enq(4)
print(deq()) # deq가 적절히 이루어지지 않으면 가득찬 모습으로 나타남
print(deq())
enq(5)
