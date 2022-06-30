'''
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
    新房子没有任何的家具
2).家具有名字和占地面积，其中
    床：占4平米
    衣柜：占2平米
    餐桌：占1.5平米
3).将以上三件家具添加到房子中
4).打印房子时，要求输出：户型，总面积，剩余面积，家具名称列表

需求分析
类：房子
属性：
    户型、总面积、剩余面积、家具列表
方法：
    添加家具-剩余面积与要添加的家具对比，大于添加的家具，可以添加，房子家具列表增加
-----------------------------------------------
类：家具
属性：名字、占地面积
方法：无
'''
class House():
    def __init__(self,apartment,total_area):
        self.apartment=apartment
        self.tolal_area=total_area
        self.reside=total_area
        self.item_list=[]
    def __str__(self):
         return f'房子的户型是{self.apartment},总面积为{self.tolal_area},剩余面积为{self.reside},目前的家具为{self.item_list}'
    def add_furnitrue(self,item):
        if item.cover_area<=self.reside:
            self.reside-=item.cover_area
            self.item_list.append(item.name)
            print(f'给房子添加家具{item.name}')
        else:
            print(f'{item.name}的占地面积太大，屋里放不下')
class Furniture():
    def __init__(self,name,cover_area):
        self.name=name
        self.cover_area=cover_area
    def __str__(self):
        return f'{self.neme}占地{self.cover_area}'
bed=Furniture('床',10)
h=House('三室两厅',80)
h.add_furnitrue(bed)

bed=Furniture('柜子',75)
h.add_furnitrue(bed)
print(h)