# 🏎️ F1 Hub

**F1 Hub** — Formula 1 bo‘yicha **yangiliklar**, **poygalar (calendar & results)** va **reytinglar (standings)**ni ko‘rsatadigan Django web-loyiha.

Loyiha **Django Templates (HTML/CSS)** asosida qurilgan.  
Frontend tayyor, backend qismi kengaytirishga ochiq.

---

## 🚀 Asosiy imkoniyatlar

### 📰 Yangiliklar
- F1 yangiliklar ro‘yxati
- Qidiruv (search)
- Yangilik tafsilotlari
- Manba bo‘yicha ko‘rsatish (RSS yoki API orqali)

### 🏁 Poygalar
- Formula 1 poygalar taqvimi (season bo‘yicha)
- Har bir Grand Prix sahifasi
- Race results (backend orqali ulanadi)

### 📊 Reyting (Standings)
- Driver standings
- Constructor standings
- Season tanlash imkoniyati

---

## 🛠 Texnologiyalar

- **Python 3**
- **Django**
- **Django Templates (HTML)**
- **Bootstrap 5**
- **SQLite / PostgreSQL (backend tanloviga qarab)**

---

## 📁 Loyiha strukturasi

f1-hub/
├── core/
├── news/
├── races/
├── standings/
├── templates/
│ ├── base.html
│ ├── news/
│ ├── races/
│ └── standings/
├── static/
├── .env
├── .env.example
├── manage.py
└── requirements.txt

yaml
Копировать код

---

## ⚙️ O‘rnatish (Local)

### 1️⃣ Repository’ni yuklab olish
```bash
git clone <repo-url>
cd f1-hub
2️⃣ Virtual environment
bash
Копировать код
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
3️⃣ Kutubxonalarni o‘rnatish
bash
Копировать код
pip install -r requirements.txt
4️⃣ .env sozlash
bash
Копировать код
cp .env.example .env
5️⃣ Serverni ishga tushirish
bash
Копировать код
python manage.py runserver
Brauzerda oching:

cpp
Копировать код
http://127.0.0.1:8000/
🔐 Muhim eslatmalar
.env va db.sqlite3 Git’ga qo‘shilmaydi

.env.example — jamoa uchun namuna

Backend’da API / RSS / F1 data ulash rejalashtirilgan

📌 Rejalashtirilgan kengaytmalar
Real F1 API orqali data olish

RSS orqali yangiliklarni avtomatik yangilash

User login + favorites

Admin panel orqali content boshqarish

Dark mode

👤 Muallif
Azizbek
Django Backend Developer
📍 Uzbekistan

📄 Litsenziya
Bu loyiha o‘quv va portfolio maqsadlarida yaratilgan.

yaml
Копировать код

---

Agar xohlasang:
- README’ni **ingliz tilida**
- GitHub uchun **badge’lar** bilan
- Demo screenshot joyi bilan

ham qilib beraman.
::contentReference[oaicite:0]{index=0}

