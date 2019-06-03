#声明一个函数，传入源列表，对源列表中的每一个元素进行加10操作，并将计算的结果放入新列表中，返回新列表
li = [12,3,22,34,12,45]

"""
def test_map(array):
	#创建一个新列表
	temp = []
	#遍历源列表
	for item in array:
		#将源列表的每一个元素+10,并放入新列表中
		temp.append(item + 10)
	return temp

v = test_map(li)
print(v)
"""
"""
def test_map(func, array):
	#创建一个新列表
	temp = []
	#遍历源列表
	for item in array:
		#func参数传传入的是一个lambda表达式，对item进行计算并前结果赋值给变量a
		a = func(item)
		#将计算的结果追加到新列表
		temp.append(a)
	return temp

v = test_map(lambda x : x + 10, li)
#v = test_map(lambda x : x * 2, li)
print(v)
"""

v = map(lambda x : x + 10, li)
print(list(v))
