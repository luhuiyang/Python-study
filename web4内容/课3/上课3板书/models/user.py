from models import Model


class User(Model):
    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.id = None

    def validate_login(self):
        users = self.all()
        for user in users:
            if self.username == user.form.get('username') and self.password == user.form.get('password'):
                return True
        return False

    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2

