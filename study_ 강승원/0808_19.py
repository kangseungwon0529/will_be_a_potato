#6249 반복 10 numbers count
numbers = list(range(10))
num = [0]*10
n= int(input())
while n>0:
    num[n%10] += 1
    n = n//10

print(f" ".join(map(str,numbers)))
print(" ".join(map(str,num)))