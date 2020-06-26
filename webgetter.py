import urllib.request
import sys
import io
import codecs

def getAllBytes(request):
    allBytes = request.read(10000)
    byteLength = len(allBytes)
    while (byteLength > 0):
        tempBytes = request.read(10000)
        allBytes += tempBytes
        byteLength = len(tempBytes)
        print(byteLength)
    return allBytes

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

requestX = urllib.request.urlopen(webUrl)
contentTypeHeader = requestX.getheader('content-type')
contentTypeSplit = contentTypeHeader.split('=')
contentType = contentTypeSplit[1]
contentLength = requestX.getheader('content-length')

if contentLength is not None:
    webPage = requestX.read(int(contentLength))
    print("There is a content length!")
else:
    webPage = getAllBytes(requestX)
    print("There is not a content length!")

webCode = webPage.decode(contentType)

f = io.open("/Users/andydeutsch/Files/Python/webgetter/webPage.htm","w+")
f.write(webCode)
f.close()