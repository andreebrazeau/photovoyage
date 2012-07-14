# -*- coding: utf-8 -*-

import sys
import os
import urllib
import urllib2
from StringIO import StringIO
from fivehundred import *
import json
# import soundcloud

CONSUMER_KEY = '7ok4JQfbUoVaXlcZXRM7soSG6TlC97XnLSZMiB0j'
def main():
    # global PHOTOS
    pl = getpx('san francisco')
    sfw = sfw_screen(pl)
    top_list = top_px(sfw,25)
    top_name = top_url(top_list)
    fe = front_end_output(top_name,pl)

# def getcities(city_string):

def getpx(city_name):
    photolist = []


    url = "https://api.500px.com/v1/photos/search?rpp=100&term=" + city_name + "&consumer_key=" + CONSUMER_KEY 
    response = None
    # try:
    file = urllib2.urlopen(url)
    readfile = file.read()
    # try: 
    response = json.loads(readfile)
    photos = response['photos']
    # print "PHOTO", photos

    for p in photos:
        photolist.append(p)
    return photolist

# photolist = [{}, {}, {}]
def sfw_screen(photolist):
  sfw_px = []
  p_tuples = ()
  category_list = [9,8,21,13,27,22]
  for photo in photolist:
  # screen out nsfw ones
    if photo['nsfw'] == False and photo['category'] in category_list:
      #p_tuples = (rating, image_url)
      p_tuple = (photo['rating'],photo['image_url'])
      # print "p_tuple", p_tuple
      sfw_px.append(p_tuple)
      # sfw_px becomes a list of (tuples)
      # print "sfw_screen", sfw_px
  sorted_px = sorted(sfw_px)
  return sorted_px

def top_px(sorted_px,n):
  # return top 10 highest rated pictures by image_url 
  top_list = sorted_px[0:n]
  return top_list

def top_url(top_10):
  # replace image_url "....2.jpg" as "....4.jpg"
  updated_url_list = []
  original_url_dict = {}
  for top_tuple in top_10:
    original_url = top_tuple[1]
    updated_url_in_tuple = (top_tuple[0],original_url.replace("/2.jpg", "/4.jpg"))
    updated_url_list.append(updated_url_in_tuple)
   
    original_url_dict[top_tuple[1]] = top_tuple[0]
  # print "Original URL Dictionary", original_url_dict
  return original_url_dict

def front_end_output(original_url_dict,photolist):
  # create a list of dictionary. each item in dictionary contains rating, height, width and image_url
  fe_output_list = []

  for photo in photolist:
    if photo['image_url'] in original_url_dict:
      fe_output = {}
      # print photo[u'height'], photo[u'width']
      fe_output['url'] = photo['image_url'].replace("/2.jpg", "/4.jpg")
      fe_output['height'] = photo['height']
      fe_output['width'] = photo['width']
      fe_output['link_URL'] = "http://www.500px.com/photo/"+str(photo['id'])
      ## add original page ##
      fe_output_list.append(fe_output) 

  data_string = json.dumps(fe_output_list)
  print data_string
  return data_string

# u'http://pcdn.500px.net/9730333/51f0d05f78152fec3063686b93c068d3e25586ef/2.jpg': 98.4


      # height = p["height"]


# {u'category': 0, u'times_viewed': 721, u'description': '', u'rating': 98.3, u'favorites_count': 70, u'created_at': u'2012-07-14T04:33:02-04:00', u'privacy': False, u'image_url': u'http://pcdn.500px.net/9733203/65974a495e176773ed50a909ad7c6762fc0fbf5e/2.jpg', u'nsfw': False, u'height': 665, u'width': 1000, u'votes_count': 136, u'user': {u'username': u'Silaphop', u'city': u'Rayong City', u'userpic_url': u'http://acdn.500px.net/243701.jpg', u'firstname': u'Silaphop', u'lastname': u'Pongsai', u'upgrade_status': 0, u'country': u'Thailand', u'fullname': u'Silaphop Pongsai', u'id': 243701}, u'comments_count': 82, u'id': 9733203, u'name': u'Sunset'} 


if __name__ == '__main__':
    main()
