# 创建子类时候，必须要在同一个文件，然后父类一定要在子类的前面
class Car(): 
    """
        一个车的大类
    """
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles): 
        self.odometer_reading += miles

    def fill_gas_tank():
        """ 被重写的父类方法 """
        print("Completed~")


# 一个电动车类
class ElectricCar(Car): 
    """ 一个电动车的类 """
    def __init__(self, make, model, year): 
        """
            继承父类的属性
        """
        super().__init__(make, model, year)     # super() 实现继承父类的东西

        # 让我们来定义一些电动车才有的属性和方法
        self.battery_size = 70  # 电瓶容量

    def describe_battery(self): 
        """显示电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    
    # 重写父类方法：有些时候，父类继承的方法，在子类中不实用，所以我们需要重写来写
    def fill_gas_tank():
        """ 重写父类方法 """
        print("This car doesn't need a gas tank!")
        


# 电动车对象生成
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())  # 继承父类的方法
my_tesla.describe_battery()             # 子类自己独有的方法

