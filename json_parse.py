import urllib2
import json

def printResults(data):
    theJSON = json.loads(data)
    #if "node" in theJSON["nodes"]:
    #print(json.dumps(theJSON, indent=4))
    for i in theJSON["nodes"]:
        title = i["node"]["title"]
        barco = i["node"]["barco"]
        fecha = i["node"]["fecha"]
        total = i["node"]["total"]
        lat = i["node"]["lat"]
        long = i["node"]["long"]
        print str(title), str(barco), str(fecha), str(total), str(lat), str(long)

urlData = "http://www.mazpesca.com/feeds/json/reporte-diario.json"
webUrl = urllib2.urlopen(urlData)
print webUrl.getcode()
if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
else:
    print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())
