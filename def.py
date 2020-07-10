def myFunction(name,age):
    """
    这是注释
    :param name:
    :return:
    """
    print("name："+name)
    print("age："+age)
    #return name+"_"+age

# str = myFunction("哈哈哈")
# print(str)

#方法注释
# print(myFunction.__doc__)
# print(help(myFunction))
#myFunction(name="名字",age="年龄")

#位置参数要在默认参数前
def fun(index,name="默认名字",age="默认年龄"):
    print(str(index)+name+age)

#fun(1)

#收集参数 参数个数不确定 收集参数把参数们打包成一个元组
def fun2(*param):
    print(param)
# fun2([1,2,3])
# fun2(1,2,3)
# fun2("sss") #('sss',)
# fun2("123",123)

#如果在收集参数后面还需要指定其他参数，那么在调用的时候需要使用关键字参数
def fun3(*param,extra):
    print("收集参数：",param)
    print("位置参数：",extra)
# fun3(1,2,3,4,5)
#fun3(1,2,3,4,extra=5)

str="FishC"
print(*str)


