string="ranisolanki"
list=[]
for i in string:
    list.append(i)
print(list)
# find the data types   
aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))

# find the output
x = 50
def fun1():
    x = 25
    print(x)
fun1()
print(x)

# which is data type
print(type({}) is dict)

print(bool(7), bool(0), bool(-3), bool(1.0+1j))

# x = 75
# def myfunc():
#     x = x + 1
#     print(y)

# myfunc()
# print(x)

print(type(0xFF))

print(type(range(5)))

