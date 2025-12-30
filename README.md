# PrimeTradeAI - Full Stack Web Application

A scalable web application with authentication and dashboard functionality, built with React.js, FastAPI, MySQL, and JWT authentication.

## 📋 Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Postman Collection](#postman-collection)
- [Features](#features)
- [Database Schema](#database-schema)
- [Security Features](#security-features)
- [Production Notes](#production-notes)

## 🛠 Tech Stack

### Frontend
- **React.js** - UI library
- **Tailwind CSS** - Styling framework
- **React Router** - Routing
- **Axios** - HTTP client
- **Vite** - Build tool

### Backend
- **Python 3.8+** - Programming language
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM
- **MySQL** - Database
- **JWT** - Authentication
- **Pydantic** - Data validation
- **Bcrypt** - Password hashing

## 📁 Project Structure

```
primetradeai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── auth.py
│   │   │       │   ├── users.py
│   │   │       │   └── tasks.py
│   │   │       ├── api.py
│   │   │       └── dependencies.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   └── schemas/
│   │       ├── user.py
│   │       ├── task.py
│   │       └── token.py
│   ├── requirements.txt
│   ├── init_db.py
│   ├── run.py
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProtectedRoute.jsx
│   │   │   ├── TaskList.jsx
│   │   │   └── TaskForm.jsx
│   │   ├── contexts/
│   │   │   └── AuthContext.jsx
│   │   ├── pages/
│   │   │   ├── Register.jsx
│   │   │   ├── Login.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── postman/
│   ├── PrimeTradeAI_API.postman_collection.json
│   └── PrimeTradeAI_Environment.postman_environment.json
└── README.md
```

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
2. **Node.js 16+** - [Download Node.js](https://nodejs.org/)
3. **MySQL 8.0+** - [Download MySQL](https://dev.mysql.com/downloads/mysql/)
4. **Postman** (Optional) - [Download Postman](https://www.postman.com/downloads/)

## 🚀 Setup Instructions

### Step 1: MySQL Database Setup

1. **Start MySQL Server**
   ```bash
   # Windows (if MySQL is installed as a service, it should start automatically)
   # Or use MySQL Workbench to start the server
   
   # Linux/Mac
   sudo systemctl start mysql
   # or
   sudo service mysql start
   ```

2. **Create Database**
   ```sql
   mysql -u root -p
   ```
   
   Then in MySQL prompt:
   ```sql
   CREATE DATABASE primetradeai_db;
   SHOW DATABASES;
   EXIT;
   ```

3. **Note your MySQL credentials** (username and password) - you'll need them for the `.env` file.

### Step 2: Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment** (Recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file**
   ```bash
   # Copy the example file
   # Windows
   copy .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   ```

5. **Edit `.env` file** with your MySQL credentials:
   ```env
   DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/primetradeai_db
   SECRET_KEY=your-super-secret-key-change-this-in-production-min-32-characters-long
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   CORS_ORIGINS=http://localhost:3000,http://localhost:5173
   ```
   
   **Important:** Replace `YOUR_PASSWORD` with your actual MySQL root password.

6. **Initialize Database Tables**
   ```bash
   python init_db.py
   ```
   
   You should see: `Database tables created successfully!`

### Step 3: Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

## ▶️ Running the Application

### Start Backend Server

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Activate virtual environment** (if not already activated)
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Run the server**
   ```bash
   python run.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

   The backend will be running at: **http://localhost:8000**

   You can verify it's working by visiting:
   - http://localhost:8000 (root endpoint)
   - http://localhost:8000/health (health check)
   - http://localhost:8000/docs (Swagger UI - Interactive API documentation)

### Start Frontend Server

1. **Open a new terminal** (keep backend running)

2. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

   The frontend will be running at: **http://localhost:3000**

### Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

## 📚 API Documentation

### Authentication Endpoints

#### Register User
```
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "testuser",
  "password": "password123",
  "full_name": "Test User"
}
```

#### Login
```
POST /api/v1/auth/login
Content-Type: application/x-www-form-urlencoded

username=testuser&password=password123
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### User Endpoints (Protected)

#### Get Current User Profile
```
GET /api/v1/users/me
Authorization: Bearer <token>
```

#### Update Current User Profile
```
PUT /api/v1/users/me
Authorization: Bearer <token>
Content-Type: application/json

{
  "email": "newemail@example.com",
  "full_name": "Updated Name"
}
```

### Task Endpoints (Protected)

#### Create Task
```
POST /api/v1/tasks
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Complete assignment",
  "description": "Finish the PrimeTradeAI project"
}
```

#### Get All Tasks
```
GET /api/v1/tasks?skip=0&limit=100&search=keyword&completed=true
Authorization: Bearer <token>
```

#### Get Task by ID
```
GET /api/v1/tasks/{task_id}
Authorization: Bearer <token>
```

#### Update Task
```
PUT /api/v1/tasks/{task_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "description": "Updated description",
  "completed": true
}
```

#### Delete Task
```
DELETE /api/v1/tasks/{task_id}
Authorization: Bearer <token>
```

## 📮 Postman Collection

### Importing the Collection

1. **Open Postman**
2. **Click "Import"** button
3. **Select Files** and choose:
   - `postman/PrimeTradeAI_API.postman_collection.json`
   - `postman/PrimeTradeAI_Environment.postman_environment.json`
4. **Select the environment** "PrimeTradeAI Environment" from the dropdown

### Using the Collection

1. **Set the environment** to "PrimeTradeAI Environment"
2. **Start with Authentication:**
   - Run "Register" to create a new user
   - Run "Login" - this will automatically save the token to the environment variable
3. **All other requests** will automatically use the saved token

### Environment Variables

- `base_url`: http://localhost:8000
- `access_token`: Automatically set after login

## ✨ Features

### Frontend Features
- ✅ User Registration with form validation
- ✅ User Login with error handling
- ✅ Protected Dashboard route
- ✅ User Profile display
- ✅ Task CRUD operations (Create, Read, Update, Delete)
- ✅ Task Search functionality
- ✅ Task Filter by completion status
- ✅ Responsive UI with Tailwind CSS
- ✅ JWT token management
- ✅ Logout functionality

### Backend Features
- ✅ RESTful API with FastAPI
- ✅ JWT-based authentication
- ✅ Secure password hashing with bcrypt
- ✅ User registration and login
- ✅ User profile management
- ✅ Task CRUD operations
- ✅ Search and filter functionality
- ✅ CORS configuration
- ✅ Pydantic validation
- ✅ Proper error handling
- ✅ Database migrations ready

## 🗄 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
);
```

### Tasks Table
```sql
CREATE TABLE tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    user_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

## 🔒 Security Features

1. **Password Hashing**: Bcrypt with automatic salt generation
2. **JWT Tokens**: Secure token-based authentication
3. **CORS**: Configured for specific origins
4. **Input Validation**: Pydantic schemas for all inputs
5. **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
6. **Token Expiration**: Configurable token expiration time
7. **Protected Routes**: Middleware for authentication

## 🚀 Production Notes

### Security Checklist
- [ ] Change `SECRET_KEY` to a strong, random string (minimum 32 characters)
- [ ] Use environment variables for all sensitive data
- [ ] Enable HTTPS in production
- [ ] Configure proper CORS origins (remove localhost)
- [ ] Use a production-grade database (consider connection pooling)
- [ ] Implement rate limiting
- [ ] Add request logging and monitoring
- [ ] Use a reverse proxy (Nginx) in front of FastAPI
- [ ] Set up proper error handling and logging

### Performance Optimization
- [ ] Add database indexes on frequently queried columns
- [ ] Implement caching (Redis) for frequently accessed data
- [ ] Use connection pooling for database
- [ ] Optimize frontend bundle size
- [ ] Implement pagination for large datasets
- [ ] Add CDN for static assets

### Deployment
- **Backend**: Consider using Gunicorn with Uvicorn workers
- **Frontend**: Build with `npm run build` and serve with Nginx
- **Database**: Use managed MySQL service (AWS RDS, etc.)
- **Environment**: Use Docker containers for easy deployment

### Environment Variables for Production
```env
DATABASE_URL=mysql+pymysql://user:password@db-host:3306/primetradeai_db
SECRET_KEY=<generate-strong-random-key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
CORS_ORIGINS=https://yourdomain.com
```

## ✅ Final Checklist

Before submitting, verify:

- [ ] Backend server starts without errors
- [ ] Frontend server starts without errors
- [ ] Database connection works
- [ ] User registration works
- [ ] User login works and token is generated
- [ ] Dashboard loads with user profile
- [ ] Can create a new task
- [ ] Can view all tasks
- [ ] Can search tasks
- [ ] Can filter tasks by status
- [ ] Can update a task
- [ ] Can delete a task
- [ ] Can update user profile
- [ ] Logout works and redirects to login
- [ ] Protected routes redirect to login when not authenticated
- [ ] All Postman API requests work
- [ ] Form validation works on frontend
- [ ] Server errors are displayed on frontend

## 🐛 Troubleshooting

### Backend Issues

**Database Connection Error:**
- Verify MySQL is running
- Check database credentials in `.env`
- Ensure database `primetradeai_db` exists

**Module Not Found:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

**Port Already in Use:**
- Change port in `run.py` or kill the process using port 8000


