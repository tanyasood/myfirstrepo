from Spy_details import *
from steganography.steganography import Steganography
from datetime import datetime
import csv



print ("Hello!")
# This will print Hello!

print('let\'s get started')
# Project will get started

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
# This will ask user to continue as Spy Name with salutation

existing = raw_input(question)

STATUS_MESSAGES=["Tanya", "Sood"]


friends = []

friends_name = []
friends_age = []
friends_rating = []
friends_online = []

def add_friends():
    new_friend = {
        'name' :"",
        'salutation': "",
        'age': 0,
        'rating' : 0.0
     }
    new_friend['name'] = raw_input("please add your friend's name:")
    new_friend['salutation'] = raw_input("are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = raw_input("age?")
    new_friend['rating'] = raw_input("spy_rating")

    if len(new_friend['name']) > 0 and int(new_friend['age']) < 50 and int(new_friend['age']) > 12 and float(new_friend['rating']) >= float(spy.rating):
        friends.append(new_friend)
        print "Congratulations! Your friends is been successfully added\n"
    else:
        print"Sorry we cannot add this friend he does'nt meet our criteria\n"
    return len(friends)


def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        read = csv.reader(friends_data)
        for row in read:
            spy = Spy(name=row[0], salutation=row[1], rating=row[2], age=row[3], is_online=row[4])
            add_friends.append(spy)

#function for loading chats
def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        read = csv.reader(chats_data)
        for row in read:
            chat = ChatMessage(name=row[0], message=row[1], isItYou=row[3])
            add_friends().append(chat)

def add_friend_old():
    new_name = input("please add your friend's name:")
    new_salutation = input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = input("Age?")
    new_rating = input("Spy_rating")
    if len(new_name) > 0 and new_age > 50 and new_rating >= spy.rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_online.append(True)

    else:
        print("Sorry! Invalid entry.We can\'t add spy with the details you provided")
        return len(friends_name)

# Function to add status
def add_status():
    updated_status_message = None
    if spy.current_status_message != None:
        print ("Your current status message is " + spy.current_status_message + "\n")
    else:
        print ("You don\'t have any status message currently \n")
    default = input("Do you want to select from the older status (y/n)? ")
    # upper is used to convert the input into upper case
    if default.upper() == "N":
        new_status_message = input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(new_status_message)
    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print ('%d. %s' % (item_position, message))
            item_position = item_position + 1
        message_selection = int(input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    return updated_status_message

def select_a_friend():
    item_no = 0
    if len(friends)!=0:
        for friend in friends:
            print("%d . %s" % (item_no+1, friend["name"]))
            item_no = item_no + 1
        friend_no = int(input("Select your Friend : "))
        if friend_no<=len(friends) and friend_no!=0:
            print("You selected %d no Friend" % friend_no)
            return friend_no-1
        else:
            print("Wrong input, please try again...")
    else:
        print("Sorry no Friend added till now, plz add a friend first...")
        friend_no=add_friends()
        print("No. of Friends: %d" % friend_no)
        select_a_friend()
# function to send secret message

def send_message():
    selection = select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_image = 'output_new.PNG'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_image, text)
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True,

    }

    friends[selection]['chats']=(new_chat)
    print "Your secret message is ready! to be delivered"


#####a function to read  secret message#########

def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file to be decoded?")
    secret_text = Steganography.decode(output_path)
    print("your secret message is:"+secret_text)
    new_chat = {
    "message": secret_text,
    "time": datetime.now(),
    "sent_by_me": False
    }
    friends[sender]['chats']=(new_chat)
    print(secret_text)
    print "Your secret message has been saved! spy"



# Function to start chat
def start_chat(spy):
    print ("Authentication complete. Welcome " + spy.name + " age: " \
          + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard")
    current_status_message=None
    show_menu = True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n" \
                       " 3. Send a secret message \n 4. Read a secret message \n" \
                       " 5. Read Chats from a user \n 6.show friends \n 7. Close Application \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                spy.current_status_message = add_status()
            elif menu_choice == 2:
                number_of_friends = add_friends()
                print("You have %d friends" % (number_of_friends))
            elif menu_choice == 3:
                print("Send message")
            elif menu_choice == 4:
                print"read_message"
            elif menu_choice == 5:
                read_chats()
            elif menu_choice == 6:
                select_a_friend()
            else:
                show_menu = False


def read_chats():
    with open('chats.csv', 'rb') as chats_data:
        read = csv.reader(chats_data)
        for row in read:
            print row


if existing == "Y":
    start_chat(spy)
else:
    spy = Spy('','',0,0.0)

    spy.name = raw_input("What is your name?")

    if len(spy.name) > 0:
        print ("Welcome " + spy.name + ". Glad to have you back with us.")
        spy.salutation = raw_input("What should we call you (Mr. or Ms.)?")
        spy.name = spy.salutation + " " + spy.name
        print ("Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed...")
        spy.age = 0
        spy.rating = 0.0
        spy.is_online = False
        spy.age = raw_input("What is your age?")
        if 18 < int(spy.age) < 65:
            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)
            if spy.rating > 4.5:
                print ("Great ace!")
            elif 3.5 < spy.rating <= 4.5:
                print ("You are one of the good ones.")
            elif 2.5 <= spy.rating <= 3.5:
                print ("You can always do better")
            else:
                print ("We can always use somebody to help in the office.")
            spy.is_online = True
            start_chat(spy)

        else:
            print ("Sorry you are not of the correct age to be a spy")
    else:

        print ("A spy needs to have a valid name. Try again please.")
