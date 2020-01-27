class Airplane():
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False
    odometer = 0
    def take_off(self):
        is_flying = True
        message_take = f"{self.make}-{self.model} was take off."
        return message_take

    
    def land(self):
        is_flying = False
        message_take = f"{self.make} has landed, it's odometer shows {self.odometer}km."
        return message_take
    
    def fly(self, km):
        self.odometer += km
        message_take = f"{self.make} flew {self.odometer}km at a speed of {self.max_speed}km."
        return message_take


        

Example = Airplane('Star', 'GRX', '2019', 1200)
print(Example.take_off())
print(Example.fly(1000))
print(Example.land())