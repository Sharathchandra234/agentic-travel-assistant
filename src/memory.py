class TravelMemory:
    def __init__(self):
        self.preferences = {}
        self.conversations = []

    def save_preference(self, key, value):
        self.preferences[key] = value

    def get_preference(self, key):
        return self.preferences.get(key)

    def save_conversation(self, conversation):
        self.conversations.append(conversation)

    def get_recent_conversations(self):
        return self.conversations[-5:]