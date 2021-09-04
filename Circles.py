import turtle as t
import random
import uuid
import io
from pil import Image

#setup screensize, speed, background color from array and hide t
scrnSz = 1000
t.screensize(canvwidth=scrnSz, canvheight=scrnSz)
t.speed(0)
t.hideturtle()
colorsBkg = ["dim grey", "dark cyan", "chocolate", "rosy brown", "indian red", "steel blue", "salmon", "light salmon", "cadet blue"]
backgroundColor = random.choice(colorsBkg)
t.bgcolor(backgroundColor)


#array of colors for strokes
colorsStrk = ["maroon", "maroon", "light blue", "misty rose", "black", "powder blue", "bisque", "powder blue"]


#number of circles, angle to rotate such that 360 is the sum on completion
numCirclesOne = [[1, 0]]
numCircles = [[6, 60], [3, 120], [7, 51.43], [5, 72], [4,90], [2, 180]]
numCirclesMany = [[9, 40], [10, 36], [12, 30]]
numCirclesMore = [[20, 18], [30, 12], [36, 10]]
numCirclesMega = [[72, 5], [120, 3]] 
    

def make_circles(strokeColor):

    #random int defining which if statement to run
    circArray = random.randrange(1,100,1)

    #each if statment checks for which array to use, determining the number/size of circles
    #1-10, 1 circle
    if (circArray <= 10):
        t.width(random.randrange(4,5,1))
        numCirChoice = random.choice(numCirclesOne)
        for i in range(numCirChoice[0]):
            #set stroke and fill color
            t.color(random.choice(colorsStrk), backgroundColor)
            #get radius as size, move south length of radius
            size = random.randrange((int)(scrnSz*0.006), (int)(scrnSz*0.7), 3)
            #draw circle
            t.up()
            t.home()
            t.setposition(random.randrange(-400,400,1), random.randrange(-700,400,1))
            t.down()
            t.begin_fill()
            t.circle(size)
            t.end_fill()
            t.right(numCirChoice[1])

    #11-60, 2-7 circles
    if (11 <= circArray <= 60):
        t.width(random.randrange(3,4,1))
        numCirChoice = random.choice(numCircles)
        for i in range(numCirChoice[0]):
            t.color(random.choice(colorsStrk), backgroundColor)
            t.circle(random.randrange((int)(scrnSz*0.006), (int)(scrnSz*0.7), 3))
            t.right(numCirChoice[1])

    #61-80, 9-12 circles
    if (61 <= circArray <= 80):
        t.width(random.randrange(2,3,1))
        numCirChoice = random.choice(numCirclesMany)
        for i in range(numCirChoice[0]):
            t.color(random.choice(colorsStrk), backgroundColor)
            t.circle(random.randrange((int)(scrnSz*0.006), (int)(scrnSz*0.7), 3))
            t.right(numCirChoice[1])


    #81-95, 20-36 circles
    if (81 <= circArray <= 95):
        t.width(random.randrange(2,3,1))
        numCirChoice = random.choice(numCirclesMore)
        for i in range(numCirChoice[0]):
            t.color(random.choice(colorsStrk), backgroundColor)
            t.circle(random.randrange((int)(scrnSz*0.006), (int)(scrnSz*0.7), 3))
            t.right(numCirChoice[1])

    #96-100, 72 120 180 circles
    if (96 <= circArray <= 100):
        t.width(2)
        numCirChoice = random.choice(numCirclesMega)
        for i in range(numCirChoice[0]):
            t.color(random.choice(colorsStrk), backgroundColor)
            t.circle(random.randrange((int)(scrnSz*0.006), (int)(scrnSz*0.7), 3))
            t.right(numCirChoice[1])


def paint_canvas(dummy_x=0, dummy_y=0):
    #runs the program
    make_circles(colorsStrk)
    t.onscreenclick(paint_canvas)


paint_canvas()

uniqueFilename = str(uuid.uuid4().hex)

#remove when run automatically
t.exitonclick()
