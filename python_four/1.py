# list1=[3,2,0,1,4,0]
# newList=[]
# for i in range(0,len(list1)):
#     newList.append(list1[i]**3)
# print(newList)

# 递归 100以内的累积和
# def digui(num):
#     if num==1:
#         return 1
#     return num+digui(num-1)
# result=digui(100)
# print(result)

# def feb(num):
#     if num<=1:
#         return num
#     return feb(num-2)+feb(num-1)
#
# for i in range(9):
#     print(feb(i),end='\t')


# glo_num=100
# def change_num():
#     global glo_num
#     glo_num=200
# change_num()
# print(glo_num)


str01='welcome to super&Test'
list03=str01.split(' ')
list04=[]
for i in  list03:
    str02=i[::-1]
    list04.append(str02)
print(' '.join(list04))


ssh -keygen -t rsa -C "1028307115@qq.com"
ssh-keygen -t rsa -C "1028307115@qq.com"
















