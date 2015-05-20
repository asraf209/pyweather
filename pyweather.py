#!/usr/bin/python

# API Key: b0db249f8c79a7d7b581c4a7581d6bdf (openweather)
# API Key: 2436ae911a0de75b8a932e6bd7edb    (weatherapi)


import urllib2
import sys

def get_response(url):
    print "Hello World.."
    try:
        conn = urllib2.urlopen(url)
        print "Http responce code: %d" % conn.getcode()
        #print "Http responce: %s" % conn.info()        
        data = conn.read()
        return data	    
    except urllib2.HTTPError, e:
	    print "HTTP error: %d" % e.code
	    return None
    except urllib2.URLError, e:
	    print "Network error: %s" % e.reason.args[1]
	    return None
    except:
        print "Unexpected error: ", sys.exec_info()[0]
        return None


def process_data(data):
    print data

    
def main():
    url = 'http://api.worldweatheronline.com/free/v2/weather.ashx?key=2436ae911a0de75b8a932e6bd7edb&q=48.85,2.35&num_of_days=2&tp=3&format=json'
    #response = get_response('https://developer.yahoo.com/')
    #response = get_response('http://api.openweathermap.org/data/2.5/weather?q=Evanston,IL')
    response = get_response(url)
    if response != None:
        process_data(response)


if __name__ == '__main__':
    main()