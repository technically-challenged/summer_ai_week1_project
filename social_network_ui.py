# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Loggin to my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def logginMyAccount():
    print("")
    return input("type in username: ")



def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Message a friend")
    print("6. <- Go back ")
    return input("Please Choose a number: ")
