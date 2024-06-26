#external libraries
from graphics import *
from numpy import *

#separate Files
from Ball import *
from Bank import *
from Physics import *



#Pooltable Graphics
pooltable = GraphWin("Pool Table", 1048, 600) #1px=0.25cm
pooltable.setBackground("green4")



#Bank Setup
topBank = Bank()
topBank.setSide("TopBank")
topBank.setLocation1(76.0, 76.0)
topBank.setLocation2(972.0, 76.0)

rightBank = Bank()
rightBank.setSide("RightBank")
rightBank.setLocation1(972.0, 76.0)
rightBank.setLocation2(972.0, 524.0)

bottomBank = Bank()
bottomBank.setSide("BottomBank")
bottomBank.setLocation1(972.0, 524.0)
bottomBank.setLocation2(972.0, 524.0)

leftBank = Bank()
leftBank.setSide("LeftBank")
leftBank.setLocation1(972.0, 524.0)
leftBank.setLocation2(76.0, 76.0)

bankList = [topBank, rightBank, bottomBank, leftBank]



#Ball Setup
Cueball = Ball()
Cueball.setSuit("Cueball")
Cueball.setLocation(56.0, 56.0)

Oneball = Ball()
Oneball.setSuit("Oneball")
Oneball.setColor("yellow")
Oneball.setLocation(168.0, 56.0)

ballList = [Cueball, Oneball]

#Bank Visuals
topBankGraphic = Polygon(Point(0,0), Point(1048,0), Point(972, 76), Point(76, 76))
rightBankGraphic = Polygon(Point(1048,0), Point(1048,600), Point(972, 524), Point(972, 76))
bottomBankGraphic = Polygon(Point(0,600), Point(1048,600), Point(972, 524), Point(76, 524))
leftBankGraphic = Polygon(Point(0,0), Point(0,600), Point(76, 524), Point(76, 76))

topBankGraphic.setFill("green")
rightBankGraphic.setFill("green")
bottomBankGraphic.setFill("green")
leftBankGraphic.setFill("green")

topBankGraphic.draw(pooltable)
rightBankGraphic.draw(pooltable)
bottomBankGraphic.draw(pooltable)
leftBankGraphic.draw(pooltable)

#Ball Visuals
Cueball.drawBall(pooltable)
Oneball.drawBall(pooltable)

#"Cue" Input
Cueball.setVelocity(100)
Cueball.setDirection(1)

#Physics Mod
Calc = Physics()

stopKey = ""
while (stopKey != "a"):
    stopKey = pooltable.getKey()

    t = 0.1
    tNew = Calc.BallCollisionTime(Cueball, Oneball)
    if (tNew < t):
        t = tNew
    print ("timeStep: " + str(t))
    print ("")

    Cueball.iterate(t, Oneball)
    Oneball.iterate(t, Cueball)
    Cueball.info()
    

pooltable.close()