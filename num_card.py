t = int(input())
for tc in range(1,t+1):
    n = int(input())
    ai = list(input())
    num_list = list(range(10))
    count = [0]*10

    for i in ai:
        if i == num_list[i]:
            count[i] += 1