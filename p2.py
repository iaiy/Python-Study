
ll = [i for i in range(10,21)]
ll.append(19)
print(ll.count(19))
ll.insert(0,"abc")
print( ll )


#tuple

t  = tuple()

t = (1,)
print(type(t))
print(t)

t = tuple(i for i in range(1,11))
print(t)


