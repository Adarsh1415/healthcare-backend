🏥 Healthcare Backend System

A foundational Flask backend system with secure user authentication and role-based access control (RBAC).
This project serves as the base for a larger healthcare application, supporting Admin, Doctor, and Member roles.

✨ Features

🔑 JWT Authentication (/auth/register, /auth/login)

👥 Role-Based Access Control (RBAC)

Admin: Manage departments & onboard doctors

Doctor & Member: Restricted access

🗂️ Departments Management (Create & list departments)

🩺 Doctor Management

Onboard doctors

Assign doctors to departments

List doctors

🔒 Password Security with Bcrypt hashing

🗃️ Database ORM with SQLAlchemy

👨‍⚕️ Default Admin User auto-created at startup


⚙️ Installation & Setup
1. Clone the repo
git clone https://github.com/your-username/healthcare-backend.git
cd healthcare-backend

2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables (in .env or config)
FLASK_APP=app.py
FLASK_ENV=development
JWT_SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db

5. Run the app
python app.py


🚀 API Endpoints
🔐 Auth Routes
Method	Endpoint	Description	Access
POST	/auth/register	Register new user	Public
POST	/auth/login	Login & get JWT token	Public
🛠️ Admin Routes (JWT + Admin Only)

Departments

Method	Endpoint	Description
POST	/admin/departments	Create a department
GET	/admin/departments	List all departments
GET	/admin/departments/<id>/doctors	List doctors in department

Doctors

Method	Endpoint	Description
POST	/admin/doctors	Onboard a new doctor
GET	/admin/doctors	List all doctors
PUT	/admin/doctors/<id>	Assign doctor to a department
🔒 Authentication & RBAC

JWT is generated on login and must be included in headers:

Authorization: Bearer <JWT_TOKEN>

🛠️ Tech Stack

Flask – Web framework

Flask-JWT-Extended – JWT Authentication

SQLAlchemy – ORM

Flask-Bcrypt – Password hashing

SQLite – Default database (can be switched to PostgreSQL/MySQL)

