import turtle
from turtle import done, circle
import time

# there are two ways for importing, first is the importing whole module
# second is the importing specific methods or attributes of module
# when importing with the second way remember not to use module name when calling method

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
circle(50)
# time.sleep(10)
done()
# we can use sleep() method within time module to wait for predefined time
# or we can use done() method within turtle module