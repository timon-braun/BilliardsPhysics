from numpy import *
from graphics import *

class Ball:
    """Creates a Ball with necessary variables"""
    suit = "Ball"
    color = "white"
    weight = .160 #kg
    radius = 2.85 #cm
    xCoord = 0.0 #cm
    yCoord = 0.0 #cm
    velocity = 0.0 #cm/s
    direction = 0.0
    rotationSpeed = 0.0
    rotationAngle = 0.0
    graphic = Circle(Point(xCoord, yCoord), radius*4)

    #Physics Constants
    slidingFriction = 0.2
    rollingFriction = 0.01
    bankRestitution = 0.75
    """ball mass moment of inertia: 2/5 mR2
    ball-ball coefficient of friction (μ): 0.03-0.08
    ball-ball coefficient of restitution (e): 0.92-0.98
    ball-cloth coefficient of rolling resistance (μ): 0.005 – 0.015
    ball-cloth coefficient of sliding friction (μ): 0.15-0.4 (typical value: 0.2)
    ball-cloth spin deceleration rate: 5-15 rad/sec2
    ball-rail coefficient of restitution (e): 0.6-0.9
    ball-table coefficient of restitution (e): 0.5
    cue-tip-ball coefficient of friction (μ): 0.6"""
    
    #Performs all actions for the next t seconds
    def iterate(self, t, ball):
        self.moveBall(t)
        self.MomentumRolling(t)
        self.BankCollision()
        self.BallCollision(ball)

    #Calculates change in velocity after t seconds, based on sliding friction (no rotation)
    def MomentumSliding(self, t):
        self.velocity -= (self.slidingFriction * (980.665 * self.weight)) * 10 * t
        if self.velocity < 0:
            self.velocity = 0

    #Calculates change in velocity after t seconds, based on rolling friction (no rotation)
    def MomentumRolling(self, t):
        self.velocity -= (self.rollingFriction * (980.665 * self.weight)) * 10 * t
        if self.velocity < 0:
            self.velocity = 0

    #Checks and executes collision with a bank
    def BankCollision(self):
        #left bank
        if (self.xCoord <= self.radius) & (90 < self.direction < 270):
            self.direction = 180 - self.direction
            self.NormalizeDirection()
            self.velocity *= self.bankRestitution
        #right bank
        if (self.xCoord >= 224 - self.radius) & ((270 < self.direction) | (self.direction < 90)):
            self.direction = 180 - self.direction
            self.NormalizeDirection()
            self.velocity *= self.bankRestitution
        #top bank
        if (self.yCoord <= self.radius) & (180 < self.direction < 360):
            self.direction = -self.direction
            self.NormalizeDirection()
            self.velocity *= self.bankRestitution
        #bottom bank
        if (self.yCoord >= 112 - self.radius) & (0 < self.direction < 180):
            self.direction = -self.direction
            self.NormalizeDirection()
            self.velocity *= self.bankRestitution

    #checks for collision with ball
    def BallCollision(self, ball):
        xb = ball.getXLocation()
        yb = ball.getYLocation()

        dist = (xb - self.xCoord)**2 + (yb - self.yCoord)**2
        aoc = (yb - self.yCoord) / (xb - self.xCoord)

        if (dist < (2*self.radius+0.01)):

            if (self.velocity != 0):
                if (abs(aoc + 90 - self.direction)) < (abs(aoc - 90 - self.direction)):
                    self.direction = aoc + 90
                    self.NormalizeDirection()
                else:
                    self. direction = aoc - 90
                    self.NormalizeDirection()
            else:
                self.direction = aoc
                self.velocity = ball.getVelocity()

    
    #if direction is not between 0 and 360, corrects accordingly
    def NormalizeDirection(self):
        while (self.direction < 0):
            self.direction += 360
        while (self.direction > 360):
            self.direction -= 360

    #draws the Ball in the Graphics Interface
    def drawBall(self, pooltable):
        self.graphic = Circle(Point(76 + (4 * self.xCoord), 76 + (4 * self.yCoord)), self.radius*4)
        self.graphic.setOutline(self.color)
        self.graphic.setFill(self.color)
        self.graphic.draw(pooltable)

    #Moves ball to it's location t seconds later at current velocity
    def moveBall(self, t):
        changeX = (cos(radians(self.direction)) * self.velocity) * t
        changeY = (sin(radians(self.direction)) * self.velocity) * t
        self.xCoord += changeX
        self.yCoord += changeY
        self.graphic.move(int(4 * changeX), int(4 * changeY))

    #Get object info
    def info(self):
        print ("Suit: " + self.suit)
        print ("Color: " + self.color)
        print ("Weight: " + str(self.weight))
        print ("Radius: " + str(self.radius))
        print ("Location: (" + str(self.xCoord) + ", " + str(self.yCoord) + ")")
        print ("Velocity: " + str(self.velocity))
        print ("Direction: " + str(self.direction))
        print ("Rotation Speed (TBD): " + str(self.rotationSpeed))
        print ("Rotation Angle (TBD): " + str(self.rotationAngle))
        print ("")
        
    #Set variable values
    def setSuit(self, val):
        self.suit = val
    def setColor(self, val):
        self.color = val
    def setWeight(self, val):
        self.weight = val
    def setRadius(self, val):
        self.radius = val
    def setLocation(self, valX, valY):
        self.xCoord = valX
        self.yCoord = valY
    def setVelocity(self, val):
        self.velocity = val
    def setDirection(self, val):
        self.direction = val
    def setRotationSpeed(self, val):
        self.rotationSpeed = val
    def setRotationAngle(self, val):
        self.rotationAngle = val

    #Get variable values
    def getSuit(self):
        return self.suit
    def getColor(self):
        return self.color
    def getWeight(self):
        return self.weight
    def getRadius(self):
        return self.radius
    def getXLocation(self):
        return self.xCoord
    def getYLocation(self):
        return self.yCoord
    def getVelocity(self):
        return self.velocity
    def getDirection(self):
        return self.direction
    def getRotationSpeed(self):
        return self.rotationSpeed
    def getRotationAngle(self):
        return self.rotationAngle





