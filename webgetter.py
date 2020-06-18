import urllib.request
import sys


print("doing something")

print(sys.argv)

arguments = sys.argv
argLength = len(sys.argv)

print(argLength)

if argLength < 2:
    print("need more args")
    exit()

print ("you made it")

webUrl = arguments[1]
print(webUrl)

webPage = urllib.request.urlopen(webUrl).read(500)
print(webPage)