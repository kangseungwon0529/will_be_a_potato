#6218숫자의 약수 구하기

n = int(input())

nanut = list(range(1,10))

num = 10
for i in range(len(nanut)):
    if n%nanut[i] == 0 :
        print(f"{nanut[i]}(은)는 {n}의 약수입니다.")