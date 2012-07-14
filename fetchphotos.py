import sys
import os
import urllib
from StringIO import StringIO
from fivehundred import *

CONSUMER_KEY = '7ok4JQfbUoVaXlcZXRM7soSG6TlC97XnLSZMiB0j'
def main():
    api = FiveHundredPx(CONSUMER_KEY)
    photos = api.get_photos(feature='popular',only=["city and architecture","travel","urban exploration","transportation","street"],limit=50)
    for p in photos:
        print p
        thumbnail_url = p['image_url']
        # fhpx_url = 'https://api.500px.com/v1/photos?feature=popular' 
        
      #   try:
      #       fileio = urllib.urlopen(thumbnail_url)
      #       im = StringIO(fileio.read())
      #       # if you have PIL you can play with the image
      #       #img = Image.open(im)
      #       print '(%s,%s)' % (thumbnail_url,fhpx_url)
      #   except Exception, e:
		    # print 'Error in the following url[%s]:%s' % (thumbnail_url,e)
		    # continue


if __name__ == '__main__':
	main()
