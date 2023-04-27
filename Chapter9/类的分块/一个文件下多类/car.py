class Car():
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """
            返回车最基本的信息，是一个字符串，不会自己打印
        """
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


# 一个电动车类
class ElectricCar(Car): 
    """ 一个电动车的类 """
    def __init__(self, make, model, year): 
        super().__init__(make, model, year)     # super() 实现继承父类的东西

        """ 注意这里：类属性 """
        self.battery = Battery()   # 这个属性比较特殊，他不止是一个数值，而是一个类

    # 重写父类方法：有些时候，父类继承的方法，在子类中不实用，所以我们需要重写来写
    def fill_gas_tank():
        """ 重写父类方法 """
        print("This car doesn't need a gas tank!")