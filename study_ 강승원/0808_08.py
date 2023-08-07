#6220 흐름과 제어 if3
t = int(input())
alpha = input()
for tc in range(1,t+1):
    if alpha.isupper():
        print(f"#{tc} {alpha} 는 대문자 입니다.")
    elif alpha.islower():
        print(f"#{tc} {alpha} 는 소문자 입니다.")