# 6230 반복 1
# while문과 pop 함수를 이용하여 기준 이상 점수의 합구하기

num = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
count = 0

while len(num)>0:
    i = num.pop()
    if i >=80:
        count += i

print(count)