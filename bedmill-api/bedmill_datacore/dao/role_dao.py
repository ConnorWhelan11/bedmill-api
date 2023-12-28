from sqlalchemy.orm import Session
from .models import Role, Permission 

class RoleDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def seed_data(self):
        if not self.db_session.query(Role).first():
            roles_data = [
                {"name": "admin", "permissions": [1, 2]},
                {"name": "user", "permissions": [1, 2]},
            ]
            self.db_session.bulk_insert_mappings(Role, roles_data)

    def create_role(self, name):
        new_role = Role(name=name)
        self.db_session.add(new_role)
        self.db_session.commit()
        return new_role

    def get_role_by_id(self, role_id):
        return self.db_session.query(Role).filter(Role.id == role_id).first()

    def list_all_roles(self):
        return self.db_session.query(Role).all()

    def add_permission_to_role(self, role_id, permission_id):
        role = self.get_role_by_id(role_id)
        permission = self.db_session.query(Permission).filter(Permission.id == permission_id).first()
        if role and permission:
            role.permissions.append(permission)
            self.db_session.commit()
            return role
        return None
