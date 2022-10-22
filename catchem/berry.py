import random

class Berry:
    def __init__(self,color,speed)
    self.position = random.randint(0,7)
    self.color = color
    self.speed = speed
    self.value = value
    def drop(self):
        if self.position<= 55:
            self.position +=8
    def display(self):
        sense.Setpixel(self.position)
        x = self.position%8
        y = self.position//8
        sense.set_pixel(x,y-1, (255,255,256))

        