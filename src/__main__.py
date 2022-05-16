#!/usr/bin/env python2.7
import json

import rospy
from std_msgs.msg import String

from processor import process_intent


class Intent:
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

class TestData:
    def __init__(self, data):
        self.data = data

def receive_data(data):
    json_string = data.data
    print(json_string)
    intent = parse_json(json_string)
    print("{name} {confidence}".format(name=intent.name, confidence=intent.confidence))
    action_request = process_intent(intent)
    publish_action(action_request)

publisher = rospy.Publisher("/action", String, queue_size=10)
def publish_action(request):
    json_data = request.to_json()
    try:
        json.loads(json_data)
    except BaseException as e:
        print("Json is not of valid format: " + str(e))
    publisher.publish(json_data)
    print(json_data)

def parse_json(json_string):
    data = json.loads(json_string)
    intent = Intent(name=data['intent']['name'], confidence=data['intent']['confidence'])
    return intent

if __name__ == "__main__":
    rospy.init_node("uxd_core")
    rospy.Subscriber("/intent", String, receive_data)
    rospy.spin()
    # receive_data(TestData("""
    #                         {
    #                             "intent":{
    #                             "name":"Move",
    #                             "confidence": 1
    #                         }
    #                     }
    #                         """))
