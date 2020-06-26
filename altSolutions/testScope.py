
def doThing( number):
    print ("it works")
    print("number : " + str(number) )
    print (extra)



extra = 254
print (extra)

doThing( 3)

extra = "superstar"
print (extra)
class Member:
    def __init__(self,x):
        print("I am inited")
        print ("extra in Member class : " + extra)
    
    def doThing(self):
        print ("did a Member thing")

m = Member(3)

m.doThing()
