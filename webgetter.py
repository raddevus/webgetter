import urllib.request
import sys
import io
import codecs

def multiply(x,y):
    return x*y

def getBytes():
    print("I'm in getBytes")
    return 55

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

request = urllib.request.urlopen(webUrl)
contentTypeHeader = request.getheader('content-type')
contentTypeSplit = contentTypeHeader.split('=')
contentType = contentTypeSplit[1]
contentLength = request.getheader('content-length')

if contentLength is not None:
    webPage = request.read(int(contentLength))
else:
    webPage = request.read(1000000)

webCode = webPage.decode(contentType)

f = io.open("/Users/andydeutsch/Files/Python/webgetter/webPage.htm","w+")
f.write(webCode)
f.close()

print(multiply(10.325,20))