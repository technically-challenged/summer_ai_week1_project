# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        self.list_of_names = []
        
    ## For more challenge try this
    #def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        #pass

    ## For more challenge try this
    #def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        #pass

    def  create_account(self):
        print("Creating ...")
        name = input("enter name: ")
        age = input("enter age: ")
        #implement function that creates account here
        
        person_info = Person(name, age)
        self.list_of_people.append(person_info)
        self.list_of_names.append(name)
     
        
        
     


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messagelist = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        new_friend = input("enter name of new friend: ")
        self.friendlist.append(new_friend)
        pass

    def send_message(self, network):
        #implement sending message to friend here
        to_who = input("enter username of friend you want to message: ")
        message = input("enter message here, and sign your name at the end: ")
        for person in network.list_of_people:
            if to_who == person.id:
                person.messagelist.append(message)
        #pass

    #i commented the below function out because i found another way to do it, but this is benedicts code so its staying for now 
    # def edit_details(self):
        #pass
        #new_age = input("enter new age: ")
        #new_name = input("enter new name: ")
        #self.year = new_age
