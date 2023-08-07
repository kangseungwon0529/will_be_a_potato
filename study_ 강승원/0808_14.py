# 6240 반복 5
# 1~100까지의 수중에서 n의 배수들의 합의 총합만 구해서 출력
count= 0
for i in range(1, 101):
    if i % 3 == 0 :
        count += i
print(f"1부터 100사이의 숫자 중 3의 배수의 총합: {count}")

