Task Manager App - README

This is a simple full-stack Task Manager web application built using FastAPI for the backend and
React for the frontend. It allows users to register, login, and manage their personal tasks.

What this project does:
- Users can create an account and log in securely
- Each user gets a token (JWT) after login
- Users can create, view, update, and delete their tasks
- Tasks are stored in a database and linked to each user
- Only logged-in users can access their own tasks
  
Tech Stack:
Backend: FastAPI, SQLAlchemy, SQLite, JWT Authentication, Python
Frontend: React, Axios, JavaScript

How to run:
Backend:
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

Frontend:
cd frontend
npm install
npm run dev

API Endpoints:
POST /register
POST /login
GET /tasks/
POST /tasks/
PUT /tasks/{id}
DELETE /tasks/{id}

What I learned:
While building this project, I understood how backend and frontend connect, how JWT
authentication works, and how APIs are structured in real applications.


Future improvements:
- Add task deadlines
- Add completed/pending status
- Improve UI design
- Deploy project online
