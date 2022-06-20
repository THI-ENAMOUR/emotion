#!/usr/bin/env python3

import requests
import rospy
from std_msgs.msg import String

# Publisher Message Format:
# '{"expression:" "<type>"}'
# e.g. with rostopic command:
# rostopic pub /cmd_facial_expression std_msgs/String \
# "data: '{\"expression\": \"default\"}'"

URL = "http://localhost:5000/"
HEADERS = {"content-type": "application/json"}


def callback_sound(data):
    try:
        requests.post(URL + "sound", json=data.data, headers=HEADERS)
    except Exception as exp:
        print("Post to server unsuccessful", exp)

def callback_display(data):
    try:
        requests.post(URL + "display", json=data.data, headers=HEADERS)
    except Exception as exp:
        print("Post to server unsuccessful", exp)


def start_listener():

    rospy.init_node("sound_display_uxd")
    # Get cmd from backend controller
    
    rospy.Subscriber("sound", String, callback_sound)
    rospy.Subscriber("display", String, callback_display)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == "__main__":
    start_listener()
