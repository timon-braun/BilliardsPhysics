class Bank:
    """Creates Bank with necessary variables"""
    side = "Bank"
    friction = 0.0
    compression = 0.0
    xCoord1 = 0.0
    yCoord1 = 0.0
    xCoord2 = 0.0
    yCoord2 = 0.0



    #Get object info
    def info(self):
        print ("Side: " + self.side)
        print ("Friction: " + str(self.friction))
        print ("Compression: " + str(self.compression))
        print ("Location1: (" + str(self.xCoord1) + ", " + str(self.yCoord1) + ")")
        print ("Location2: (" + str(self.xCoord2) + ", " + str(self.yCoord2) + ")")
        print ("")
        
    #Set variable values
    def setSide(self, val):
        self.side = val
    def setFriction(self, val):
        self.friction = val
    def setCompression(self, val):
        self.compression = val
    def setLocation1(self, valX, valY):
        self.xCoord1 = valX
        self.yCoord1 = valY
    def setLocation2(self, valX, valY):
        self.xCoord2 = valX
        self.yCoord2 = valY

    #Get variable values
    def getSide(self):
        return self.side
    def getFriction(self):
        return self.friction
    def getCompression(self):
        return self.compression
    def getXLocation1(self):
        return self.xCoord1
    def getYLocation1(self):
        return self.yCoord1
    def getXLocation2(self):
        return self.xCoord2
    def getYLocation2(self):
        return self.yCoord2
