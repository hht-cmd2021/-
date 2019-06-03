def fun1(x, *args):
	print(x)
	print(args)
	print(*args[0])


#fun1(1,2,3,4,5,6)
#fun1(1,[12,3,2])


def fun2(x, **kwargs):
	print(x)
	print(kwargs)


fun2(1,color="r", rotation=45)
