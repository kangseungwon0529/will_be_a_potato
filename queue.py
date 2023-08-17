def enQ(data):
    global  rear
    #if 문이 존재하지 않으면 아웃오브 레인지가 발생할 수 있음
    if rear == front -1:
        print("Q is Full")
    rear += 1
    Q[rear] = data

def deQ():
    global front
    if front == rear: # 비어있다면?
        print(("큐가 비어있어요"))
        return -1
    else:
        front += 1
        return Q[front]


Qsize = 10

Q = [0]*Qsize
front =rear = -1

enQ(1)
enQ(2)
print(deQ())
print(deQ())
# front += 1
# tmp = Q[front] # 이런식으로 진행되면 오류가 발생한다!
# print(tmp)
