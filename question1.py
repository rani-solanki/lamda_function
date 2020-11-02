def x(a): return a + 10
print(x(5))

# y=lambda a,b:a*b
# print(y(2,3))

x = lambda a, b : a * b
print(x(5, 6))

z= lambda x,y,i:x*y+i
print(z(2,3,4))

# when we are use this unction inside the the another function:
def functipon(n):
    return lambda a,b,c : a*b*c*n
x=functipon(4)
print(x(2,3,4))

# when we call two times take aregument
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))




