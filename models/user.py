# emmanuel
from models.person import Person

class User(Person):
    def __init__(self, name, email, password, role="user"):
        super().__init__(name)

        self._email = email
        self._password = password
        self._role = role

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def role(self):
        return self._role

    def __str__(self):
        return f"{self.name} - {self.email} - {self.role}"
