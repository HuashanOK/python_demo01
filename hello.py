#print ("Hello World!")

# a="123";
# print(isinstance(a,str)) #判断数据类型
# print(isinstance(a,int))
# print(isinstance(a,float))

# a="1"
# print(int(a)) #数据类型转换
# print(float(a))
# print(str(2))

# a=b=c=d=e=10
# a+=1
# b-=1
# c*=10
# d/=8
# e=e//8 #取整数部分
# f=5%2
# g=3**2 #幂运算 3的2次幂
# print(a,b,c,d,e,f,g)

# a=(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
# print(a)

# score = int(input("请输入数字："))
# level = 'A' if 100>=score>=90 else 'B' if 90>score>=80 else 'C' if 80>score>=70 else 'D' if score<70 else 'E'
# print(level)

#assert 3>4 #当关键字后条件为假 抛出异常

""""循 环"""""
# for i in "abcdefg":
#     print(i)

# range(stop)
# range(start,stop)
# range(start,stop,step)
#print(list(range(10)))

# for i in range(1,10,2):
#     print(i)

# i=0
# while i < 10:
#     if(i==5):
#         break
#     print(i)
#     i+=1

# for year in range(2018,2050):
#     if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         print(year)
#         continue

"""列 表"""
# number=[1,2,3]
# number.append(5)
# print(number)
# number.extend([8,9])
# print(number)
# number.insert(0,0)
# print(number)
# number.insert(-1,8.5) #-1 表示与列表末尾的相对距离
# print(number)

#names = ["张三","李四","王五","贾六"]
# print(names[0])
# print(len(names))
# print(names[len(names)-1])
# print(names[-1])

# import random
#names = ["张三","李四","王五","贾六"]
# print(random.choice(names)) #随机取

# names = ["张三","李四","王五",["贾六","七","八"]]
# print(names[3][2])

#names = ["张三","李四","王五",["贾六","七","八"]]
#names.remove("张三") #删除指定元素
# name = names.pop(0) #将列表中指定元素 取出并删除 参数：索引  不带参数默认最后一个
# print(name)
# del names[0] #del python语句 可以删除元素或者变量
# print(names)
# del names
# print(names)

#列表切片 slice 获得源列表拷贝
# list=["一","二","三","四","五","六"]
# list2 = list[2:4]
# list2 = list[:4]
# list2 = list[2:]
# list2 = list[:]
# print(list2)

# list = list(range(100))
# print(list[-10:])

# list = [1,2,3,4,5,6,7,8,9]
# print(list[2:8:3]) #列表切片第三个参数 步长 默认1
# print(list[::-1]) #负数 倒叙

# del list[:2] #del 方法会删除源列表
# print(list)

# list1 = [123]
# list2 = [234]
# print(list1>list2)
# list1 = ["a"]
# list2 = ["b"]
# print(list1>list2)
# list1 = [123,234]
# list2 = [345,123]
# print(list1>list2) #默认比较第一个元素
# print(list1+list2) #合并两个列表 等于 extend()
# print(list1.extend(list2))
# print(list1*3) #列表里的元素复制三份

#in 、not in 只能判断一层
# list = ["一","二","三"]
# list = ["一","二",["三","四"]]
# print("一" in list)
# print("一" not in list)
# print("三" in list)
# print("三" not in list)

#print(dir(list))
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# list = [1,2,3,4,5,6,5,7,8]
# print(list.count(5)) #统计某个元素在列表中出现的次数
# print(list.index(5)) #返回第一次出现的索引
# print(list.index(5,5,7)) #index可以限定查找范围
# list.reverse() # 与list[::-1]效果一样，此方法在改变源列表，list[::-1]不改变源列表
# print(list)
# list.sort(reverse=True) #列表排序 sort() 从小到大 sort(reverse=True) 从小到大排序后再倒叙
# print(list)

"""元 组"""
#元组只能被访问 不能被修改
# tuple1 = (1,2,3,4,5)
# print(tuple1)
# print(type(tuple1))
# print(tuple1[:3])
# print(tuple1[2:])
# tuple2 = tuple1[:]
# print(tuple2)

#元组只要用逗号 , 区分
# tuple1 = (8)
# print(type(tuple1))
# tuple1 = (8,)
# print(type(tuple1))
# tuple1 = 8,
# print(type(tuple1))
# print(8*(8))
# print(8*(8,))

#利用切片和拼接的方法更新元组 ps:两个tuple1名字相同但不是同一个
# tuple1 = ("a","b","c","d")
# print(id(tuple1))
# tuple1 = (tuple1[0],"A") + tuple1[1:]
# print(tuple1)
# print(id(tuple1))
# print(tuple1[:1]+tuple1[2:])

"""字符串"""
# str1 = "一只穿云箭"
# str1 = str1[:1]+"支"+str1[2:]
# print(str1)
# print(str1.count("一"))
# print(str1.count("只",0,5))
# print(str1.find("只"))
# print(str1.find("支"))
# print(str1.index("支"))
# print(str1.replace("一","二"))
# print(str1.split("穿"))
# num = ['1','2','3','4','5']
# str1 = "_".join(num)
# print(str1)

#字符串格式化
# print("{0} love{1}.{2}".format("I","fishC","com")) #位置参数
# print("{a} love{b}.{c}".format(a="I",b="fishC",c="com")) #关键字参数
# print("{0} love{b}.{c}".format("I",b="fishC",c="com")) #位置参数再关键字参数前
# print("{{0}} love{b}.{c}".format("I",b="fishC",c="com")) #打印{}
# print("{0} : {1:.2f}".format("圆周率",3.1415926))

result = "result is %s : %d" % ("张三",100)
result2 = "result is %s : %d" % ("李四",50)
print(result)
print("%s  %s" % (result,result2))
print("%5.1f" % 12.3456)

