from car import Car
from ba import Battery


# 一个电动车类
class ElectricCar(Car): 
    """ 一个电动车的类 """
    def __init__(self, make, model, year): 
        super().__init__(make, model, year)     # super() 实现继承父类的东西

        """ 注意这里：类属性 """
        self.battery = Battery()   # 这个属性比较特殊，他不止是一个数值，而是一个类

    # 重写父类方法：有些时候，父类继承的方法，在子类中不实用，所以我们需要重写来写
    def fill_gas_tank(self):
        """ 重写父类方法 """
        print("This car doesn't need a gas tank!")