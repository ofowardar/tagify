from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from app.user_manager import UserManager
from app.note_manager import NoteManager
from app.tagger import TagExtractor

app = FastAPI(
    title="Tagify is AI supported note app",
    description="Take notes, AI supported tagging, multi-user system with JSON storage",
    version="0.1.0"
)

user_manager = UserManager()
note_manager = NoteManager()
tagger = TagExtractor()

current_users = {}  # username -> logged in

def get_current_user(username: str):
    if username not in current_users:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return username

# Models
class RegisterModel(BaseModel):
    username: str
    password: str

class LoginModel(BaseModel):
    username: str
    password: str

class NoteCreateModel(BaseModel):
    username: str
    content: str

@app.get("/")
def root():
    return {"message": "Welcome to Tagify App!"}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "AI Supported Tagify is working..."}

@app.post("/register")
def register(data: RegisterModel):
    try:
        user_manager.register(data.username, data.password)
        return {"message": f"User '{data.username}' registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
def login(data: LoginModel):
    if user_manager.login(data.username, data.password):
        current_users[data.username] = True
        return {"message": f"User '{data.username}' logged in"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/notes")
def add_note(data: NoteCreateModel):
    user = get_current_user(data.username)
    note = note_manager.create_note(content=data.content, owner=user, tagger=tagger)
    return note.to_dict()

@app.get("/notes")
def get_notes(username: str):
    user = get_current_user(username)
    notes = note_manager.get_notes_for_user(user)
    return [n.to_dict() for n in notes]
