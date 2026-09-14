# emmanuel
from models.person import Person


class User(Person):
    def __init__(self, name, email, password, role="user", user_id=None):
        super().__init__(name)

        self._email = email
        self._password = password
        self._role = role
        self._user_id = user_id

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def role(self):
        return self._role

    @property
    def user_id(self):
        return self._user_id

    def __str__(self):
        return f"{self.name} - {self.email} - {self.role}"