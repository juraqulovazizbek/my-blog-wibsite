# 🏎️ F1 Hub — Django Project

Bu loyiha mening **birinchi mustaqil Django loyiham** hisoblanadi.  
Loyiha Formula 1 mavzusiga bag‘ishlangan bo‘lib, kelajakda:

- 📰 F1 yangiliklari  
- 🏁 F1 poygalar (calendar va natijalar)  
- 📊 Driver va Constructor reytinglari  

ni ko‘rsatadigan web-ilova bo‘lishi rejalashtirilgan.

Hozircha loyiha **rivojlanish bosqichida**.

---

## 🎯 Loyiha maqsadi

Bu loyihani yaratishdan maqsad:

- Django framework’ni **amaliyotda o‘rganish**
- Project va app’lar bilan **to‘g‘ri ishlash**
- Frontend (HTML templates) va backend’ni **ajratib yozishni tushunish**
- GitHub bilan ishlashni (commit, push, merge) o‘rganish

---

## 🛠 Texnologiyalar

- Python 3
- Django
- Django Templates (HTML)
- CSS
- Git & GitHub
- SQLite (hozircha)

---

## 📌 Hozirgi holati

✅ Loyiha strukturasi yaratildi  
✅ Django project va app’lar tayyor  
✅ Frontend HTML sahifalar yozildi  
❌ Backend logika hali to‘liq yozilmagan  
❌ Real F1 API yoki RSS hali ulanmagan  

> Loyiha ustida ish **davom etmoqda**.

---

## 🧱 Loyiha strukturasi

my-blog-wibsite/
├── core/ # Django project (settings, urls)
├── news/ # Yangiliklar uchun app
├── races/ # Poygalar uchun app
├── standings/ # Reytinglar uchun app
├── templates/ # HTML frontend
├── static/ # CSS va rasmlar
├── manage.py
├── requirements.txt
├── .env.example
└── README.md


---

## 📄 App’lar haqida

### 📰 news
F1 yangiliklarini ko‘rsatish uchun mo‘ljallangan.  
Hozircha faqat HTML sahifalar mavjud.

### 🏁 races
Formula 1 poygalar taqvimi va natijalari uchun.  
Backend qismi keyinchalik yoziladi.

### 📊 standings
Driver va Constructor reytinglari uchun.  
Hozircha frontend tayyor.

---

## ⚙️ Local’da ishga tushirish

### 1️⃣ Repository’ni klonlash
```bash
git clone https://github.com/juraqulovazizbek/my-blog-wibsite.git
cd my-blog-wibsite


2️⃣ Virtual environment yaratish
python -m venv .venv


Aktivatsiya:

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

3️⃣ Kutubxonalarni o‘rnatish
pip install -r requirements.txt

4️⃣ Serverni ishga tushirish
python manage.py runserver


Brauzerda:

http://127.0.0.1:8000/

🔐 Muhim eslatmalar

.env, .venv, db.sqlite3 GitHub’ga yuklanmaydi

Maxfiy ma’lumotlar .env ichida saqlanadi

.env.example — namuna fayl

🚧 Kelajakda qilinadigan ishlar

F1 API yoki RSS ulash

Backend logic (models, views)

Pagination va search

Admin panel

User login/register

Deploy (Render yoki Railway)

👤 Muallif

Azizbek
Boshlovchi Django Backend Developer
Uzbekistan 🇺🇿

📌 Eslatma

Bu loyiha o‘rganish va tajriba orttirish maqsadida yaratilgan.
Vaqt o‘tishi bilan loyiha bosqichma-bosqich rivojlantiriladi.

#
#
#git push origin main