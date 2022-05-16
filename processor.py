import json
import uuid

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

def process_intent(intent):
    # Look up current action
    emotion = State.current_emotion

    # Look up corresponding field in table
    action_request = look_up_action(intent, emotion)

    return action_request

class UUIDv4(uuid.uuid4):
    def __dict__(self):
        return str(self)

def look_up_action(intent, emotion):
    id = uuid.uuid4()
    State.current_action = id
    return ActionRequest(id=id, clear_action_queue=False, actions=[SitAction(start_time=1000), GroupAction(actions=[SitAction(start_time=3000)])])