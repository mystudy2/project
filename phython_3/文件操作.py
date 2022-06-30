# f=open('text.txt','w')
# # f.write('hello word')
# # f.close()

# f=open('text.txt')
# f.write('hello word1')

# content=f.read()

# content=f.readlines()

# content=f.readline()
# print(content)
# content=f.readline()
# print(content)

# f.seek(4)
# content=f.readlines()
# print(content)
# f.close()

# 2.1 提取⽂件后缀点的下标
old_name='test.txt'
index = old_name.rfind('.')
# print(index) # 后缀中.的下标
# print(old_name[:index]) # 源⽂件名（⽆后缀）
# 2.2 组织新⽂件名 旧⽂件名 + [备份] + 后缀
new_name = old_name[:index] + '[备份]' + old_name[index:]
# 打印新⽂件名（带后缀）
# print(new_name)