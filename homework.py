t = 10
for _ in range(1,t+1):
    tc = int(input())
    numbers = list(map(int,input().split()))
    arr = [0]*100000
    front = rear = -1
    for i in range(8):
        rear += 1
        arr[rear] = numbers[i]


    num = 1
    for i in range(len(arr)):
        front += 1
        rear += 1
        arr[rear] = arr[front]-num
        num += 1
        if arr[rear] <= 0:
            arr[rear] = 0
            break
        elif num>5:
            num = 1
    result = ""
    for i in range(8):
        result += str(arr[rear-7+i])+ " "

    print(f"#{tc} {result}")







