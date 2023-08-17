t = int(input())
for tc in range(1, t + 1):
    # n은 오븐크기 m은 피자개수
    n, m = map(int, input().split())
    # 우리가 구워야할 피자들의 치즈정보
    ci = list(map(int, input().split()))

    # 다음에 꺼내올 피자 인덱스
    next_i = 0

    # 오븐을 큐로 만들어보자
    arr = [0] * 1000
    front = rear = -1
    # 오븐의 크기만큼 피자 넣어주기
    for i in range(n):
        # 오븐에 피자 넣기
        rear += 1
        # 나중에 꺼낼때를 위해서 피자번호도 같이넣기
        arr[rear] = [i, ci[i]]  # [피자 번호, 치즈양]
        next_i += 1

    # 오븐에 남아있는 피자의 개수
    reamin = n
    # 마지막에 꺼낸피자의 번호
    last_idx = -1
    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        # 피자를 하나꺼내서
        front +=1
        pizza_idx , pizza = ci[front]
        # 치즈를 녹이고//2
        pizza //=2


        # 남은 치즈양이 0 이나니다 ==> 다시 오븐에 넣기
        if pizza != 0:
            rear +=1
            ci(rear) = [pizza_idx, pizza]
        # 남은 치즈의 양이 0이다
        else:
        # 현재 오븐의 자리에 남은 피자 하나 꺼내서 넣기
            if next_i<m:
                rear+=1
                over[rear] = [next_i,ci[next_i]]
                next_i += 1


        # 넣은 피자가 없다
            else:
                reamin -= 1
                if reamin == 0 :
                    last_idx = pizza_idx
                    break
        # 오븐에 남은 피자도 없는 상황
        # 현재 피자의 번호가 답
        # 반복 종료
    print(f"#{tc} {last_idx+1}")
