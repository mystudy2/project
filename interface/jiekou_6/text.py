class Dog():
    __tooth=10
    @classmethod
    def get_tooth(cls):
        return cls.__tooth
wangcai=Dog()
result=wangcai.get_tooth()
print(result)

# 测1试