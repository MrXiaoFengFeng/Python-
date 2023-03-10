# 一、名称空间namespaces：存放名字的地方，是对栈区的划分
# 有了名称空间后，就可以在栈区中存放相同的名字，详细的，名称空间
# 分为三种：
# 1.1内置名称空间
# 存放的名字：存放的python解释器内置的名字
#存活周期：python解释器启动则产生，python解释器关闭则销毁
'''
>>> print
<built-in function print>
>>> input
<built-in function input>
'''



# 1.2全局名称空间
# 存放的名字：只要不是函数内定义的，也不是内置的，剩下的都是全局名称空间
#存活周期：python文件执行则产生，python文件运行完毕后销毁
# import os
# x = 10
# if 13 > 3:
#     y = 20
#     if 3 == 3:
#         z = 30
# class Foo:
#     pass
#以上均为全局名称空间
#以下不是
# def func(): #func是全局名称空间
#     a = 111 #不是，函数定义内的
#     b = 222 #不是





# 1.3局部名称空间
# 存放的名字：在调用函数时，运行函数体代码过程中产生的函数内的名字
#存活周期：在调用函数时存活，函数调用完毕则销毁
# def func(a,b):
#     pass
# func(1,2)
# func(1,3)
# func(1,4)
# 函数调用一次就产生一次名称空间，调用完毕后就销毁，所以以上会产生3次局部名称空间，哪怕是func()


#1.4名称空间的加在顺序
# 内置名称空间>全局名称空间>局部名称空间

#1.5销毁顺序
# 局部名称空间>全局名称空间>内置名称空间


#1.6名字的查找优先级：当前所在的位置向上一层一层查找
#如果当前在局部名称空间：
# 局部名称空间-》全局名称空间-》内置名称空间
# 举例：
# input = 3333
# def func():
#     input = 444
#     print(input)
# func()
# 解析：当前程序运行后，打印input结果为444，在局部里找；
# 注释掉input = 444，打印结果为3333，局部没有就去全局找；
# 注释掉input = 3333，打印结果为<built-in function input>，全局没有就去内置找


#如果当前在全局名称空间：
# input = 3333
# def func():
#     input = 444
# func()
#print(input) #3333


#示范1：
# def func():
#     print(x)  #结果为111,局部没找到就去全局找
# x = 111
# func()
#
# 示范2：名称空间的'嵌套'关系是'以函数定义阶段为准'，与调用位置无关
# x = 1
# def func():
#     print(x)  #结果为1
# def foo():
#     x = 222
#     func()
# foo()


#示范3：函数嵌套定义
# input = 111
# def f1():
#     input = 222
#     def f2():
#         input = 333
#         print(input) #结果为333，调用f2（）时，局部找到了
#     f2()
# f1()
#

#示范4：变量一定要先定义后调用
# x = 111
# def func():
#     print(x) #报错x没有定义，x=222应该放在print上面，UnboundLocalError: local variable 'x' referenced before assignment
#     x = 222
# func()


# ========================================================================
# 二.作用域->作用范围
# 全局作用域:内置名称空间,全局名称空间
# 1.全局存活
# 2.全局有效:被所有函数共享
# def foo():
#     x = 111
#     print(x)
#
# def bar():
#     y = 222
#     print(y)
# foo()
# bar()
#foo中无法找到y值，bar中无法找到x值，局部内不共享，但是如有全局名称空间的值或者内置名称空间的值则可以

# 局部作用域:局部空间的名字
# 1.临时存活
# 2.局部有效:函数内有效  f1(),f2()都能获取到x

# def foo(x):
#     def f1():
#         def f2():
#             print(x)

# build-in
# global
# def f1():
#     # e
#     def f2():
#         # e-》enclosing
#         def f3():
#             # local
#             pass


# ===================总结重点====================
# 重点1：
# 名词查找：当前所在的位置向外查找
# 局部名称空间-》全局名称空间-》内置名称空间
#
# 重点2：
# 名称空间只有优先级之分，本身并无嵌套关系，画图知识为了方便理解
#
# 重点3：
# 名称空间的嵌套关系决定了名字的查找顺序。
# 而名称空间的嵌套关系是以函数的定义阶段为准的，
# 即函数的嵌套关系与名字的查找顺序是在定义阶段就已经确定好了的

#
# 全局作用域：内置名称空间+全局名称空间的名字
#     全局存活，全局有效
# 局部作用域：
#     临时存活，局部有效




# def f1():
#     print(x)  #x没有被定义 UnboundLocalError: local variable 'x' referenced before assignment
#     x = 222
# f1()

num_list = [1, 2, 3]


def foo(nums):
    nums.append(5)
    print('zhe',nums)


foo(num_list)
print(num_list)
# # 结果为
# [1, 2, 3, 5]