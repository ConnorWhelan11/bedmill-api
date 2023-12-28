from sqlalchemy.orm import Session
from .models import Case, User

class CaseDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_case(self, title, created_by_user_id):
        new_case = Case(title=title, created_by_user_id=created_by_user_id)
        self.db_session.add(new_case)
        self.db_session.commit()
        return new_case

    def get_case_by_id(self, case_id):
        return self.db_session.query(Case).filter(Case.id == case_id).first()

    def list_all_cases(self):
        return self.db_session.query(Case).all()
    
    def add_user_access_to_case(self, case_id, user_id):
        case = self.get_case_by_id(case_id)
        user = self.db_session.query(User).filter(User.id == user_id).first()
        if case and user:
            case.accessible_users.append(user)
            self.db_session.commit()
            return case
        return None

    def get_accessible_cases_for_user(self, user_id):
        return self.db_session.query(Case).filter(Case.accessible_users.any(id=user_id)).all()
