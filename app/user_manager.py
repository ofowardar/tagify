# app/user_manager.py
import json
from pathlib import Path
from passlib.context import CryptContext
from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
MAX_PASSWORD_LENGTH = 72

class UserManager:
    def __init__(self, filepath: str = "users.json"):
        self.filepath = Path(filepath)
        if not self.filepath.exists() or self.filepath.read_text().strip() == "":
            self.filepath.write_text("[]", encoding="utf-8")
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                data = json.loads(content) if content else []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        users = []
        for u in data:
            username = u.get("username")
            password_hash = u.get("password_hash")
            if not password_hash and "password" in u:
                password_hash = pwd_context.hash(u["password"][:MAX_PASSWORD_LENGTH])
            users.append(User(username, password_hash))
        return users

    def save_users(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)

    def register(self, username, password):
        password_hash = pwd_context.hash(password[:MAX_PASSWORD_LENGTH])
        user = User(username, password_hash)
        self.users.append(user)
        self.save_users()
        return user

    def login(self, username, password):
        user = next((u for u in self.users if u.username == username), None)
        if not user:
            return False
        return pwd_context.verify(password[:MAX_PASSWORD_LENGTH], user.password_hash)
