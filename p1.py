import keyword
from typing import Any, Union

age = 18 + True
print(age)

name = "yang %s, %d years old"
print(name % ("feixiang", 18))

a = 5 / 3
print(a)

a = 5 // 2
print(a)

a = 5 % 2
print(a)

a = 5 ** 3
print(a)
a *= 2
print(a)


# l = [1, 2, 3, 5, 6]
# for i in l:
#     print(i)

# a = keyword.kwlist
# b = keyword.kwlist.copy()
# print( a is b )
#
# a = input("你是男是女?")
# if a == "男":
#      print("大老爷们儿")
# elif a=="女":
#      print("老娘们儿")
# else:
#     print("你是泰国来的么?")

def IsOuShu(num):
    if num % 2 == 0:
        return True
    else:
        return False


for i in range(1, 10):
    if IsOuShu(i):
        print("%d 是偶數%s" % (i, "!"))
else:
    print("no break.")


def func_PrintColumn(row):
    for col in range(1, row + 1):
        print("{0} x {1} = {2}\t".format(col, row, col * row), end="")


for i in range(1, 10):
    func_PrintColumn(i)
    print("")

print("*" * 40)

# print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

a = 10
b = 20
print("a = {0}, b={1}".format(a,b))
a,b = b,a
print("在 python 中 a({0}) 与 b({1}) 调换后".format(a,b))

def stu(*args):
    for item in args:
        print(item)


stu("a", "b", "c")


def stu_key(**kwargs):
    for k, v in kwargs.items():
        print(k, "-" * 5, v)
    # for key in kwargs:
    #     print("{0}:{1}".format(key,kwargs[key]))


stu_key(name="yang feixiang", age=19, worker="IT")

print( "*" * 50)
def  stu_key_more(name, **kwargs):
    print( "my name is ", name )
    for k, v in kwargs.items():
        print(k, "-" * 5, v)

stu_key_more(name="yang feixiang", age=19, worker="IT")

# 收集参数的解包
def  stu1(* args):
  '''
  这是一个测试的函数描述文档.
  :param args: 收集参数
  :return: None
  '''
  for item in args:
        print( item )

l=["yang","feixiang",19,399]
#stu1(l)
stu1(*l)


def func_global_args():
    global  b1
    b1 = 100
    print( " 函数内的b1 = {0}".format(b1))

func_global_args()
print(b1)


global1 = 0
def modify_globalparam():
    global global1
    global1   = global1 +1
    print(global1)

modify_globalparam()


ll = [3,4,54,6,3,435,34]
print(ll[1:6])
print(ll[:2])
print(ll[0:5:1])
print(ll[-1:-4:-1])
print(ll[-1:-4:-2])

#汉诺塔
def move(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,"A","B","C")


#help(ll.sort)
#ll.sort()
#ll.sort( reverse=True)

#list 的创建
l = [i for i in range(1,11)]
print(l)

#创建List并且可以在后面加条件语句,666
# l = [i for i in range(1,11) if i % 2 == 0]
# print(l)

# l = [ (i + j) for i in range(1,4) for j in range(4,7) ]
# print(l)

# ll = list(l)
# print(ll)
#
# ll = [i for i in range(1,11)]
# ll.extend(["a","b","c"])
# ll.append("d")
#print(ll)


print(id(ll))
ll.clear()
print(ll)
print(id(ll))



print("*" * 30)

