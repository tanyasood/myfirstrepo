import spy_detail

######################Spy_Chat#########################
from spy_detail import spy_salutation ,spy_name,spy_age,spy_rating
def start_chat(spy_name,spy_salutation,spy_age,spy_rating):
    menu_choices = "what do you want to do? \n 1.Add a status update\n2.Add a friend\n3.Send a secret message\n4.Read a secret message\n5.Read chats from a user\n6.Close the application"
    menu_choice = int(input(menu_choices))

    if(menu_choice == '1'):
        print('Add Status is :')
    if(menu_choice == 2):
        print('Add Friend is:')
    if(menu_choice == 3):
        print('Send Secret Mess. is:')
    if(menu_choice == 4):
        print('Read Secret Mess. is:')
    if(menu_choice == 5):
        print('Read Chats is:')
    else:
        print('close application')


question = "continue as"  + spy_salutation + " " + spy_name + "(Y/N)?"
existing = input(question)

if existing=="Y":
    start_chat(spy_name,spy_salutation,spy_age,spy_rating)
else:
    spy_name = input("welcome to spy chat . You must tell me your spy name first:")



