# 2.	Множественное наследование, делегирование; Миксин для проверки прав

class PermissionMixin:
    def has_permission(self, user_role):
        return user_role == "admin"

class SecureAction(PermissionMixin):
    def execute(self, user_role):
        if self.has_permission(user_role):
            print("Админ. Метод запущен")
        else:
            print("Нет прав.")

action = SecureAction()
action.execute("user") # Нет прав.
action.execute("admin") # Админ. Метод запущен
