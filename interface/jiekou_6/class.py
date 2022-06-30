class Washer():
    def wash(self):
        print("洗衣服")
        print('self: ',self)

haier1=Washer()
haier1.wash()
print('haier1',haier1)

#self指的是调用该函数的对象 谁调用指的就是谁，如haier1,haier2

#给类添加属性
haier1.height=500
haier1.width=300

#获取类的属性
print(f'海尔洗衣机的高为：{haier1.height}')
print(f'海尔洗衣机的宽为：{haier1.width}')



class Washer():
    def __init__(self):
        self.height=300
        self.width=400
    def wash(self):
        print('洗衣机的高为：',self.height)
        print('洗衣机的宽为：', self.width)
haier1=Washer()
haier1.wash()



class Washer():
    def __init__(self,width,height):
        self.height=height
        self.width=width
    def wash(self):
        print('洗衣机的高为：',self.height)
        print('洗衣机的宽为：', self.width)
    def __str__(self):
        return '这是海尔洗衣机的说明书'
haier1=Washer(100,200)  #创建对象的时候传参数，只有self不用传参数
# haier1.wash()
# print(haier1)


class Washer():
    def __init__(self,width,height):
        self.height=height
        self.width=width
    def wash(self):
        print('洗衣机的高为：',self.height)
        print('洗衣机的宽为：', self.width)
    def __str__(self):
        return '这是海尔洗衣机的说明书1'
    def __del__(self):
        print(f'{self}')
haier1=Washer(100,200)  #创建对象的时候传参数，只有self不用传参数
# print(haier1)
# del haier1
# print(haier1)

class Cat():
    def eat(self):
        print('小猫爱吃鱼')
    def drink(self):
        print('小猫爱喝水')
badCat=Cat()
badCat.eat()
badCat.drink()


#性别为男的梁超老师教测试
# 类：老师
# 属性：性别，姓名
# 方法：教
class Teacher():
    def __init__(self,sex,name):
        self.sex=sex
        self.name=name
    def eat(self):
        print('吃饭')
    def jiao(self,item):
        self.eat() #类里面调用自己的方法
        print(f'性别为{self.sex}的{self.name}老师教{item}')
t1=Teacher('男','梁超')
t1.jiao('测试')





# 类：烤地瓜
# 属性：口味
# 方法：烤

class SweetPotato():
    def __init__(self):
        self.cook_static='生的'
        self.cook_time=0
        self.condiments=[]
    def add_tiaoliao(self,tiaoliao):
        self.condiments.append(tiaoliao)
    def cook(self,time):
        self.cook_time+=time
        if 0<=self.cook_time<3:
            self.cook_static='生的'
        elif 3<=self.cook_time<5:
            self.cook_static='半生不熟'
        elif 5<=self.cook_time<8:
            self.cook_static='熟了'
        elif self.cook_time>8:
            self.cook_static='糊了'
    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态时{self.cook_static},添加的调料有{self.condiments}'
digua1=SweetPotato()
digua1.cook(2)
digua1.add_tiaoliao('孜然')
print(digua1)

digua1.cook(2)
digua1.add_tiaoliao('孜然')
print(digua1)


'''
#将小于房子剩余面积的家具摆放到房子中
分析：
    1-类：
        1.1-房子类
            1.1.1-属性：总面积、剩余面积、家具列表、户型
            1.1.2-方法：添加家具
                1.1.2.1-参数item-代表接收家具（对象）变量
                1.1.2.1-根据家具的占地面积和房子的剩余面积标记
        1.2-家具类
            1.2.1-属性：名称、家具占地面积
           1.2.2-方法：无
'''

class Furniture():
    def __init__(self,name,area):
        self.name=name
        self.area=area
class Home():
    def __init__(self,area):
        self.area=area
        self.free_area=area
        self.furniture=[]
    def __str__(self):
        return f'房屋的剩余面积为{self.free_area},房屋的家具有{self.furniture}'
    def add_furniture(self,item):
        if self.free_area>=item.area:
            self.furniture.append(item.name)
            self.free_area-=item.area
        else:
            print('家具超过房屋的剩余面积，请放入另一个房间')
home=Home(100)
bed=Furniture('床',10)
home.add_furniture(bed)
bed=Furniture('柜子',100)
home.add_furniture(bed)
print(home)




#单继承-煎饼果子
#师父类
class Master(object):
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School():
    def __init__(self):
        self.kongfu='[香辣煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[酸甜煎饼果子配方]'
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
class Tusun(Prentice):
    pass

xiaoming=Tusun()
xiaoming.make_cake()
xiaoming.make_school_cake()
xiaoming.make_master_cake()
# xiaoming=Prentice()
# xiaoming.make_cake()
# xiaoming.make_master_cake()
# xiaoming.make_school_cake()
# xiaoming.make_cake()
# print(Prentice.__mro__)


class Master():
    def __init__(self):
        self.kongfu='[五香煎饼]'

    def make_cake(self):
        print(f'制作{self.kongfu}')


class School(Master):
    def __init__(self):
        self.kongfu='[香辣煎饼]'
    def make_cake(self):
        print(f'制作{self.kongfu}')
        super().__init__()
        super().make_cake()
class Prentice(School):
    def __init__(self):
        self.kongfu = '[酸甜煎饼]'
        self.__money = '200'
    def __info(self):
        print(self.__money)
    def make_cake(self):
        self.__init__()
        print(f'制作{self.__money}')
    def make_old_cake(self):
        super().__init__()
        super().make_cake()
xiaoming=Prentice()
# xiaoming.make_old_cake()
# xiaoming.make_cake()
xiaoming.__info()



class Dog():
    def __init__(self):
        self.tooth=10
    def info_print(self):
        print(self.tooth)
wangcai=Dog()
# xiaohei=Dog()
# wangcai.tooth=12
print(wangcai.tooth)
# print(Dog.tooth)
# print(xiaohei.tooth)
wangcai.info_print()



























