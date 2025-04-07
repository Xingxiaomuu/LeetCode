import time
from collections import deque
from datetime import datetime, timedelta
import random

def generate_event():
    return {
        "event_type": random.choice(["click", "view", "purchase"]),
        "timestamp": datetime.now(),
        "user_id": random.randint(1, 100),
        "item_id": random.randint(1, 10),
    }

class SlidingWindowAggregator:
    def __init__(self, window_size_seconds):
        self.window_size = timedelta(seconds=window_size_seconds)
        self.events = deque()
    
    def add_event(self,event):
        self.events.append(event)
        self.remove_old_event()

    def remove_old_event(self):
        now = datetime.now()
        while self.events and (now-self.events[0]['timestamp']>self.window_size):
            self.events.popleft()
        
    def get_event_metrics(self):
        total_events = len(self.events)
        event_types = {}
        user_ids = {}
        for event in self.events:
            event_types[event['event_type']] = event_types.get(event['event_type'], 0) + 1
            #  print(f"{event_types.get(event['event_type'], 0)}")
            user_ids[event['user_id']] = user_ids.get(event['user_id'], 0) + 1
            unique_users = len(set(event['user_id'] for event in self.events))
        return total_events, event_types, unique_users, user_ids

if __name__ == "__main__":
    total_events = 60  # Number of events to generate
    window_size_seconds = 60  # Set the window size to 60 seconds
    aggregator = SlidingWindowAggregator(window_size_seconds)
    for _ in range(total_events):
        event = generate_event()
        aggregator.add_event(event)
        total_events, event_types, unique_users, user_ids = aggregator.get_event_metrics()
        print(f"Total events in the last {window_size_seconds} seconds: {total_events}")
        print(f"Event types: {event_types}")
        print(f"Unique users: {unique_users}")
        print(f"User IDs: {user_ids}")