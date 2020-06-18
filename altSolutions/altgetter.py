import urllib.request
import sys

def getAllBytes(request):
    print("i'll read all your bytes")
    allBytes = request.read(10000)
    byteLength = len(allBytes)
    while (byteLength > 0):
        tempBytes = request.read(10000)
        allBytes += tempBytes
        byteLength = len(tempBytes)
        print(byteLength)
    return allBytes

# print(sys.argv[1])
arrayLength = len(sys.argv)

if arrayLength < 2:
    print("can\'t continue - no args")
    exit()

webpage = sys.argv[1]
if len(sys.argv) == 3:
    byteCount = int(sys.argv[2])
else:
    byteCount = 500

request = urllib.request.urlopen(webpage)
contentLength = request.getheader('Content-Length')
print(str(contentLength))

if contentLength is not None:
    byteCount = int(contentLength)
    print("Reading " + str(byteCount) + " bytes.")
    bytesRead = request.read(byteCount)
else:
    bytesRead = getAllBytes(request)
    byteCount = len(bytesRead)
    print("Reading " + str(byteCount) + " bytes.")

allHeaders = request.getheaders()
# print(allHeaders)
contentHeaderValue = request.getheader('Content-Type')
print(contentHeaderValue)
textEncoding = contentHeaderValue.split("=")[1]

# urllib.request.urlopen(webpage).get_header(header_name, default=None)
stringFromBytes = bytesRead.decode(textEncoding)
f = open("first.htm", "w")
f.write(stringFromBytes)
f.close()
