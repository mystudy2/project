# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# list1=[]
# for i in range(1,3):
#     for j in range(0,3):
#         # print((i,j))
#         list1.append((i,j))
# print(list1)

# dict1={}
# for i in range(1,6):
#     dict1[i]=i**2
# print(dict1)

# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 20, 'man']
# dict1={}
# for i in range(len(list1)):
#     dict1[list1[i]]=list2[i]
# print(dict1)


counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dict1={key:value for key,value in counts.items() if value>=200}
print(dict1)

