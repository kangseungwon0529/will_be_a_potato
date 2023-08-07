#6251 반복 11별찍기
star = "*"
space = " "
i = 1
k = 4
while i<6:
    print("{0}{1}".format((space)*k,star*i))
    i += 1
    k -= 1

