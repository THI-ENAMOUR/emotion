#!/usr/bin/env python2.7
import json
import rospy
from std_msgs.msg import String

from processor import process_intent, to_json

class Intent:
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

def receive_data(data):
    json_string = data.data
    print(json_string)
    intent = parse_json(json_string)
    print("{name} {confidence}".format(name=intent.name, confidence=intent.confidence))
    action_request = process_intent(intent)
    
    if action_request is not None:
        publish_action(action_request)


publisher = rospy.Publisher("/action", String, queue_size=10)
def publish_action(request):
    json_data = to_json(request)
    publisher.publish(json_data)
    print("Publishing data: " + json_data)

def parse_json(json_string):
    data = json.loads(json_string)
    intent = Intent(name=str(data['intent']['name']), confidence=data['intent']['confidence'])
    return intent

class TestData:
    def __init__(self, data):
        self.data = data

if __name__ == "__main__":
    rospy.init_node("uxd_core")
    rospy.Subscriber("/intent", String, receive_data)
    rospy.spin()

    
    
    # receive_data(TestData("""
    #                         {
    #                             "intent":{
    #                             "name":"makeDogNeutral",
    #                             "confidence": 1
    #                         }
    #                     }
    #                         """))
