from sqlalchemy.orm import Session
from .models import Permission 

class PermissionDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    def seed_data(self):
        if not self.db_session.query(Permission).first():
            # Seed permissions
            permissions_data = [
                {"name": "read_message"},
                {"name": "write_message"},
            ]
            self.db_session.bulk_insert_mappings(Permission, permissions_data)

    def create_permission(self, name):
        new_permission = Permission(name=name)
        self.db_session.add(new_permission)
        self.db_session.commit()
        return new_permission

    def get_permission_by_id(self, permission_id):
        return self.db_session.query(Permission).filter(Permission.id == permission_id).first()

    def list_all_permissions(self):
        return self.db_session.query(Permission).all()
