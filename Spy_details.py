from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#for an existing user
spy = Spy('Tanya', 'Ms.', 21, 4.6)

# chat class
class ChatMessage:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.time = datetime.now()






