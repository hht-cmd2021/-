def fun(x,y,z):
	print("x的值：" + str(x))
	print("y的值：" + str(y))
	print("z的值：" + str(z))

#调用函数时，可以指定参数的值，不需要和函数声明时参数的位置一致
fun(y=1,x=3,z=5)

#定义函数时，参数可以有默认值
def fun2(x=0,y=2,z=3):
	print("x的值：" + str(x))
	print("y的值：" + str(y))
	print("z的值：" + str(z))
fun2(x=5)