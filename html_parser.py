from HTMLParser import HTMLParser

metacount = 0;
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        global metacount
        print "Encountered a start tag: ", tag
        if tag == "meta":
            metacount += 1
        
        pos = self.getpos()
        print "At line: ", pos[0], " position ", pos[1]
        if attrs.__len__ > 0:
            print "\tAttributes:"
            for a in attrs:
                print "\t", a[0], "=", a[1]
    
    def handle_endtag(self, tag):
        print "Encountered an end tag: ", tag
        pos = self.getpos()
        print "At line: ", pos[0], " position ", pos[1]
        
    def handle_data(self, data):
        print "Encountered some data: ", data
        pos = self.getpos()
        print "At line: ", pos[0], " position ", pos[1]
    
    def handle_comment(self, data):
        print "Encountered comment: ", data
        pos = self.getpos()
        print "At line: ", pos[0], " position ", pos[1]
        
parser = MyHTMLParser()
f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()
    parser.feed(contents)
    
print "%d meta tags encountered" % metacount
