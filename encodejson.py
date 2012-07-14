import json

data = [ {u'category': 0, u'times_viewed': 721, u'description': '', u'rating': 98.3, u'favorites_count': 70, u'created_at': u'2012-07-14T04:33:02-04:00', u'privacy': False, u'image_url': u'http://pcdn.500px.net/9733203/65974a495e176773ed50a909ad7c6762fc0fbf5e/2.jpg', u'nsfw': False, u'height': 665, u'width': 1000, u'votes_count': 136, u'user': {u'username': u'Silaphop', u'city': u'Rayong City', u'userpic_url': u'http://acdn.500px.net/243701.jpg', u'firstname': u'Silaphop', u'lastname': u'Pongsai', u'upgrade_status': 0, u'country': u'Thailand', u'fullname': u'Silaphop Pongsai', u'id': 243701}, u'comments_count': 82, u'id': 9733203, u'name': u'Sunset'} ]
print 'DATA:', repr(data)

data_string = json.dumps(data)
print 'JSON:', data_string