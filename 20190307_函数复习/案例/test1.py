#没有参数，没有返回值
#输出1-100的和
def fun1():
	i = 1
	sum = 0
	while  i<=100:
		sum += i
		i += 1
	print(sum)

#没有参数，有返回值
#输出1-100的和，并返回
def fun2():
	i = 1
	sum = 0
	while  i<=100:
		sum += i
		i += 1
	return sum

#有参数，没有返回值
#传入n，计算1-n的和,并输出
def fun3(n):
	i = 1
	sum = 0
	while  i<=n:
		sum += i
		i += 1
	print(sum)

#有参数，有返回值
#传入n，计算1-n的值，并返回计算结果
def fun4(n):
	i = 1
	sum = 0
	while  i<=n:
		sum += i
		i += 1
	return sum

