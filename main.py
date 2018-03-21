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
    spy_name = input("Whats your name")
    print(spy_name)
    print("Welcome " + spy_name + " How are you?")
    type(spy_name)
    spy_salutation = input("What should we call you(Mr./Miss.)")
    print(spy_salutation)
    print(spy_salutation + " " + spy_name)
    print("Alright " + spy_salutation + " " + spy_name + " I would like to know a little bit more about you")
else:
    exit(0)



