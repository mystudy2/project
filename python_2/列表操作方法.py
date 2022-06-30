#8个老师如何随机分配到3个教室
'''
import random
names=['A','B','C','D','E','F','G','H']
office1=[]
office2=[]
office3=[]


for name in names:
    index=random.randint(1,3)
    if index==1:
        office1.append(name)
    elif index==2:
        office2.append(name)
    else:
        office3.append(name)
offices=[office1,office2,office3]
print('三个办公室的随机分配情况为：',offices)

for i in range(len(offices)):
    print('办公室%d的人数为%d' % (i+1,len(offices[i])))
    print('分别是：',end='\t')
    for name in offices[i]:
        print(name,end='\t')
    print('\n','-'*20)
'''
import random
offices=[[],[],[]]
names=['A','B','C','D','E','F','G','H']
for name in names:
    index=random.randint(0,2)
    offices[index].append(name)
print('三个办公室的随机分配情况为：',offices)



