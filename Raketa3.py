class Rocket:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def fly (self):
         return self.x , self.y
    def move_up(self):
        self.x +=1
        return self.x
    def move_down(self):
        self.x -=1
        return  self.x
    def move_left(self):
        self.y -=1
        return self.y
    def move_right(self):
        self.y +=1
        return self. y
x_value = 0
y_value = 0
my_rocket = Rocket (x_value, y_value)
print(my_rocket.fly())
my_rocket2 =Rocket(x_value,y_value)
print (my_rocket2.move_up())
my_rocket3 =Rocket(x_value,y_value)
print(my_rocket3.move_down())
my_rocket_left = Rocket(x_value,y_value)
print(my_rocket_left.move_left())
my_rocket_right  = Rocket(x_value,y_value)
print(my_rocket_right.move_right())
