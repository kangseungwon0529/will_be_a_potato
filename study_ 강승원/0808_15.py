#6242 반복 6
student = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {}

for i in student:
    if i in dic.keys():
        dic[i] +=1
    else:
        dic[i] = 1
print(dic)