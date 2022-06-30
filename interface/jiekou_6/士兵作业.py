'''
4.士兵开枪
需求：
1).士兵瑞恩有一把ak47
2).士兵可以开火(士兵开火扣动的扳机)
3).抢 能够发射子弹（把子弹发射出去）
4).抢 能够装填子弹-增加子弹的数量

需求分析
类：士兵
属性：名字
方法：开火
        士兵 枪 发射
===================
类：枪
属性：
    子弹=0
    名字
方法：
    发射：判断当前子弹的数量 子弹减少 没子弹
    装填：子弹增加
'''
class Gun():
    def __init__(self,name):
        self.name=name
        self.bullet_count=0
    #魔法方法的作用-打印类中的对象的时候，自动调用str方法
    def __str__(self):
        return f'制作一把{self.name}有{self.bullet_count}发子弹'
    def add_bullet(self):
        self.bullet_count+=20
        print(f'{self.bullet_count}装填完毕')
    def shot(self):
        self.bullet_count-=1
        print(f'发射子弹1发，还剩{self.bullet_count}')
class Soilder:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'士兵{self.name}'
    def fire(self,item):
        if item.bullet_count>0:
            print('士兵射击')
            item.shot()
        else:
            print(f'{item.name}子弹不足，需要装填子弹')
            item.add_bullet()
AK=Gun('AK47')
print(AK)

re=Soilder('瑞恩')
print(re)
re.fire(AK)
re.fire(AK)