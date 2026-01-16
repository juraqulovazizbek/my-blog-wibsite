# 🏎️ F1 Hub — Django Web Application

**F1 Hub** — Formula 1 mavzusiga bag‘ishlangan web-ilova bo‘lib, unda:
- 📰 F1 **yangiliklari**
- 🏁 F1 **poygalar taqvimi va natijalari**
- 📊 **Driver va Constructor reytinglari**

ko‘rsatiladi.

Loyiha **Django** asosida qurilgan va **Django Templates (HTML/CSS)** yordamida frontend qismi ishlab chiqilgan.

---

## 🎯 Loyiha maqsadi

Ushbu loyiha:
- Django’da **toza struktura** bilan ishlashni
- Frontend va backend qismlarini **ajratib yozishni**
- Real sport ma’lumotlari bilan ishlashga tayyor backend yaratishni

o‘rganish va namoyish qilish uchun ishlab chiqilgan.

---

## 🚀 Asosiy funksiyalar

### 📰 Yangiliklar (News)
- F1 yangiliklar ro‘yxati
- Yangilik detail sahifasi
- Qidiruv (search)
- RSS yoki API ulashga tayyor

### 🏁 Poygalar (Races)
- Formula 1 poygalar taqvimi
- Har bir Grand Prix uchun alohida sahifa
- Race results (backend orqali)
- Season bo‘yicha filter

### 📊 Reyting (Standings)
- Driver standings
- Constructor standings
- Season bo‘yicha ko‘rish

---

## 🧱 Loyiha arxitekturasi

- `core/` — Django project (settings, urls, wsgi, asgi)
- `news/` — yangiliklar
- `races/` — poygalar
- `standings/` — reytinglar
- `templates/` — HTML frontend
- `static/` — CSS va rasmlar

---

## 📁 Papka strukturasi

my-blog-wibsite/
├── core/
├── news/
├── races/
├── standings/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── .env
├── .env.example
└── README.md

yaml
Копировать код

---

## ⚙️ Local’da ishga tushirish

### 1️⃣ Repository’ni klonlash
```bash
git clone https://github.com/juraqulovazizbek/my-blog-wibsite.git
cd my-blog-wibsite
2️⃣ Virtual environment
bash
Копировать код
python -m venv .venv
Aktivatsiya:

bash
Копировать код
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
3️⃣ Kutubxonalarni o‘rnatish
bash
Копировать код
pip install -r requirements.txt
4️⃣ Environment sozlash
bash
Копировать код
cp .env.example .env
5️⃣ Server
bash
Копировать код
python manage.py migrate
python manage.py runserver
Brauzer:

cpp
Копировать код
http://127.0.0.1:8000/
🔐 Muhim eslatmalar
.env, .venv, db.sqlite3 GitHub’ga yuklanmaydi

Maxfiy sozlamalar .env ichida

.env.example — namuna fayl

🛠 Rejalashtirilgan kengaytmalar
F1 API ulash

RSS auto update

User login/register

Favorite driver/team

Deploy (Render / Railway)

👤 Muallif
Azizbek
Django Backend Developer
Uzbekistan