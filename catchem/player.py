import random

class Player:
    def __init__(self,left,right,position)
        self.left = left
        self.right = right
        self.position = random.randint(left,right)

    def move_right(self):
        if self.position < self.right:
            self.position = self.position +1
    def move_left(self):
        if self.position > self.left:
            self.position = self.position -1
    def get_position():
        return position

    def display(self,move):
        y = 7
        x = self.position%8
        sense.set_pixel(x-move,y,(0,0,0))
        sense.set_pixel(x,y,(130,50,50))


         