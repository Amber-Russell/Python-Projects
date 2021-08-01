#this code is protected
class Safe:
    def __init__(self):
        self._safeVar = 0

obj = Safe()
obj._safeVar =72
print(obj._safeVar)
#The output will show 72, the program works with the last value assigned to a variable 

class Security:
    def __init__(self):
        self.__securityVar = 20

    def getSecurity(self):
        print(self.__securityVar)

    def setSecurity(self, private):
        self.__securityVar = private

obj = Security()
obj.getSecurity()
obj.setSecurity(92)
obj.getSecurity()
        
#Security is denoted with a double underscore prefix. This makes it so
#that private cannot be changed unless it is on purpose, the out put will
#produce both values.
