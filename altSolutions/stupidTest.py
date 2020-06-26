import sample

def printGlobal():
   print(str(extra))

extra = 35
printGlobal() # prints 35
extra = "Python are stupid."

class Arsinine:
   def __init__(self):
      print(extra)

a = Arsinine() # prints Python are stupid.

s = sample.Sample()