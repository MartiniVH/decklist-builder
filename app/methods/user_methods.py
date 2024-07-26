def read_users_method():
    return [{"username": "Rick"}, {"username": "Morty"}]


def read_user_me_method():
    return {"username": "fake_current_user"}


def read_user_method(username: str):
    return {"username": username}
