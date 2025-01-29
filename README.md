#  Django CashFlow Tracker

**Django-приложение для управления движением денежных средств (ДДС).**

## 🚀 Функциональность
- **Добавление/редактирование/удаление транзакций.**
- **Фильтрация записей** по статусу, типу, категории, подкатегории и дате.
- **Динамическое обновление категорий и подкатегорий** (без перезагрузки страницы).
- **Управление справочниками** (статусы, типы, категории, подкатегории).
- **Адаптивный интерфейс** (Bootstrap).

## 🛠️ Установка и запуск
### 1️⃣ **Клонируем репозиторий**
```sh
git clone https://github.com/ВАШ_ЛОГИН/cashflow-tracker.git
cd cashflow-tracker

### 2️⃣ **Создаем виртуальное окружение
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate

### 3️⃣ **Устанавливаем зависимости
    pip install -r requirements.txt

### 4️⃣ **Настройка переменных окружения
Создайте файл .env и добавьте:
    DEBUG=True
    SECRET_KEY=your_secret_key
    ALLOWED_HOSTS=127.0.0.1,localhost   

### 5️⃣ **Запускаем сервер
python manage.py migrate  # Применяем миграции
python manage.py createsuperuser  # Создаем администратора
python manage.py runserver  # Запускаем сервер

Приложение будет доступно по адресу: http://127.0.0.1:8000.

## 🔧 Используемые технологии
Django — Python-фреймворк для веб-разработки.
Django REST Framework — для работы с API.
Bootstrap — стилизация интерфейса.
JavaScript (Vanilla) — для динамической подгрузки категорий и подкатегорий.


## 📝 Автор
👨‍💻 Гагик Абраамян
📧 abraamyangagik10@gmail.com
🐙 https://github.com/IamGagik