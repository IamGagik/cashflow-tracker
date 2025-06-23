# 💸 Django CashFlow Tracker

**A Django-based web application for managing and tracking cash flow.**

---

## 🚀 Features

- **Create, edit, and delete transactions**
- **Filter records** by status, type, category, subcategory, and date
- **Dynamic category and subcategory updates** (without page reload)
- **Manage directories**: statuses, types, categories, subcategories
- **Responsive interface** (Bootstrap-powered)

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cashflow-tracker.git
cd cashflow-tracker
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables

Create a `.env` file in the project root with the following content:

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5️⃣ Run the application

```bash
python manage.py migrate           # Apply migrations
python manage.py createsuperuser   # Create admin user
python manage.py runserver         # Start the development server
```

The app will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔧 Tech Stack

- **Django** — Python web framework  
- **Django REST Framework** — for building APIs  
- **Bootstrap** — for responsive styling  
- **Vanilla JavaScript** — for dynamic category/subcategory loading  

---

## 📝 Author

👨‍💻 Gagik Abrahamyan  
📧 abraamyangagik10@gmail.com  
🐙 [github.com/IamGagik](https://github.com/IamGagik)
