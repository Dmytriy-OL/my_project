class USER():
    def __init__(self, user_id=None, login=None, name=None, password=None, last_name=None, email=None):
        self.__user_id = user_id
        self.__login = login
        self.__name = name
        self.__password = password
        self.__last_name = last_name
        self.__email = email

    def unidentified_user(self):
        return False if self.__name == 'None' else True