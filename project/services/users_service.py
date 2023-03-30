from project.dao.user import UsersDAO
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO):
        self.dao = dao

    def get_one(self, uid):
        """
        Сервис получения одного пользователя
        """
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        """
        Сервис получения пользовтеля по email
        """
        return self.dao.get_by_email(email)

    def get_all(self):
        """
        Сервис получения всех пользовтелей
        """
        users = self.dao.get_all()
        return users

    def create(self, user_data: dict[str, str]):
        """
        Сервис создания пользователя
        """
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_data):
        """
        Сервис получения пользователя по email
        """
        self.dao.update(user_data)
        return self.dao

    def update_password(self, email, new_password):
        """
        Сервис обновления пароля пользователя
        """
        self.dao.update_password(email, new_password)

    def delete(self, uid):
        """
        Сервис удаления пользователя
        """
        self.dao.delete(uid)
