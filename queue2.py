q= []

q.append(1) #enqueue(1)
q.append(2)
q.append(3)

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
#front, rear 를 사용하면 인덱스를 이용하여 인덱스 값을 조정하는 것이므로
#인덱스로 이동하는 것이기 때문에
# q 리스트에 담겨진 원소는 사라지지 않고 그래도 있다
# append, pop을 사용하면 사라져요 ==> 원소 자체를 건드는 것이기 때문에