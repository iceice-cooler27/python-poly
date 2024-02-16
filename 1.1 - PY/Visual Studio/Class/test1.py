class Car:
    brand = "Nissan"
    model = "Model X"
    colour = "White"
    def __init__(self, brand, model, colour, top_speed):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.speed = 0
        self.top_speed = top_speed
    
    def startCar(self):
        self.speed = 10
        print("The car has started.")
    
    def stopCar(self):
        self.speed = 0
        print("The car has stopped")
    
    def honk(self):
        print("HONK")
    
    def set_top_speed(self, speed):
        self.top_speed = speed

ToyCar =Car("Toyota","Model Y","Grey",100)
ToyCar.startCar()
print("Before:", ToyCar.top_speed)
ToyCar.set_top_speed(120)
print("After:", ToyCar.top_speed)