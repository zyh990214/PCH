'''
1.创建一个汽车类:
类要求有以下属性:
    1.颜色
    2.牌子
    3.价钱
类要求有以下动作
    1.启动
    2.开始跑
    3.超车
'''


#定义一个car类
class Car():
    #车的名字(品牌)
    name = None
    #车的颜色
    color = None
    #车的价钱
    price = None

    #创建车的方法
    #启动
    def stratThe(self):
        print("启动喽")
    def overTaking(self):
        print("前面的车子让让,我要开始超车了")

car = Car()
car.name = "宝马"
car.color = "黑色"
car.price = "5W"

print("我买的",car.color,car.name,car.price)

car.stratThe()

car.overTaking()