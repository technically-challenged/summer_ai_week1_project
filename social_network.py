#Various import Statements can go here
from  social_network_classes import SocialNetwork, Person
import social_network_ui


#Create instance of main social network object
ai_social_network = SocialNetwork()
#ai_person = Person("john", 20) --> you need to create specific instances bc there are many people, ie the class needs to be used many times


if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
            #this is for CREATING a NEW account 
            #works

        #inner menu 
        elif choice == "2":
            loggin_screen = social_network_ui.logginMyAccount()
                # to loggin to account
                #works

            current_user_index = ai_social_network.list_of_names.index(loggin_screen) 
            current_user = ai_social_network.list_of_people[current_user_index]
            inner_menu_choice = social_network_ui.manageAccountMenu()
            while True:

                #works

                if inner_menu_choice == "1":
                    pass 
                    #this is for editing details 
                    new_name = input("enter new name: ")
                    new_age = input("enter new age: ")
                    current_user.id = new_name
                    current_user.age = new_age
                    #works


                elif inner_menu_choice == "2":
                    #this is for adding friends
                    
                    new_friend = input("enter name of new friend: ")
                    current_user.friendlist.append(new_friend)
                    print(current_user.friendlist)
                    #works
                    

                elif inner_menu_choice == "3":
                    #this is for viewing friends
                    print(current_user.friendlist)
                    #works

                elif inner_menu_choice == "4":
                    #this is for viewing your messages 
                    print(current_user.messagelist)
                    #works


                elif inner_menu_choice == "5":
                    #this is for messaging a friend 
                    current_user.send_message(ai_social_network)
                    #works


                elif inner_menu_choice == "6":
                        break
                inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()

