# Tagify - AI Supported Note App

<p align="center">
  <img src="logo.png" alt="Tagify Logo" width="180"/>
</p>

Tagify is a modern web application that makes note-taking easy and smart with AI-powered tagging. It features a FastAPI backend with multi-user JSON-based storage and a sleek Streamlit frontend.

---

## 🚀 Features

- **User Registration & Login** (JSON-based)
- **Add, View & Manage Notes**
- **AI-Powered Automatic Tag Extraction**
- **Modern Streamlit UI** with hamburger menu & logout on every page
- **Simple JSON Data Storage**
- **Secure Password Hashing** (bcrypt)

---

## 🛠️ Technologies

| Layer      | Tech         |
|------------|-------------|
| Backend    | FastAPI     |
| Frontend   | Streamlit   |
| Encryption | Passlib (bcrypt) |
| Language   | Python 3.11+|
| Storage    | JSON files  |

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/tagify.git
   cd tagify
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .myenv
   .\.myenv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend API:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Run the frontend:**
   ```bash
   streamlit run app.py
   ```

---

## 📚 API Endpoints

All endpoints are prefixed with `/api` unless otherwise noted.

### **Authentication**

#### `POST /api/register`
Register a new user.
- **Request Body:**
  ```json
  {
    "username": "yourname",
    "password": "yourpassword"
  }
  ```
- **Response:**
  ```json
  {
    "username": "yourname"
  }
  ```

#### `POST /api/login`
Login with username and password.
- **Request Body:**
  ```json
  {
    "username": "yourname",
    "password": "yourpassword"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "jwt_token"
  }
  ```

---

### **Notes**

#### `GET /api/notes`
Get all notes for the authenticated user.
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Note Title",
      "content": "Note content...",
      "tags": ["tag1", "tag2"]
    }
  ]
  ```

#### `POST /api/notes`
Create a new note.
- **Headers:** `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "title": "Note Title",
    "content": "Note content..."
  }
  ```
- **Response:**
  ```json
  {
    "id": 2,
    "title": "Note Title",
    "content": "Note content...",
    "tags": ["tag1", "tag2"]
  }
  ```

#### `GET /api/notes/{id}`
Get a specific note by ID.
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  {
    "id": 2,
    "title": "Note Title",
    "content": "Note content...",
    "tags": ["tag1", "tag2"]
  }
  ```

#### `PUT /api/notes/{id}`
Update a note.
- **Headers:** `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "title": "Updated Title",
    "content": "Updated content..."
  }
  ```
- **Response:**
  ```json
  {
    "id": 2,
    "title": "Updated Title",
    "content": "Updated content...",
    "tags": ["tag1", "tag2"]
  }
  ```

#### `DELETE /api/notes/{id}`
Delete a note.
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  {
    "detail": "Note deleted"
  }
  ```

---

### **Tag Extraction**

#### `POST /api/tags/extract`
Extract tags from note content using AI.
- **Request Body:**
  ```json
  {
    "content": "Your note content here..."
  }
  ```
- **Response:**
  ```json
  {
    "tags": ["tag1", "tag2", "tag3"]
  }
  ```

---

## 🎨 Screenshots

<p align="center">
  <img src="screenshots/home.png" alt="Home" width="600"/>
  <img src="screenshots/note_detail.png" alt="Note Detail" width="600"/>
  <img src="screenshots/tagify_ai.png" alt="AI Tagging" width="600"/>
</p>

---

## ⚡ Quick Start

```bash
git clone https://github.com/yourusername/tagify.git
cd tagify
python -m venv .myenv
.\.myenv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
streamlit run app.py
```

---

## 📝 License

MIT License © 2025 [ofowardar](https://github.com/ofowardar)

---

## 💡 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

For questions or feedback, open an issue or email [ofowardar@gmail.com](mailto:ofowardar@gmail.com).
