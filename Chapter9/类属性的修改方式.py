class Car():
    def __init__(self, make, model, year): 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 接下来，我们要用不同的方法，实现对这个默认值的改动

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage): 
        """ 
            修改odo_reading 为指定的数 
        """
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016)


# 1、直接修改法
my_new_car.odometer_reading = 23

# 2、通过内置方法间接修改
my_new_car.update_odometer(66)