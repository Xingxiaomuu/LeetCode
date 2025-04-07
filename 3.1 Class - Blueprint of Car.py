class Car() :
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        self.speed = 0
    def accelerate(self,increment):
        self.speed += increment
    def brake(self,decrement):
        if self.speed <= decrement:
            self.speed = 0
        else:
            self.speed -= decrement
    def show_info(self):
        print(f"{self.color}{self.brand}汽车当前时速为 {self.speed} km/h")


car1 = Car("宝马","灰色")
car2 = Car("奔驰","黑色")
car3 = Car("奥迪","白色")
car1.accelerate(50)
car1.show_info()