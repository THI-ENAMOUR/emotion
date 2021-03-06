import json
import random
import uuid

class State:
    current_emotion = None
    current_action = None

class ActionRequest(object):
    def __init__(self, id, clear_action_queue, actions):
        id = id if id is not None else uuid.uuid4()
        self.id = id
        self.clear_action_queue = clear_action_queue
        self.actions = actions

class Action(object):
    def __init__(self, type, start_ms, id=None, end_ms=None):
        id = id if id is not None else uuid.uuid4()
        self.id = id
        self.type = type
        self.start_ms = start_ms
        self.end_ms = end_ms


class DisplaySoundData:
    def __init__(self, name):
        self.name = name


class SoundAction(Action):
    type = "sound"

    def __init__(self, start_ms, data):
        self.data = data
        super(SoundAction, self).__init__(type=SoundAction.type, start_ms=start_ms)


class DisplayAction(Action):
    type = "display"

    def __init__(self, start_ms, data):
        self.data = data
        super(DisplayAction, self).__init__(type=DisplayAction.type, start_ms=start_ms)


class ActionGroup(Action):
    type = "group"

    def __init__(self, start_ms, actions):
        self.actions = actions
        super(ActionGroup, self).__init__(type=ActionGroup.type, start_ms=start_ms)


class NavigationAction(Action):
    type = "navigation"

    def __init__(self, start_ms, x=None, y=None, yaw=None,  body_height=None):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.body_height = body_height
        super(NavigationAction, self).__init__(type=NavigationAction.type, start_ms=start_ms)

class HeadAction(Action):
    type = "head"

    def __init__(self, start_ms, end_ms=None, roll=None, pitch=None, yaw=None):
        self.end_ms = end_ms
        self.roll =roll
        self.pitch = pitch
        self.yaw = yaw
        super(HeadAction, self).__init__(type=HeadAction.type, start_ms=start_ms)

class PoseAction(Action):
    type = "pose"

    def __init__(self, start_ms, end_ms, roll=None, pitch=None, yaw=None, body_height=None):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.body_height = body_height
        super(PoseAction, self).__init__(type=PoseAction.type, start_ms=start_ms, end_ms=end_ms)


class SitAction(Action):
    type = "sit"

    def __init__(self, start_ms):
        super(SitAction, self).__init__(type=SitAction.type, start_ms=start_ms)

sadSoundList = ["Sad_01","Sad_02","Sad_03"]
joySoundList = ["Joy_01","Joy_02","Joy_03"]
sleepySoundList = ["Sleepy_01","Sleepy_02","Sleepy_03"]
affectionSoundList = ["Affection_01","Affection_02","Affection_03"]
angrySoundList = ["Anger_01","Anger_02","Anger_03"]
fearSoundList = ["Fear_01","Fear_02","Fear_03"]

lookup = {
    "endOfConversation": {
        "actions": {
            "sad": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
            "joy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
            "affection": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
            "angry": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
            "fear": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
            "curious": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
            "sleepy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
            "default": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral"))]
            },
        },
        "resulting_emotion": "neutral"
    },

    "makeDogSad": {
        "actions": {
            "neutral": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
            "joy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
            "affection": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
            "angry": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
            "fear": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
            "curious": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
            "sleepy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
            "default": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sadSoundList)))]
            },
        },
        "resulting_emotion": "sad"
    },

    "makeDogJoy": {
        "actions": {
            "neutral": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
            "sad": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
            "affection": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
            "angry": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
            "fear": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
            "curious": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
            "sleepy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
            "default": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="joy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(joySoundList)))]
            },
        },
        "resulting_emotion": "joy"
    },

    
    "makeDogSleepy": {
        "actions": {
            "neutral": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
            "sad": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
            "affection": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
            "angry": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
            "fear": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
            "curious": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
            "joy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
            "default": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sleepy")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(sleepySoundList)))]
            },
        },
        "resulting_emotion": "sleepy"
    },
    
    "makeDogAffection": {
        "actions": {
            "neutral": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
            "sad": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
            "sleepy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
            "angry": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
            "fear": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
            "curious": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
            "joy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
            "default": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="affection")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(affectionSoundList)))]
            },
        },
        "resulting_emotion": "affection"
    },

    "makeDogAngry": {
        "actions": {
            "neutral": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
            "sad": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
            "affection": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
            "sleepy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
            "fear": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
            "curious": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
            "joy": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
            "default": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="angry")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(angrySoundList)))]
            },
        },
        "resulting_emotion": "angry"
    },

    "makeDogFear": {
    "actions": {
        "neutral": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
        "sad": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
        "affection": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
        "sleepy": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
        "angry": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
        "curious": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
        "joy": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
        "default": {
            "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="fear")), SoundAction(start_ms=0, data=DisplaySoundData(name= random.choice(fearSoundList)))]
        },
    },
    "resulting_emotion": "fear"
    },
    

}

def process_intent(intent):
    # Look up current action
    emotion =  State.current_emotion if  State.current_emotion is not None else "default"
    return look_up_action(intent, emotion)

def look_up_action(intent, emotion):
    
    action_dict = lookup[intent.name]["actions"]
    try:
        resulting_action = action_dict[emotion]["action"]
    except KeyError:
        resulting_action = action_dict["default"]["action"]

    resulting_emotion = lookup[intent.name]["resulting_emotion"]
    State.current_emotion = resulting_emotion if resulting_emotion is not None else State.current_emotion

    if len(resulting_action) > 0:
        id = uuid.uuid4()
        State.current_action = id
        return ActionRequest(id=id, clear_action_queue=False, actions=resulting_action)
    else:
        return None



def to_json(data, **kwds):
    return json.dumps(data, default=to_serializable_dict, **kwds)


def to_serializable_dict(data):
    if is_primitive(data) or data is None:
        return data
    elif isinstance(data, uuid.UUID):
        return str(data)
    if hasattr(data, "__dict__"):
        deserializable_dict = dict(data.__dict__)
        for key, value in deserializable_dict.iteritems():
            if isinstance(value, list):
                new_value = []
                for item in value:
                    new_value.append(to_serializable_dict(item))
                deserializable_dict[key] = new_value
            elif isinstance(value, uuid.UUID):
                deserializable_dict[key] = str(value)
        return deserializable_dict
    else:
        return str(data)

def is_primitive(data):
    return isinstance(data, (int, float, bool, str))