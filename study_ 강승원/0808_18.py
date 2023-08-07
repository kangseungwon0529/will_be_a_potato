#6247 반복 9 별찍기
star = "*"
space = " "
i = 7
k = 0
while i>0:
    print("{0}{1}".format((space)*k,star*i))
    i -= 2
    k += 1

