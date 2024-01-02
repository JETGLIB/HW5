class EventLogger:
    def __init__(self):
        self.log = []

    def log_event(self, event):
        self.log.append(event)

    def print_log(self):
        for event in self.log:
            print(event)