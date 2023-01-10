subscribers = {}


def subscribe(event_type: str, fn):
    subscribers.setdefault(event_type, []).append(fn)

def post_event(event_type: str, data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)
