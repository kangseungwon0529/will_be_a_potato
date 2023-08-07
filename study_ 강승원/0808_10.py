# 6230 반복 1

num = [88,30,61,55,95]

for i in range(0,len(num)):
    if num[i] >= 60:
        print(f"{i+1}번 학생은 {num[i]}점으로 합격입니다. ")
    elif num[i] < 60:
        print(f"{i+1}번 학생은 {num[i]}점으로 불합격입니다. ")

