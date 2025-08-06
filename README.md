
# 🎫 Movie Ticket Management System

A comprehensive **Ticket Management System** designed to handle support, issue, or service tickets efficiently—ideal for movie screenings and other events.

---

## 🧩 Overview

This project offers:

- CRUD operations for tickets: create, view, update, delete
- Option to update the content of tables
- Option to book and print tickets of any movie selected
  

## 📁 Project Structure

```
/
├── backend/               # Server-side code
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   └── README.md
├── frontend/              # UI Layer
│   ├── src/
│   └── public/
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🛠 Technologies Used

- **Backend**: Python
- **Database**: SQLITE3
- **Frontend**: Python tkinter
- **Auth**: Password based authentication

---

## 🚀 Getting Started

### Prerequisites

- Node.js (v14+), npm or yarn
- Running database instance (MongoDB, PostgreSQL)

### Setup Steps

1. Clone the repository  
   ```bash
   git clone https://github.com/GayatriPadhii/Ticket-Management-System.git
   cd Ticket-Management-System
   ```

2. Install server dependencies  
   ```bash
   cd backend
   npm install
   ```

3. Configure environment variables (create `.env` in `backend/`):  
   ```
   DATABASE_URI=your_db_connection_string
   JWT_SECRET=your_secret_key
   PORT=3000
   ```

4. Start the server  
   ```bash
   npm run dev
   ```

5. (If frontend exists)  
   ```bash
   cd ../frontend
   npm install
   npm start
   ```

Access the app at `http://localhost:3000`.

---

## 📂 API Endpoints

| Method | Endpoint            | Description                         |
|--------|---------------------|-------------------------------------|
| POST   | `/api/tickets`      | Create a new ticket                 |
| GET    | `/api/tickets`      | Retrieve all tickets                |
| GET    | `/api/tickets/:id`  | Get a specific ticket by ID         |
| PUT    | `/api/tickets/:id`  | Update ticket details/status        |
| DELETE | `/api/tickets/:id`  | Remove a ticket by ID               |

---

## 🙌 Contributing

Feel free to submit PRs, open issues, or suggest features. Please follow project coding conventions and include relevant tests.

---




