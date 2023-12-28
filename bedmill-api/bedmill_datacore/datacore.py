from .dao import UserDAO, CaseDAO, MessageDAO, RoleDAO, PermissionDAO
from .dao.models import (
    User,
    Case,
    Message,
    Role,
    Permission,
    Message,
    case_user_association,
    roles_permissions,
    Base
)
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table
from databases import Database
from sqlalchemy.orm import Session, sessionmaker
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DATABASE_URL = "sqlite:///./test.db"

class Datacore:
    def __init__(self, url) -> None:
        if url:
            database_url = url
        else:
            database_url = DATABASE_URL
        self.metadata = MetaData()
        self.engine = create_engine(database_url)
        self.database = Database(database_url)
        self.session = sessionmaker(bind=self.engine)()
        Base.metadata.create_all(self.engine)
        self.service = None
    
    def start(self):
        service: DatacoreService = self.get_service()
        service.init_tables()
        logger.info("Datacore started")
        return service

    def get_engine(self):
        if self.engine is None:
            self.engine = create_engine(DATABASE_URL)
        return self.engine
    
    def get_session(self):
        if self.session is None:
            self.session = sessionmaker(bind=self.get_engine())()
        return self.session
    
    def get_service(self):
        if self.service is None:
            self.service = DatacoreService(self.get_session())
        return self.service

class DatacoreService:
    """
    DatacoreService is the main service class for Bedmill datacore.
    """
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.user_dao = UserDAO(db_session)
        self.case_dao = CaseDAO(db_session)
        self.message_dao = MessageDAO(db_session)
        self.role_dao = RoleDAO(db_session)
        self.permission_dao = PermissionDAO(db_session)
    
    def init_tables(self):
        self.permission_dao.seed_data()
        self.role_dao.seed_data()
        print("Tables seeded")
        
    def create_user_with_role(self, username, role_name):
        role = self.role_dao.create_role(role_name)
        return self.user_dao.create_user(username, role.id)

    def send_message_to_case(self, message_content, case_id, sender_user_id):
        return self.message_dao.create_message(message_content, case_id, sender_user_id)

    def create_new_case(self, title, created_by_user_id):
        return self.case_dao.create_case(title, created_by_user_id)