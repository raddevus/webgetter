
def doThing(extra, number):
    print ("it works")
    print (extra)



extra = 254
print (extra)

doThing("first", 3)

class Member:
    def __init__(self,x):
        print("I am inited")
    
    def doThing(self):
        print ("did a Member thing")

m = Member(3)

m.doThing()
