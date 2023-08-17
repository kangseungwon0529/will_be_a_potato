t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    ci = list(map(int,input().split()))
    arr = [0] * 100
    front = rear = -1
    after_init = ""
    for i in range(n):
        if rear == front:
            rear += 1
            arr[rear] = ci[i]
        elif rear == front-1 :
            after_init += str(ci[i])

    for j in after_init:
        for i in range(m):
            front += 1
            rear += 1

            if arr[front]//2 == 0:
                arr[rear] = int(j)
            elif arr[front]//2 !=0:

                arr[rear] = arr[front]//2




