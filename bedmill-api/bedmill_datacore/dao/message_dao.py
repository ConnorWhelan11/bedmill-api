from sqlalchemy.orm import Session
from .models import Message

class MessageDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_message(self, content, case_id, sender_user_id):
        new_message = Message(content=content, case_id=case_id, sender_user_id=sender_user_id)
        self.db_session.add(new_message)
        self.db_session.commit()
        return new_message

    def get_messages_by_case_id(self, case_id):
        return self.db_session.query(Message).filter(Message.case_id == case_id).all()

    def list_all_messages(self):
        return self.db_session.query(Message).all()
