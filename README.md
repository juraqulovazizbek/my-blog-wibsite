🏎️ Formula 1 Blog Website

Bu mening **birinchi Django loyiham**.  
Loyiha Formula 1 mavzusida bo‘lib, unda F1 yangiliklari, poygalar va reytinglarni ko‘rsatish rejalashtirilgan.

Hozircha loyiha **boshlang‘ich bosqichda**. Frontend va loyiha strukturasi mavjud, backend qismi esa **keyinchalik bosqichma-bosqich qo‘shiladi**.

---

## 🎯 Loyihaning maqsadi
Bu loyiha orqali men:
- Django framework bilan ishlashni
- Project va app’larni to‘g‘ri ajratishni
- Git va GitHub bilan ishlashni
- Frontend (HTML, CSS) va backend’ni birlashtirishni
o‘rganmoqdaman.

---

## 🚧 Loyiha holati
- ✅ Loyiha strukturasi tayyor
- ✅ HTML template’lar mavjud
- ❌ Backend (models, views, database) hali to‘liq yozilmagan
- 🔜 Keyingi bosqichlarda backend qo‘shiladi

Bu **o‘quv (education) loyiha** hisoblanadi.

---

## 📌 Rejalashtirilgan funksiyalar
- 📰 Formula 1 yangiliklarini ko‘rsatish
- 🏁 Poygalar jadvali
- 🏆 Haydovchilar (Driver) reytingi
- 🏆 Jamoalar (Constructor) reytingi
- 🎨 Oddiy va tushunarli frontend
- ⚙️ Django backend

---

## 🗂️ Loyiha strukturasi
```text
my-blog-wibsite/
├── core/                # Django project (settings, urls, wsgi)
├── news/                # Yangiliklar uchun app
├── races/               # Poygalar uchun app
├── standings/           # Reytinglar uchun app
├── templates/           # HTML sahifalar
├── static/              # CSS, JS, rasmlar
├── manage.py
├── requirements.txt     # Kutubxonalar ro‘yxati
├── .env.example         # Muhit sozlamalari namunasi
└── README.md
💻 Ishga tushirish bo‘yicha qo‘llanma
1️⃣ Repository’ni yuklab olish
bash
Копировать код
git clone https://github.com/juraqulovazizbek/my-blog-wibsite.git
cd my-blog-wibsite
2️⃣ Virtual environment yaratish
Virtual muhit kutubxonalarni alohida saqlash uchun kerak.

bash
Копировать код
python -m venv .venv
3️⃣ Virtual environment’ni yoqish
Windows:

bash
Копировать код
.venv\Scripts\activate
Mac / Linux:

bash
Копировать код
source .venv/bin/activate
4️⃣ Kerakli kutubxonalarni o‘rnatish
bash
Копировать код
pip install -r requirements.txt
5️⃣ .env fayl yaratish
Bu faylda maxfiy sozlamalar bo‘ladi.

bash
Копировать код
copy .env.example .env
So‘ng .env ichini kerakli qiymatlar bilan to‘ldiring.

6️⃣ Serverni ishga tushirish
bash
Копировать код
python manage.py runserver
Brauzerda oching:
👉 http://127.0.0.1:8000/

🧠 Rejalashtirilgan model’lar
Kelajakda quyidagi model’lar qo‘shiladi:

News – yangiliklar

Race – poygalar

DriverStanding – haydovchilar reytingi

ConstructorStanding – jamoalar reytingi

📸 Screenshotlar
Hozircha mavjud emas.
Keyinchalik loyiha rivojlangach qo‘shiladi.

📄 License
Ushbu loyiha o‘quv maqsadida yaratilgan.

👤 Muallif
Azizbek Juraqulov
GitHub: https://github.com/juraqulovazizbek

⭐ Agar loyiha yoqsa, yulduzcha (star) bosib qo‘yishingiz mumkin 🙂


