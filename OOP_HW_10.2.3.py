# 2.3. Разные роли пользователя

class Admin:
    def create_user(self, name):
        self.name = name
        print(f"User created: {name}")


class Support:
    def create_ticket(self, description):
        print(f"Ticket created: {description}")

class SuperUser(Admin, Support):
    pass

su = SuperUser()
su.create_user("Ivan")
su.create_ticket("Падает сервис")


