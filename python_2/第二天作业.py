# 5、求100以内的质数（只能被1和它本身整除）
list=[]
for i in range(2,101):
    for j in range(2,i): #比如76 则不可以被1和76整除 所以区间为 2到75
        if i%j==0:
            break
    else:
       list.append(i)
print(list)