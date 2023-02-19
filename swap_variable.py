#Solution1 (Using third variable)
#x = 13
#y = 12

#temp = x
#print("The value of temp variable is",temp)

#x = y
#print("The value of x is ", x)

#y = temp
#print("The value of y is ",y)

#Solution2 (without using third variable)
x = 12
y = 13

x, y = y,x

print("The value of x is",x)
print("The value of y is",y)