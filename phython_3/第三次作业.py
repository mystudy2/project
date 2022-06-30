# 1.把上次课的作业重新编程（不能看答案，把分析过程写出来敲代码）
# 99乘法表；质数判断；三角形打印；斐波那契数列
# 2.打印由*组成的菱形，该菱形一共7行，已经发在群里，字节找图
# 3.使用列表退推倒式生成能被5整除的数（100以内）
# 4.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄

'''
斐波那契数列
斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368[1]
特别指出：第0项是0，第1项是第一个1。
这个数列从第3项开始，每一项都等于前两项之和

list1=[0,1]

for i in range(11):
        list1.append(list1[len(list1)-2]+list1[len(list1)-1])
print(list1)

#斐波那契数列 1 1 2 3 5
i=int(input('请输入第几位数:'))
def fib(n):
   if n==1 or n==2:
       return 1
   return fib(n-1)+fib(n-2)
result=fib(i)
print(result)

num=int(input('inptut your num:'))
for i in range(2,num):
    if num%i==0:
        print(f'{num} is not a 质数')
        break
else:
    print(f'{num} is  a 质数')




1*1=1
1*2=2 2*2=2
1*3=3 2*3=6 3*3=9
''
1*9=9                     9*9=81

i=1
while i<=9:
    j=1
    while j<=i:
        print(f'{i}*{j}={i*j}',end='\t')
        j+=1
    print()
    i+=1



# 2.打印由*组成的菱形，该菱形一共7行，已经发在群里，字节找图

   *
  ***
 *****
*******
 *****
  ***
   *

print('***','1')  #print打印两个字符串连接，中间会多了个空格

i=0
while i<4:
    print((3-i)*' ',end='')
    print((2*i+1)*'*')
    i+=1
bottom=1
lines=3
while bottom<4:
    print(bottom*' ',end='')
    print((2 * (lines-bottom) + 1) * '*')
    bottom+=1
"""






# 3.使用列表退推倒式生成能被5整除的数（100以内）
# list1=[i for i in range(101) if i%5==0]
# print(list1)

# 4.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄

name=['lilingyan','panxu','fengrui','yanshai']
age=[33,31,32,30]
dict1={}
for i in range(len(name)):
    dict1[name[i]]=age[i]
print(dict1)
'''
