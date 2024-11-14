from django.urls import re_path
from Streak import consumers

# We call the as_asgi() classmethod in order to get an ASGI application that will 
# instantiate an instance of our consumer for each user-connection
websocket_urlpatterns = [
	re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]




