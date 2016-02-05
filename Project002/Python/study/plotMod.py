
import random
import time
import math

from turtle import *    # import turtle
import matplotlib.pyplot as plt

version = '0.1'
    
################################################################################################### 
#
# plot multi-line segments
#
def moveTurtles(turtleList,dist,angle):
    for turtle in turtleList:   # Make every turtle on the list do the same actions.
        turtle.forward(dist)
        turtle.right(angle)
#
# plot circle
#
def pCircle( x, y, r, detail):
    xarr=[]
    yarr=[]
    for i in range(detail+1):
        jiao=float(i)/detail*2*math.pi
        x1=x+r*math.cos(jiao)
        y1=y+r*math.sin(jiao)
        xarr.append(x1)
        yarr.append(y1)
    plt.plot(xarr,yarr,linestyle='-', color='r')
    #plt.plot(xarr,yarr,linestyle='-', marker='o', color='r',markersize=10)
    plt.show() # display
#
# plot sun-light
#
def pSunLight(length):   
    color('red', 'yellow')
    #length = 400
    terminateDis = 10
    begin_fill()
    while True:
        forward(length)
        left(170)
        if abs(pos()) < terminateDis:
            break
    end_fill()
    done()
#
# plot rectangle
#
def pRectangle(turtle,centerX,centerY,radius):
    turtle.up()
    turtle.goto(centerX,centerY)
    turtle.color("red")
    turtle.pensize(5)
    turtle.write("O")
    turtle.pensize(2)
    turtle.color("purple")
    length = radius
    turtle.goto(length,length)
    turtle.down()
    turtle.goto(length,-length)
    turtle.goto(-length,-length)
    turtle.goto(-length,length)
    turtle.goto(length,length)
#
# plot pentagram
#
def pPentagram(turtle,centerX,centerY,radius):
    turtle.up()
    turtle.goto(centerX,centerY)
    turtle.color("red")
    turtle.pensize(5)
    turtle.write("O")
    turtle.pensize(2)
    turtle.color("purple")
    length = radius
    turtle.goto(length,length)
    turtle.down()
    turtle.goto(length,-length)
    turtle.goto(-length,-length)
    turtle.goto(-length,length)
    turtle.goto(length,length)
################################################################################################### 
#def main():   
#    nt = turtle.Turtle()   # Make a new turtle, initialize values
#    nt.setheading(20)
#    nt.pensize(2)
#    #nt.color(random.randrange(256),random.randrange(256),random.randrange(256))
#    nt.speed(10)
#    pCircle(10,10,300)
#main()
