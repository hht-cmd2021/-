movies = ["国产:流浪地球","国产：飞驰人生","国产：疯狂的外星人","欧美：阿丽塔","欧美：驯龙高手3","欧美：死侍2"]

#过滤movies，声明函数，传入列表，返回新列表，新列表中的所有内容都是国产电影
"""
def test_filter(array):
	#创建一个新列表用来返回
	temp = []
	for item in array:
		if(item.startswith("国产")):
			temp.append(item)
	return temp
v = test_filter(movies)
print(v)
"""

"""
def test_filter(func, array):
	#创建一个新列表用来返回
	temp = []
	for item in array:
		if(func(item)):
			temp.append(item)
	return temp

#v = test_filter(lambda x:x.startswith("国产"),movies)
#v = test_filter(lambda x : x.startswith("欧美"), movies)
print(v)
"""

v = filter(lambda x:x.startswith("国产"), movies)
print(list(v))