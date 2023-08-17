#일단 앞에서 빼서 뒤로 추가
# 추가된 것을 다시 배열로 인식하고
# 숫자에 +1

t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    n_list = list(map(int, input().split()))
    arr = [0]*1000
    front = rear = -1
    for i in range(n):
        rear += 1
        arr[rear] =n_list[i]
    for i in range(m):
        front += 1
        rear += 1
        arr[rear] = arr[front]
    print(f"#{tc} {arr[m]}")


# t = int(input())
# for tc in range(1,t+1):
#     n,m = map(int,input().split())
#     n_list = list(map(int, input().split()))
#
#     print(f"#{tc} {n_list[m%n]}")