from cgitb import lookup
import json
import uuid
import csv
import numpy as np

import rospy
from std_msgs.msg import String
from typing import List



def deserialize(data):
    d = data.__dict__
    for key, value in d.iteritems():
        if isinstance(value, List):
            new_value = []
            for item in value:
                new_value.append(deserialize(item))
            d[key] = new_value
        elif isinstance(value, uuid.UUID):
            d[key] = str(value)
    return d

class ActionRequest:
    def __init__(self, clear_action_queue, actions, id=None):
        self.id = id if id is not None else uuid.uuid4()
        self.clear_action_queue = clear_action_queue
        self.actions = actions

    def to_json(self):
        return json.dumps(deserialize(self))

class SitAction:
    def __init__(self, start_time):
        self.type = "sit"
        self.start_time = start_time

class GroupAction:
    def __init__(self, actions, start_time=0):
        self.type = "group"
        self.start_time = start_time
        self.actions = actions

class DisplayAction:
    def __init__(self, name, start_time):
        self.type = "display"
        self.name = name
        self.start_time = start_time


class SoundAction:
    def __init__(self, name, start_time):
        self.type = "sound"
        self.name = name
        self.start_time = start_time


class State:
    current_emotion = None
    current_action = None


def update_current_emotion(intent):
    currentEmotion = State.current_emotion




def process_intent(intent):


    # OpenCSV and turn it into dictionary
    input_file = csv.DictReader(open("lookup.csv"))

    #GetCurrentEmotion
    emotion = State.current_emotion


    # Look up corresponding field in table
    for key, value in input_file.items():
        Name, Confidence, Sentiment, CorrespondingAction  = value
    if (Name == "HappyGivePaw") & (Confidence == "1") & (Sentiment == "Happy") & (emotion == "Sad"):
        # This line would correspond to the JSON or directly turning the String into a JSON
        action = CorrespondingAction
        action_request = look_up_action(action, intent, emotion)

    return action_request

class UUIDv4(uuid.uuid4):
    def __dict__(self):
        return str(self)

def look_up_action(action, intent, emotion):
    input_file = csv.DictReader(open("actionlookup.csv"))
    for key, value in input_file.items():
        Name, subcommand1 ,subcommand2 ,subcommand3 = value
    if (Name == action):
        print (ActionRequest (id=id, clear_action_queue=True, actions=[subcommand1, subcommand2, subcommand3])) 
        # We need to have a fix for the classes to correspond to the table
       

    id = uuid.uuid4()
    State.current_action = id
    return ActionRequest(id=id, clear_action_queue=False, actions=[SitAction(start_time=1000), GroupAction(actions=[SitAction(start_time=3000)])])