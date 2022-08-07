#zip函数
list1=['1','2','3']
list2=['3','4','5']
# print(dict(zip(list1,list2)))  #{'1': '3', '2': '4', '3': '5'}

#字典表达式
dict1={list1[i]:list2[i] for i in range(len(list2))}
print(dict1)  #{'1': '3', '2': '4', '3': '5'}