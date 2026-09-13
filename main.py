# Barack
from models.user import User


user = User(
    "Emmanuel",
    "emmanuel@gmail.com",
    "password123"
)

admin = User(
    "Barack",
    "barack@gmail.com",
    "adminpassword",
    "admin"
)

print(user)
print(admin)