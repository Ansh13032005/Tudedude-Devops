# Flask & MongoDB Atlas Assignment

This repository contains the solution for the Flask and MongoDB Atlas integration assignment. It features a local REST API endpoint reading mock data and a web form that captures student submissions and stores them in a cloud-hosted MongoDB Atlas database.

## Project Structure

```text
flask-mongodb-assignment/
│── app.py                 # Main Flask application logic & routes
│── data.json              # Mock database for the API endpoint (Question 1)
│── requirements.txt       # Project Python dependencies
│── templates/             # HTML Templates for rendering pages
│   ├── index.html         # Form input page with error feedback
│   └── success.html       # Success page shown after successful database insertion
│── static/                # Static assets (CSS/JS)
└── README.md              # Project documentation
```

---

## Step-by-Step Implementation Guide

### Step 1: Install Required Packages

Run the following command to install the necessary libraries:

```bash
pip install flask pymongo dnspython
```

*   **`flask`**: Python micro web framework.
*   **`pymongo`**: Driver for connecting Python with MongoDB databases.
*   **`dnspython`**: Required to resolve DNS-based SRV connection strings used by MongoDB Atlas.

---

### Step 2: Create Mock JSON Data (`data.json`)

Created a local database fallback containing initial mock records:

```json
[
    {
        "name": "Ansh",
        "course": "DevOps"
    },
    {
        "name": "Rahul",
        "course": "Python"
    }
]
```

---

### Step 3: Write Application Logic (`app.py`)

The main script connects to MongoDB Atlas using the URI and serves three primary routes:
1.  **`/api`**: Serves the contents of `data.json` as JSON.
2.  **`/`**: Displays the registration form template (`index.html`).
3.  **`/submit`**: Accepts POST requests, parses student data, inserts it into MongoDB Atlas, and handles success/error redirections.
4.  **`/success`**: Renders the success message upon insertion.

---

### Step 4: Setup MongoDB Atlas

1.  Sign in to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2.  Create a free shared cluster (e.g. `Cluster0`).
3.  Navigate to **Database Access** and create a new user with read/write access.
4.  Navigate to **Network Access** and select **Add IP Address** -> `0.0.0.0/0` (Allow Access from Anywhere).
5.  Go to **Database** -> Click **Connect** -> Choose **Drivers** -> Copy your Connection URI.
6.  Open `app.py` and replace `MONGO_URI` with your connection string (inserting your database user password).

---

### Step 5: Run the Project

Start the local server with:

```bash
python app.py
```

Open your browser to:
-   **API Endpoint Check**: `http://127.0.0.1:5000/api`
-   **Form Submission Test**: `http://127.0.0.1:5000/`

---

## Git Deployment

Initialize the repository and push to GitHub:

```bash
git init
git add .
git commit -m "Flask MongoDB assignment"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```
