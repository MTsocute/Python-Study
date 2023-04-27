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