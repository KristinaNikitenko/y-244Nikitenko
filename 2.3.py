import math
x=float(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=float(input("Введите переменную z:"))
s=((1+math.pow(math.sin(x+y),2))/math.fabs(x-(2*y/(1+math.pow(x,2)*math.pow(y,2)))))*math.pow(x,math.fabs(y))+math.pow(math.cos(math.atan(1/z)),2)
print("s={0:.5F}".format(s))