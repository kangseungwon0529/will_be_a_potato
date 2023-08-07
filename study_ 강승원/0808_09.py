# 6226 흐름과 제어if 7
# 1~200까지의 수중에서 7의 배수 인데 5의 배수가 아닌 수만 출력
com_ex = ""
for i in range(1,201):
    if i%7 == 0 and i%5 != 0:
        com_ex += str(i) + ","

print(com_ex[:-1])