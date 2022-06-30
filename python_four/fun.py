import os
path1=os.getcwd()
print('-------------path',path1)

path2=os.path.abspath(__file__) #返回的被执行文件的绝对的路径
print('-------------path2',path2)

path3=os.path.dirname(__file__)
print('-------------path3',path3) #返回文件名的路径

path4=os.path.dirname(os.path.dirname(__file__)) #os.path.dirname,返回当前文件名的父路径
print('-------------path4',path4) #返回文件名的路径
# -------------path C:\Users\li\PycharmProjects\vip8study\python_four
# -------------path2 C:\Users\li\PycharmProjects\vip8study\python_four\fun.py
# -------------path3 C:/Users/li/PycharmProjects/vip8study/python_four
# -------------path4 C:/Users/li/PycharmProjects/vip8study

'''
不建议用，建议用abspath
getcwd()函数的缺点：在自己的文件里引用该函数没有问题，但是其他文件引入自己的文件，
获取到的文件路径为被执行文件的路径
路径会随着被执行文件的改变而改变获取到的路径
比如fun.py在C:\Users\li\PycharmProjects\vip8study\python_four\
path1=os.getcwd() 打印为C:\Users\li\PycharmProjects\vip8study\python_four
pra.py在C:\Users\li\PycharmProjects\vip8study\python_2\文件里
pra.py引用了fun.py文件
打印后路径为C:\Users\li\PycharmProjects\vip8study\python_2\，而不是原来的路径
'''

