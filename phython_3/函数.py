# def add(a,b):
#     sum=a+b
#     print(sum)
#
# a=int(input('please input num1:'))
# b=int(input('please input num2:'))
# add(a,b)

# def add(a,b):
#     """求和函数"""
#     return a+b
# a=int(input('please input num1:'))
# b=int(input('please input num2:'))
# sum=add(a,b)
# print(sum)

# help(add)

#求三个数平均值
# def sum_num(a,b,c):
#     return a+b+c
# def avg(a,b,c):
#     sum=sum_num(a,b,c)
#     return sum/3
# avg=avg(1,1,1)
# print(avg)

# def buy():
#     return '烟','钱'
# # 使⽤变量保存函数返回值
# goods,money = buy()
# print(goods,money)

# 计算 list1 序列中各个数字的2次⽅
# list1 = [1, 2, 3, 4, 5]
# def func(x):
#     return x*2
# result=map(func,list1)
# print(result)
# print(list(result))


# 计算 list1 序列中各个数字的累加和
# list1 = [1, 2, 3, 4, 5]
# import functools
# def func(a,b):
#     return a+b
# result=functools.reduce(func,list1)
# print(result)