print("SPYCHAT")
print("Welcome to SPYCHAT")
spy_name=input('What/s your name')
print(spy_name)
print("Welcome " + spy_name + " How are you?")
type(spy_name)
spy_salutation=input("What should we call you(Mr./Miss.)")
print(spy_salutation)
print(spy_salutation +" " + spy_name)
print("Alright "+ spy_salutation +" " + spy_name + " I would like to know a little bit more about you")
spy_account=input("Tell which account would you prefer to choose(default/new)")
if(spy_account=="new"):
    spy_name = str(input("Whats your name"))
    print(spy_name)
    print("Welcome " + spy_name + " How are you?")
    type(spy_name)
    spy_salutation = str(input("What should we call you(Mr./Miss.)"))
    print(spy_salutation)
    print(spy_salutation + " " + spy_name)
    print("Alright " + spy_salutation + " " + spy_name + " I would like to know a little bit more about you")
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = True
spy_age = int(input("What is your age?"))
if spy_age > 17 and spy_age < 60:
    spy_rating = float(input("What is your spy rating?"))
    if spy_rating > 4.5:
        print("Great ace!")
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print("You are one of the good ones.")
    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print("You can always do better.")
    else:
        print("We can always use somebody to help in the office.")

else:
    exit(0)

print('welcome in python class' + spy_salutation + " " + spy_name + " \n age :"+ str(spy_age) + " \n rating:"  + str(spy_rating) + "\n proud to have you onboard")




