'''
2、小明爱跑步，爱吃东西
1)小明体重75.0公斤
2)每次跑步会减重0.5公斤
3)每次吃东西体重会增加1公斤
4)小美的体重是45.0公斤
需求分析
类：人
属性：名字、体重
方法：
    吃：体重增加1公斤
    跑步：体重减少0.5公斤
'''
class People():
    def __init__(self,name,heavy):
        self.name=name
        self.heavy=heavy
    def __str__(self):
        return f'{self.name}的体重为{self.heavy}kg'
    def eat(self):
        self.heavy+=1
        print(f'{self.name}的体重目前为{self.heavy}')
    def run(self):
        self.heavy-=0.5
xiaoming=People('小明',75)
print(xiaoming)
xiaoming.eat()