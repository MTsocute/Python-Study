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
        print("Completed~")


# 电池类
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self): 
        """显示电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """根据电瓶容量来推算这个车充满能开多远"""
        if self.battery_size == 70: 
            range = 240
        elif self.battery_size == 85: 
            range = 270
        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        """升级电池的大小到 85"""
        if self.battery_size < 85:
            self.battery_size = 85
            print("Your battery has been updated to {} -kWh".format(self.battery_size))
        elif self.battery_size == 85:
            print("Your battery is equal to 85 -kWh! You don't need to update it")
        else:
            print("Your battery is grater than 85 -kWh! You don't need to update it")


# 一个电动车类
class ElectricCar(Car): 
    """ 一个电动车的类 """
    def __init__(self, make, model, year): 
        super().__init__(make, model, year)     # super() 实现继承父类的东西

        """ 注意这里：类属性 """
        self.battery = Battery(85)   # 这个属性比较特殊，他不止是一个数值，而是一个类

    # 重写父类方法：有些时候，父类继承的方法，在子类中不实用，所以我们需要重写来写
    def fill_gas_tank(self):
        """ 重写父类方法 """
        print("This car doesn't need a gas tank!")
        


# 电动车对象生成
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.upgrade_battery()
my_tesla.fill_gas_tank()