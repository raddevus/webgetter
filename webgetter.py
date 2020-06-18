import urllib.request
import sys


print("doing something")

print(sys.argv)

arguments = sys.argv
argLength = len(sys.argv)

print("Number of args: " + str(argLength))

if argLength < 2:
    print("Needs more args")
    exit()

print ("There are enough args")

webUrl = arguments[1]
print(webUrl)

webPage = urllib.request.urlopen(webUrl).read(500)
print(webPage)