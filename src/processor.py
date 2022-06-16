import json
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


lookup = {
    "makeDogNeutral": {
        "actions": {
            "sad": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="neutral")), HeadAction(start_ms=200, end_ms=1200, roll=0, pitch=10, yaw=0), ActionGroup(start_ms=2500, actions=[HeadAction(start_ms=0, end_ms=2000, roll=0, pitch=0, yaw=0), PoseAction(start_ms=0, end_ms=2000, roll=0, pitch=10, yaw=0, body_height=200)]), ActionGroup(start_ms=4500, actions=[HeadAction(start_ms=0, end_ms=2000, roll=0, pitch=10, yaw=0), PoseAction(start_ms=0, end_ms=2000, roll=0, pitch=0, yaw=0, body_height=250)])]
            },
        },
        "resulting_emotion": "neutral"
    },
    "makeDogSad": {
        "actions": {
            "default": {
                "action": [DisplayAction(start_ms=0, data=DisplaySoundData(name="sad"))]
            }
        },
        "resulting_emotion": "sad"
    }
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
        deserializable_dict = data.__dict__
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