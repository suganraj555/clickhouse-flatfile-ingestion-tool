# 🔄 Bidirectional ClickHouse & Flat File Data Ingestion Tool

A web-based tool that supports **bidirectional data ingestion** between a **ClickHouse database** and **Flat Files (CSV)**. The app includes features like JWT-based authentication, column selection, data preview, progress tracking, and detailed reporting.

---

## 📌 Features

- ✅ Bidirectional data ingestion:
  - ClickHouse ➡️ Flat File
  - Flat File ➡️ ClickHouse
- ✅ JWT authentication for ClickHouse
- ✅ Column selection UI
- ✅ Schema discovery
- ✅ Record count reporting
- ✅ Error handling with user-friendly messages
- ✅ Attractive React-based frontend
- ✅ FastAPI backend

### 🔥 Bonus Features
- 🔗 ClickHouse multi-table joins with JOIN conditions
- 👀 Data preview before ingestion
- 📊 Ingestion progress bar

---

## ⚙️ Technologies Used

- **Frontend**: React.js + TailwindCSS
- **Backend**: FastAPI (Python)
- **Database**: ClickHouse
- **Others**: Pandas, Uvicorn, JWT, Axios

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/clickhouse-flatfile-ingestion-tool.git
cd clickhouse-flatfile-ingestion-tool
```

---

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### 🔐 Environment Variables (Optional)

If needed, create a `.env` file for credentials:

```env
CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=8123
CLICKHOUSE_DB=default
CLICKHOUSE_USER=default
JWT_TOKEN=your_jwt_token
```

#### Run Backend

```bash
uvicorn main:app --reload
```

---

### 3. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

---

## 📁 Project Structure

```
clickhouse-flatfile-ingestion-tool/
├── backend/
│   ├── main.py
│   ├── clickhouse.py
│   ├── flatfile.py
│   ├── ingestion.py
│   └── utils/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   └── tailwind.config.js
├── README.md
└── prompts.txt
```

---

## ✅ Test Cases

1. ✅ ClickHouse ➡️ Flat File (selected columns)
2. ✅ Flat File ➡️ ClickHouse (new table)
3. ✅ Multi-table JOIN ➡️ Flat File
4. ❌ Fail cases: wrong JWT, wrong host
5. 👀 Data preview for first 100 records

---

## 🤖 AI Tool Prompts (prompts.txt)

This project used AI to help generate:
- Backend logic
- FastAPI JWT integration
- React UI components
- Styling with TailwindCSS
- JOIN query builders

All prompts are recorded in `prompts.txt`

---

## 📸 Demo (Optional)

If you recorded a demo:

👉 [Demo Video on YouTube](https://youtu.be/your-demo-link)

---

## 📄 License

MIT License

---

## ✨ Author

Made with ❤️ by [Your Name](https://github.com/your-username)
