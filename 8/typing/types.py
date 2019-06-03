from typing import TypeVar

class User:
    x: int
class BasicUser(User):
    y: int
class ProUser(User): ...
class TeamUser(User): ...

# Accepts User, BasicUser, ProUser, TeamUser, ...
def make_new_user(user_class: Type[User]) -> User:
    # ...
    return user_class()

T = TypeVar('T')

def make_new_user2(user_class: Type[T]) -> T:
    # ...
    return user_class()

u = make_new_user(BasicUser)
u.x