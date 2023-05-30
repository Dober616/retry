class User():
    user_name = 'Admin'
    password = 'qwerty'
    is_banned = False
    friends = list()

    def print_info(self):
        print(f'Name: {self.user_name}\n'
              f'Password: {self.password}\n'
              f'Ban status: {self.is_banned}\n'
              f'Список друзей: {self.friends}')

    def add_friend(self, name):
        if isinstance(name, User):
            self.friends.append(name.user_name)
        else:
            self.friends.append(name)


user_1 = User()
user_2 = User()
user_2.user_name = 'Alina'
user_1.user_name = 'Kirill'
user_1.add_friend('Егор')
user_1.add_friend(user_2)


user_1.print_info()
