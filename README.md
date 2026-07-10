# 🚀 AI-Powered Task & Knowledge Management System

An AI-powered Task & Knowledge Management System that combines **Task Management**, **Document Management**, and **Retrieval-Augmented Generation (RAG)** to help users organize tasks and retrieve accurate information from uploaded documents using AI.

The system allows users to upload PDF/TXT documents, assign them to tasks, and ask AI questions related only to the documents linked with that task.

---

## 📌 Features

### 👤 User Management
- User Registration
- JWT Authentication
- Role-Based Access Control (Admin, Manager, Employee)

### 📂 Document Management
- Upload PDF Documents
- Upload TXT Documents
- Store document metadata in MySQL
- Automatic text extraction
- Automatic document chunking
- FAISS Vector Indexing

### ✅ Task Management
- Create Tasks
- Assign Tasks
- Set Priority
- Set Deadline
- Track Task Status
- Link Multiple Documents to Tasks

### 🤖 AI Assistant (RAG)
- Semantic Search using FAISS
- SentenceTransformer Embeddings
- Groq LLM Integration
- Task-Specific AI Chat
- AI answers only from linked documents

### 📊 Activity Logs
- User Activity Tracking
- Document Upload Logs
- Task Creation Logs
- AI Query Logs

---

# 🛠 Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- MySQL
- JWT Authentication
- Pydantic

## AI Stack
- Groq API
- Llama 3.3 70B Versatile
- Sentence Transformers
- FAISS
- LangChain Document Loaders

---

# 📁 Project Structure

```
AI-Task-Knowledge-System
│
├── backend
│   ├── app
│   │   ├── core/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── uploads/
│   │   ├── vector_store/
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── .env
│   └── test_search.py
│
│
└── README.md
```

---

# 🏗 System Architecture

```

                  FastAPI Backend
                        │
        ┌───────────────┼───────────────┐
        │               │               │
     Authentication    MySQL        AI Service
        │               │               │
        │               │          FAISS Vector DB
        │               │               │
        │               │     Sentence Transformers
        │               │               │
        └──────────────► Groq LLM ◄─────┘
```

---

# 🧠 AI Workflow

```
Upload PDF / TXT
        │
        ▼
Extract Text
        │
        ▼
Text Chunking
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS
        │
        ▼
User Question
        │
        ▼
Semantic Search
        │
        ▼
Top Relevant Chunks
        │
        ▼
Groq LLM
        │
        ▼
AI Response
```

---

# 🗄 Database Schema

## Roles

| Field | Type |
|------|------|
| id | Integer |
| role_name | String |

---

## Users

| Field | Type |
|------|------|
| id | Integer |
| name | String |
| email | String |
| password | String |
| role_id | Foreign Key |

---

## Documents

| Field | Type |
|------|------|
| id | Integer |
| title | String |
| filename | String |
| filepath | String |
| uploaded_by | Foreign Key |
| uploaded_at | DateTime |

---

## Tasks

| Field | Type |
|------|------|
| id | Integer |
| title | String |
| description | Text |
| priority | String |
| status | String |
| deadline | DateTime |
| assigned_to | Foreign Key |
| created_by | Foreign Key |
| created_at | DateTime |

---

## Task Documents

Many-to-Many Relationship

| task_id | document_id |

---

## Activity Logs

| Field | Type |
|------|------|
| id | Integer |
| user_id | Foreign Key |
| action | String |
| timestamp | DateTime |

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/1-ashish-04/AI-Powered-Task-Knowledge-System.git

cd AI-Task-Knowledge-System
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv .venv
```

### Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file inside the backend folder.

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ai_task_db
DB_USER=root
DB_PASSWORD=your_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

GROQ_API_KEY=your_groq_api_key
```

---

## 5. Create Database

```sql
CREATE DATABASE ai_task_db;
```

---

## 6. Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

# 📄 Supported Documents

- PDF (.pdf)
- Text (.txt)

---

# 🔐 Authentication

Login using

```
POST /auth/login
```

Copy the generated JWT Token.

Click **Authorize** in Swagger and enter

```
Bearer YOUR_ACCESS_TOKEN
```

---

# 📚 API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/auth/login` |

---

## Users

| Method | Endpoint |
|---------|----------|
| POST | `/users/` |

---

## Documents

| Method | Endpoint |
|---------|----------|
| POST | `/documents/upload` |

---

## Tasks

| Method | Endpoint |
|---------|----------|
| POST | `/tasks/` |
| POST | `/tasks/{task_id}/documents` |

---

## AI Chat

| Method | Endpoint |
|---------|----------|
| POST | `/chat` |

Example Request

```json
{
    "task_id": 1,
    "question": "Explain Python variables."
}
```

---

# 🧪 RAG Flow

```
User Question
      │
      ▼
Selected Task
      │
      ▼
Retrieve Linked Documents
      │
      ▼
Semantic Search (FAISS)
      │
      ▼
Top Matching Chunks
      │
      ▼
Groq LLM
      │
      ▼
AI Response
```

---

# 📌 Current Progress

- ✅ User Authentication
- ✅ JWT Authorization
- ✅ Role Management
- ✅ Document Upload
- ✅ PDF Processing
- ✅ TXT Processing
- ✅ SentenceTransformer Embeddings
- ✅ FAISS Vector Database
- ✅ Document Indexing
- ✅ Task Creation
- ✅ Task Assignment
- ✅ Task-Document Linking
- ✅ AI Chat using Groq
- 🚧 Activity Logs
- 🚧 React Dashboard
- 🚧 Analytics

# 🚀 Future Improvements

- React Dashboard
- User Profile Management
- Task Update/Delete APIs
- Document Preview
- AI Task Summarization
- Activity Dashboard
- Notifications
- Email Integration
- Docker Support
- CI/CD Pipeline
- Deployment on AWS/Azure

---

# 👨‍💻 Author

**Ashish Jayaswal**

- Python Full Stack Developer
- FastAPI | React | SQL | FAISS | RAG | Groq | GenAI

---

# 📜 License

This project is developed for educational and learning purposes. You are free to use, modify, and extend it for personal or academic projects.