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
- Frontend (templates) va backend (logic)ni **ajratib yozishni**
- Real dunyodagi sport ma’lumotlari bilan ishlashga tayyor backend yaratishni

o‘rganish va namoyish qilish uchun ishlab chiqilgan.

---

## 🚀 Asosiy funksiyalar

### 📰 Yangiliklar (News)
- F1 yangiliklar ro‘yxati
- Har bir yangilik uchun alohida sahifa
- Qidiruv (search)
- RSS yoki API orqali real yangiliklarni ulashga tayyor

### 🏁 Poygalar (Races)
- Formula 1 mavsum poygalar taqvimi
- Har bir Grand Prix uchun detail sahifa
- Race results (backend orqali to‘ldiriladi)
- Season (yil) bo‘yicha filter

### 📊 Reyting (Standings)
- Driver standings
- Constructor standings
- Season bo‘yicha reytinglarni ko‘rish

---

## 🧱 Loyiha arxitekturasi

Loyiha **modulli yondashuv** asosida yozilgan.

### Project (asosiy sozlamalar)
- `core/` — Django project (settings, urls, wsgi, asgi)

### App’lar
- `news/` — yangiliklar logikasi
- `races/` — poygalar va natijalar
- `standings/` — reytinglar

### Frontend
- `templates/` — barcha HTML template’lar
- `static/` — CSS, rasmlar va boshqa static fayllar

---

## 📁 Papka strukturasi

my-blog-wibsite/
├── core/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── news/
├── races/
├── standings/
│
├── templates/
│ ├── base.html
│ ├── news/
│ ├── races/
│ └── standings/
│
├── static/
│ ├── css/
│ └── img/
│
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
2️⃣ Virtual environment yaratish
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
5️⃣ Migratsiyalar va server
bash
Копировать код
python manage.py migrate
python manage.py runserver
Brauzerda oching:

cpp
Копировать код
http://127.0.0.1:8000/
🔐 Muhim eslatmalar
.env, .venv, db.sqlite3 GitHub’ga yuklanmaydi

Maxfiy ma’lumotlar .env ichida saqlanadi

.env.example — loyiha uchun namuna fayl

🛠 Kelajakda qo‘shilishi rejalashtirilgan
Real F1 API bilan poygalar va reytinglarni olish

RSS orqali yangiliklarni avtomatik yangilash

User authentication (login/register)

Favorite driver / team

Admin panel orqali content boshqarish

Deploy (Render / Railway / VPS)

👤 Muallif
Azizbek
Django Backend Developer
📍 Uzbekistan

📄 Litsenziya
Ushbu loyiha o‘quv va portfolio maqsadlarida ishlab chiqilgan.

markdown
Копировать код

---

## ✅ QANDAY QO‘LLAYSAN
1. `README.md` ni och  
2. Ichidagi hamma narsani o‘chir  
3. Yuqoridagi **butun blokni** paste qil  
4. Saqla → `git commit` → `git push`

Agar xohlasang:
- README’ni **ingliz tilida**
- yoki **yana ham professional (job-ready)** variantini  
- yoki **Najot Talim topshiriq formatida**

ham qilib beraman.
::contentReference[oaicite:0]{index=0}
