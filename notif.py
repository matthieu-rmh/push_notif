#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

from pushbullet import PushBullet
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import time

# Get the access token from Pushbullet.com
access_token = "o.CMYsTKFMNpY14LhUAm0vkHAhh0UV4lOq"

# Taking input from the user
data = input('Title')

# Taking large text input from the user
text = textarea(
"Text", rows=3, placeholder="Une notification",
required=True)

# Get the instance using the access token
pb = PushBullet(access_token)

# Send the data by passing the main title
# and text to be send
push = pb.push_note(data, text)

# Put a success message after sending
# the notification
put_success("Message sent successfully...")

# Sleep for 3 seconds
time.sleep(3)

# Clear the screen
clear()

# Give the pop at last
toast("Thanks for using it :)")

# hold the session until the whole work finishes
hold()