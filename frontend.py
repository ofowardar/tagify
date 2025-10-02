import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# Session state ile login takibi
if "username" not in st.session_state:
    st.session_state.username = None
if "registered" not in st.session_state:
    st.session_state.registered = False

st.sidebar.title("Tagify Menu")
if st.session_state.username:
    st.sidebar.write(f"Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.username = None
        st.session_state.registered = False

# Sidebar menu
menu = ["Register", "Login", "Notes"]
choice = st.sidebar.radio("Go to", menu)

# Register
if choice == "Register":
    st.header("Register")
    username = st.text_input("Username", key="reg_user")
    password = st.text_input("Password", type="password", key="reg_pass")
    if st.button("Register"):
        if username and password:
            resp = requests.post(f"{API_URL}/register", json={"username": username, "password": password})
            if resp.status_code == 200:
                st.success(f"User {username} registered successfully!")
                st.session_state.registered = True
            else:
                st.error(resp.json().get("detail"))
        else:
            st.warning("Please provide username and password")

# Login
elif choice == "Login":
    st.header("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        if username and password:
            resp = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
            if resp.status_code == 200:
                st.session_state.username = username
                st.success(f"Logged in as {username}")
            else:
                st.error(resp.json().get("detail"))
        else:
            st.warning("Please provide username and password")

# Notes
elif choice == "Notes":
    if not st.session_state.username:
        st.warning("You must login to access Notes")
    else:
        st.header("Your Notes")
        note_content = st.text_area("Write a new note")
        if st.button("Add Note"):
            if note_content.strip():
                payload = {"content": note_content, "username": st.session_state.username}
                resp = requests.post(f"{API_URL}/notes", json=payload)
                if resp.status_code == 200:
                    st.success("Note added!")
                else:
                    st.error(resp.json())
        # Fetch notes
        resp = requests.get(f"{API_URL}/notes", params={"username": st.session_state.username})
        if resp.status_code == 200:
            notes = resp.json()
            st.subheader("My Notes")
            for n in notes:
                st.markdown(f"**Content:** {n['content']}")
                st.markdown(f"**Tags:** {', '.join(n.get('tags', []))}")
                st.markdown("---")
        else:
            st.error("Failed to fetch notes")
