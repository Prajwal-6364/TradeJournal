from db import get_db
import os
from dotenv import load_dotenv

env_path = r"c:\Users\prajw\Downloads\trading-journal-flask-mongo\tjp-flask-mongo\backend\.env"
load_dotenv(env_path)

db = get_db()
users = list(db.users.find({}, {"email": 1, "username": 1}))

print(f"Total registered users: {len(users)}")
for u in users:
    print(f"- {u.get('email')} (username: {u.get('username')})")
