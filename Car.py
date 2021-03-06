class Car:

   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self.current_speed = 0

   def accelerate(self, step=10):
       self.current_speed += step

   def decelerate(self, step=10):
       self.current_speed -= step

   def set_current_speed(self, value):
        if value <= self.top_speed:
            self.current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

   @property
   def current_speed(self):
       return self._current_speed

   @current_speed.setter
   def current_speed(self,value):
       if value <= self.top_speed:
           self._current_speed = value
       else:
           raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

class DieselEngine:
    def tank(self, how_many = 100):
        print(f"Adding {how_many} litres of Diesel")

class PetroEngine:
    def tank(self, how_many=20):
        print(f"Adding {how_many} litres of Diesel") 

class Manual:
    def gearbox(self):
        print(f"Manual gearbox")

class Truck(Car, DieselEngine):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

class SportCar(Car, PetroEngine, Manual):
    pass         

car = Car(make="BMW", model_name="3", top_speed=250, color="red")
print(car.current_speed)
truck = Truck(make="Mercedes", model_name="Vito", top_speed=220, color= "White", max_load=1200)
porshe = SportCar(make="Porshe", model_name="911", top_speed=300, color= "Black")
truck.tank()
porshe.tank()
porshe.gearbox()