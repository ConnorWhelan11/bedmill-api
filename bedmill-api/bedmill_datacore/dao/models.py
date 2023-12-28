from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association Table for Many-to-Many relationship between Roles and Permissions
roles_permissions = Table('roles_permissions', Base.metadata,
    Column('role_id', ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', ForeignKey('permissions.id'), primary_key=True)
)

case_user_association = Table('case_user_association', Base.metadata,
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role")

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    permissions = relationship("Permission", secondary=roles_permissions)

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_by_user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User")
    accessible_users = relationship("User", secondary=case_user_association)

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    case_id = Column(Integer, ForeignKey('cases.id'))
    sender_user_id = Column(Integer, ForeignKey('users.id'))
    case = relationship("Case")
    sender = relationship("User")

