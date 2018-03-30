from spy_detail import spy, Spy, friends
from datetime import datetime

print ("Hello!")
# This will print Hello!

print('let\'s get started')
# Project will get started

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
# This will ask user to continue as Spy Name with salutation

existing = input(question)

STATUS_MESSAGES=["Tanya", "Sood"]

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
        new_status_message =input("What status message do you want to set?")

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


# Function for adding friends
def add_friend():
    new_friend = Spy('', '', 0, 0.0)
    new_friend.name=input("Please add your friend's name")
    new_friend.salutation = input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(input("Age?"))


    new_friend.rating = float(input("Spy rating?"))
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print ("Friend Added!",'red')
    else:
        print ("Sorry! Invalid entry. We can\'t add spy with the details you provided")

    return len(friends)


# Function to start chat
def start_chat(spy):
    print ("Authentication complete. Welcome " + spy.name + " age: " \
          + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard")
    current_status_message=None
    show_menu = True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n" \
                       " 3. Send a secret message \n 4. Read a secret message \n" \
                       " 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                spy.current_status_message = add_status()
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print ("You have %d friends" % (number_of_friends))
            elif menu_choice == 3:
                send_a_message()
            elif menu_choice == 4:
                read_a_message()
            elif menu_choice == 5:
                read_chat_history()
            else:
                show_menu = False
if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)

    spy.name = input("What is your name?")

    if len(spy.name) > 0:
        print ("Welcome " + spy.name + ". Glad to have you back with us.")
        spy.salutation = input("What should we call you (Mr. or Ms.)?")
        spy.name = spy.salutation + " " + spy.name
        print ("Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed...")
        spy.age = 0
        spy.rating = 0.0
        spy.is_online = False
        spy.age = int(input("What is your age?"))
        if 18 < spy.age < 65:
            spy.rating = float(input("What is your spy rating?"))
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
