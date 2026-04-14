# 🎓 SmartEdu API: Education Management System

SmartEdu API, modern bir eğitim yönetim sisteminin backend altyapısını simüle eden, **Django REST Framework** tabanlı ve **Dockerize** edilmiş profesyonel bir API projesidir. Proje, ölçeklenebilir bir mimari ile güvenli veri yönetimini hedefler.

---

###  Teknik Yetkinlikler & Mimari

Bu proje, bir mühendis olarak aşağıdaki konulardaki yetkinliklerimi sergilemek üzere geliştirilmiştir:

* **RESTful Mimari:** Tam uyumlu CRUD operasyonları ve modüler uygulama yapısı.
* **İlişkisel Veritabanı (ORM):** `Teacher`, `Course` ve `Student` modelleri arasında **One-to-Many** ve **Many-to-Many** ilişkisel modelleme.
* **Güvenlik & Auth:** **SimpleJWT** entegrasyonu ile güvenli token tabanlı kimlik doğrulama.
* **Konteynerizasyon:** Uygulamanın her ortamda tutarlı çalışması için **Docker** altyapısı.
* **Deployment:** CI/CD süreçlerine uygun şekilde **Render** üzerinden canlıya alma.

###  Teknolojik Stack

- **Dil & Framework:** Python 3.12.6 , Django 6.0.4
- **API Engine:** Django REST Framework (DRF)
- **Güvenlik:** JSON Web Token (JWT)
- **Altyapı:** Docker, Dockerfile, .dockerignore
- **Veritabanı:** SQLite (Geliştirme süreci için optimize edilmiş)

---

###  Docker

Uygulamayı yerel ortamınızda saniyeler içinde ayağa kaldırabilirsiniz:

```bash
# 1. Docker imajını oluşturun
docker build -t smartedu-app .

# 2. Konteynerı çalıştırın (Port 8000 üzerinden)
docker run -p 8000:8000 smartedu-app
```
API Erişimi: http://localhost:8000/api/

Admin Paneli: http://localhost:8000/admin/

### 🌐 Canlı Demo (Live API)
Uygulama Dockerize edilerek Render üzerinde canlıya alınmıştır. Herhangi bir kurulum yapmadan aşağıdaki link üzerinden API'yi test edebilirsiniz:
🔗 **Canlı API Adresi:** https://smartedu-api.onrender.com

| Kaynak | Endpoint | Erişim Türü |
|--------|----------|-------------|
| Kurslar | `/api/` | Herkese Açık |
| Token Al (Giriş) | `/api/token/` | Kayıtlı Kullanıcı |
| Yönetim Paneli | `/admin/` | Superuser |
