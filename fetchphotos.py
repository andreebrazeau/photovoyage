import sys
import os
import urllib
from StringIO import StringIO
from fivehundred import *
import re

CONSUMER_KEY = '7ok4JQfbUoVaXlcZXRM7soSG6TlC97XnLSZMiB0j'
def main():
    # global PHOTOS
    pl = getpx()
    sfw = sfw_screen(pl)
    top10 = top_10(sfw)
    top_name = top_url(top10)
    front_end_output(top_name,pl)

def getpx():
    photolist = []
    api = FiveHundredPx(CONSUMER_KEY)
    photos = api.get_photos(feature='popular',limit=50)
    # print "getpx()", photos
    # return photos
    for p in photos:
        photolist.append(p)
    print photolist
    return photolist
        
    #     thumbnail_url = p['image_url']
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


# photolist = [{}, {}, {}]
def sfw_screen(photolist):
    sfw_px = []
    p_tuples = ()

    for photo in photolist:
    # screen out nsfw ones
      if photo['nsfw'] != True:
        #p_tuples = (rating, image_url)
        p_tuple = (photo['rating'],photo['image_url'])
        print "p_tuple", p_tuple
        sfw_px.append(p_tuple)
        # sfw_px becomes a list of (tuples)
        print "sfw_screen", sfw_px
    sorted_px = sorted(sfw_px)
    return sorted_px

    # return top 10 highest rated pictures by image_url 
def top_10(sorted_px):
    top_10 = sorted_px[0:10]
    return top_10

    # replace image_url "....2.jpg" as "....4.jpg"
def top_url(top_10):
    updated_url_list = []
    original_url_dict = {}
    for top_tuple in top_10:
      original_url = top_tuple[1]
      updated_url_in_tuple = (top_tuple[0],original_url.replace("/2.jpg", "/4.jpg"))
      updated_url_list.append(updated_url_in_tuple)
      original_url_dict[top_tuple[1]] = top_tuple[0]
    print "UPDATED URL LIST", updated_url_list
    print "Original URL Dictionary", original_url_dict
    return original_url_dict

    # return rating, height and width for front end editing/collaging
def front_end_output(original_url_dict,photolist):
    fe_output_list = []
    fe_output = {}
    # dictionary of 
    # rating = updated_url_list[0], height = , width and URL = updated_url_list[1]
    for k,v in original_url_dict.items():
      # for k in original_url_dict:
      # if original_url == photolist["image_url"] ???
      for photo in photolist:
        if k == photo[u'image_url']:
          print photo[u'height'], photo[u'width']
          fe_output[u'image_url'] = k.replace("/2.jpg", "/4.jpg")
          fe_output[u'rating'] = v
          fe_output[u'height'] = photo[u'height']
          fe_output[u'width'] = photo[u'width']
          fe_output_list.append(fe_output)
      print fe_output_list

# u'http://pcdn.500px.net/9730333/51f0d05f78152fec3063686b93c068d3e25586ef/2.jpg': 98.4


      # height = p["height"]

# {u'category': 0, u'times_viewed': 721, u'description': '', u'rating': 98.3, u'favorites_count': 70, u'created_at': u'2012-07-14T04:33:02-04:00', u'privacy': False, u'image_url': u'http://pcdn.500px.net/9733203/65974a495e176773ed50a909ad7c6762fc0fbf5e/2.jpg', u'nsfw': False, u'height': 665, u'width': 1000, u'votes_count': 136, u'user': {u'username': u'Silaphop', u'city': u'Rayong City', u'userpic_url': u'http://acdn.500px.net/243701.jpg', u'firstname': u'Silaphop', u'lastname': u'Pongsai', u'upgrade_status': 0, u'country': u'Thailand', u'fullname': u'Silaphop Pongsai', u'id': 243701}, u'comments_count': 82, u'id': 9733203, u'name': u'Sunset'} 







if __name__ == '__main__':
    main()
