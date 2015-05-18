#!/usr/bin/python
import urllib2

def get_response(url):
    print "Hello World.."
    try:
	    conn = urllib2.urlopen(url)
	    #print "Http responce: %s" % conn.info()
	    print "Http responce code: %d" % conn.getcode()
	    data = conn.read()
    
    except urllib2.HTTPError, e:
	    print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
	    print "Network error: %s" % e.reason.args[1]
	    
def main():
    response = get_response('https://developer.yahoo.com/')

if __name__ == '__main__':
    main()