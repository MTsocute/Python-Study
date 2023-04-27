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