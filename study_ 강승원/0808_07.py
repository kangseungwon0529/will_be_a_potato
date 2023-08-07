#6218숫자의 약수 구하기

n = int(input())

nanut = list(range(1,10))
count = 0

for i in range(len(nanut)):
    if n%nanut[i] == 0 :
        print(f"{nanut[i]}(은)는 {n}의 약수입니다.")
        count += 1
if count == 2 :
    print(f"{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.")
