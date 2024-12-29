class uppercase:
    def __init__(self):
        self.str=""
    def getstring(self):
        self.str=input("enter a string")
    def printstring(self):
        print("result",self.str.upper())
object=uppercase()
object.getstring()
object.printstring()