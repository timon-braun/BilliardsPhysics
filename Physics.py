from numpy import *
from scipy.optimize import fsolve

from Ball import *
from Bank import *

class Physics(object):
    """Contains functions for physics calculations and more"""
    #bankList = []
    #ballList = []

    #def __init__(self, bankList, ballList):
    #    self.bankList = bankList
    #    self.ballList = ballList

    def BankCollision(self, Ball, bankList):
        for bank in bankList:
            bank = bank

    def BallCollisionTime(self, Ball1, Ball2):
        x1 = Ball1.getXLocation()
        y1 = Ball1.getYLocation()
        v1 = Ball1.getVelocity()
        th1 = Ball1.getDirection()
        
        x2 = Ball2.getXLocation()
        y2 = Ball2.getYLocation()
        v2 = Ball2.getVelocity()
        th2 = Ball2.getDirection()

        r = 2.85

        f0 = (x1**2 - 2*x1*x2 + x2**2) + (y1**2 - 2*y1*y2 + y2**2) - 4*(r**2)
        f1 = (2 * (x1 - x2) * (cos(th1)*v1 + cos(th2)*v2)) + (2 * (y1 - y2) * (sin(th1)*v1 + sin(th2)*v2))
        f2 = v1**2 - 2*cos(th1-th2)*v1*v2 + v2**2

        f = lambda t: f0 + f1*t + f2*(t**2)

        funcRoot = fsolve(f, 0.1)

        if (0.01 <= funcRoot < 0.1):
            return funcRoot
        else:
            return 0.1
