# names of classes in python should have every first letter of the word capitalized, this is called PascalCase
class User:
    # init function is called every time we create a new object from the class
    def __init__(self, user_id, username):
        # attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # methods need to have the self parameter as the first parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Dennis otwoma")
user_2 = User("002", "Maasai Doctor")
print(user_1.followers)
print(user_1.username)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)