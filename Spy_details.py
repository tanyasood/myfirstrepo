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

spy = Spy('Ritesh', 'Mr.', 20, 4.5)

friend_one = Spy('Deepanshu', 'Mr.', 20, 4.7)
friend_two = Spy('Tanya', 'Ms.', 20, 4.8)
friend_three = Spy('Rahul', 'Mr.', 20, 4.8)
friend_four = Spy('Ritesh', 'Mr..', 21, 4.9)
friend_five = Spy('Harshika', 'Ms.', 20, 4.9)
friend_six = Spy('Yash', 'Mr..', 20, 4.9)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five,friend_six]