    #!/usr/bin/python

import urllib2


def main():
    print "Hello World.."
    url = 'https://developer.yahoo.com/'
    
    try:
	    conn = urllib2.urlopen(url)
	    #print "Http responce: %s" % conn.info()
	    print "Http responce code: %d" % conn.getcode()
	    data = conn.read()
    
    except urllib2.HTTPError, e:
	    print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
	    print "Network error: %s" % e.reason.args[1]

if __name__ == '__main__':
    main()