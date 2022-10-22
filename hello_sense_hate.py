import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
# alternatives
sense.rotation = 180

sense = SenseHat()
sense.flip_h()


r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

JCisBeautiful = [l, l, l, l, l, l, l, l,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, p,
         l, k, k, k, k, k, k, l,
         l, l, l, l, l, l, l, l
]	
sense.set_pixels(JCisBeautiful)	

JCisBeautiful2 = [l, l, l, l, l, l, l, l,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, p,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, l, l, l, l, l, l, l]

JCisBeautiful3 = [l, l, l, l, l, l, l, l,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, p,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, l, l, l, l, l, l, l]
JCisBeautiful4 = [l, l, l, l, l, l, l, l,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, k, p,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, l, l, l, l, l, l, l]
JCisBeautiful5 = [l, l, l, l, l, l, l, l,
         l, k, k, k, k, k, k, k,
         l, k, k, k, k, k, p, l,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, k, k, k, k, k, k, l,
         l, l, l, l, l, l, l, l]        
Snake = input(" >>> ")
if(Snake == "move"):
    
    sense.set_pixels(JCisBeautiful2)
    time.sleep(0.5)
    sense.set_pixels(JCisBeautiful3)
    time.sleep(0.5)
    sense.set_pixels(JCisBeautiful4)
    time.sleep(0.5)
    sense.set_pixels(JCisBeautiful5)

# elif Snake == "move":
#     JCisBeautiful = [l, l, l, l, l, l, l, l,
#          l, k, k, k, k, k, k, k,
#          l, k, k, k, k, k, k, k,
#          l, k, k, k, k, k, k, k,
#          l, k, k, k, k, k, k, p,
#          l, k, k, k, k, k, k, l,
#          l, k, k, k, k, k, k, l,
#          l, l, l, l, l, l, l, l
# ]	
		
		
		
		
		
		
		
		
		