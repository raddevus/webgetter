import urllib.request
import sys
import io
import codecs


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

request = urllib.request.urlopen(webUrl)
contentTypeHeader = request.getheader('content-type')
print(contentTypeHeader)

webPage = request.read(1000000)
webCode = webPage.decode('utf-8')

f = io.open("/Users/andydeutsch/Files/Python/webgetter/webPage.htm","w+")
f.write(webCode)
f.close()



