from sqlalchemy.orm import Session
from .models import User


class UserDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, username, role_id):
        new_user = User(username=username, role_id=role_id)
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user

    def get_user_by_id(self, user_id):
        return self.db_session.query(User).filter(User.id == user_id).first()

    def list_all_users(self):
        return self.db_session.query(User).all()
