from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bedmill_datacore.datacore import Datacore

app = FastAPI()
# Initialize Datacore
DATABASE_URL = "sqlite:///./test.db"
datacore = Datacore(DATABASE_URL)
servie = datacore.start()

class UserWithRole(BaseModel):
    username: str
    role_name: str

class Message(BaseModel):
    message_content: str
    case_id: int
    sender_user_id: int

class Case(BaseModel):
    title: str
    created_by_user_id: int
    
class Role(BaseModel):
    role_name: str

class Permission(BaseModel):
    permission_name: str


@app.post("/users/")
async def create_user_with_role(user: UserWithRole):
    return service().create_user_with_role(user.username, user.role_name)

@app.post("/messages/")
async def send_message(new_message: Message):
    return service().send_message_to_case(new_message.message_content, new_message.case_id, new_message.sender_user_id)

@app.post("/cases/")
async def create_case(new_case: Case):
    return service().create_new_case(new_case.title, new_case.created_by_user_id)


@app.post("/roles/")
async def create_role(role: Role):
    # Implement logic to create a new role using your datacore service
    return {"message": f"Role '{role.role_name}' created successfully"}

@app.post("/permissions/")
async def create_permission(permission: Permission):
    # Implement logic to create a new permission using your datacore service
    return {"message": f"Permission '{permission.permission_name}' created successfully"}