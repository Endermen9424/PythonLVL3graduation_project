# 📚 ElaAdmin - Eğitim Yönetim Sistemi

## 📖 Proje Açıklaması

Bu proje, öğretmenlerin dersler oluşturabileceği, YouTube üzerinden ders videoları paylaşabileceği, kısa sınavlar hazırlayabileceği ve öğrencileri puanlama sistemiyle değerlendirebileceği **web tabanlı bir çevrimiçi öğrenme platformudur**. 

Bu proje, **ClassDojo** adlı bir uygulamadan esinlenilmiştir. Bazı ek fikirler olsa da, temel amacı ClassDojo'ya benzer. **Yazılım açısından tamamen özgün kod kullanılmıştır.**

---

## 🎯 Ana Özellikleri

- ✅ **Öğrenci Yönetimi** - Öğrencileri sınıflara göre organize edin ve yönetin
- ✅ **Ders Oluşturma** - YouTube videolarıyla zengin ders içeriği hazırlayın
- ✅ **Sınav Sistemi** - Çoktan seçmeli sınavlar oluşturun ve yönetin
- ✅ **Puanlama Sistemi** - Öğrenci performansını puanlarla değerlendirin
- ✅ **Kolay Yönetim** - Basit ve kullanıcı dostu arayüz
- ✅ **Veri Güvenliği** - Tüm veriler güvenli bir şekilde saklanır

---

## 🛠️ Teknoloji Stack'i

| Teknoloji | Açıklama |
|-----------|----------|
| **Backend** | Python Flask |
| **Frontend** | HTML, CSS, JavaScript |
| **Database** | SQLite3 |
| **Data Format** | JSON |
| **Web Server** | Flask Built-in Server |

---

## 📊 Veritabanı Yapısı

```
School System
├── Classes (Sınıflar)
│   ├── id (Primary Key)
│   └── name (Sınıf Adı)
│
├── Teachers (Öğretmenler)
│   ├── id (Primary Key)
│   ├── name (Adı)
│   ├── email (E-posta)
│   └── password (Şifre)
│
├── Students (Öğrenciler)
│   ├── id (Primary Key)
│   ├── name (Adı)
│   ├── school_no (Okul Numarası)
│   ├── class_id (Foreign Key - Sınıf)
│   └── points (Puanlar)
│
└── Lessons (Dersler)
    ├── id (Primary Key)
    ├── lesson_name (Ders Adı)
    ├── topic_name (Konu Adı)
    ├── description (Açıklama)
    ├── youtube_url (Video URL'i)
    └── class_id (Foreign Key)

Tests (JSON Files)
├── exam_name (Sınav Adı)
├── exam_description (Açıklama)
├── lesson_name (Ders Adı)
└── exam_data (Sorular Dizisi)
    └── [Question Objects]
        ├── question (Soru Metni)
        ├── options (A, B, C, D Seçenekleri)
        └── correct (Doğru Cevap Index'i)
```

---

## 🚀 Kurulum ve Kullanım

### Gereksinimler

- Python 3.7 veya üzeri
- pip (Python paket yöneticisi)
- Flask web framework'ü

### Kurulum Adımları

```bash
# 1. Depoyu klonlayın
git clone [repository-url]

# 2. Proje dizinine gidin
cd PythonLVL3graduation_project

# 3. Flask'ı yükleyin
pip install flask

# 4. Uygulamayı çalıştırın
python main.py

# 5. Tarayıcıda açın
http://localhost:5000
```

---

## 📁 Proje Yapısı

```
PythonLVL3graduation_project/
├── main.py                      # Flask uygulaması (Ana dosya)
├── DBmanager.py                # Veritabanı yönetim sınıfı
├── JsonManager.py              # JSON dosya işlemleri
├── README.md                   # Proje açıklaması
│
├── static/
│   └── css/
│       └── style.css           # Ana CSS dosyası
│
├── image/                      # Görseller dizini
│
├── templates/                  # HTML şablonları
│   ├── index.html             # Anasayfa
│   ├── ogrenciler.html        # Öğrenci yönetimi
│   ├── addstudents.html       # Öğrenci ekleme
│   ├── dersler.html           # Ders yönetimi
│   ├── addders.html           # Ders ekleme
│   ├── exam.html              # Sınav listesi
│   ├── exam_add.html          # Sınav ekleme
│   ├── exam_edit.html         # Sınav düzenleme
│   ├── addclass.html          # Sınıf ekleme
│   └── ayarlar.html           # Ayarlar
│
└── Testjsons/                 # Sınav JSON dosyaları dizini
    ├── Canlılar.json
    ├── Fonksiyonlar.json
    └── [Diğer sınav dosyaları]
```

---

## 📖 Temel Özellikler Detayı

### 🎓 Öğrenci Yönetimi

- Öğrencileri sisteme ekleyin, sınıflandırın ve düzenleyin
- Her öğrencinin okul numarası, adı ve sınıfı gibi bilgiler kaydedilir
- Öğrenci puanlarını takip edin ve sınavlardaki performanslarını değerlendirin
- Öğrencileri hızlı şekilde silebilir veya puan verebilirsiniz

### 📚 Ders Yönetimi

- Öğretmenler konu başlıkları altında dersler oluşturabilir
- YouTube'dan ders videoları ekleyebilir ve ders açıklamaları yazabilir
- Dersleri silme, düzenleme gibi işlemleri kolayca yapın
- Ders içeriğini zenginleştirme ve güncellemeler

### ✏️ Sınav Yönetimi

- Çoktan seçmeli (A, B, C, D) sınavlar oluşturun
- Her soru için dört seçeneği ve doğru cevabı belirleyin
- Sınavları düzenleyin, silin veya yeni sorular ekleyin
- Sınav adını değiştirirken otomatik dosya yeniden adlandırması
- Mevcut soruları başarıyla editleyebilme

### ⭐ Puanlama Sistemi

- Öğrenci başarısını puanlarla ölçün
- Sınav sonuçlarına göre puanlandırma
- Kümülatif puan takibi

---

## 🔧 Teknik Detaylar

### Backend (Flask)

- Route'lar ile sayfa yönetimi
- Template rendering (Jinja2)
- Form işlemleri
- Dosya yönetimi (JSON işlemleri)

### Database (SQLite)

- İlişkisel veri yapısı
- Foreign key constraints
- Verimli sorgular

### Frontend

- Responsive tasarım
- Modern CSS styling
- JavaScript interaktivitesi
- Kullanıcı dostu arayüz

---

## 🚀 Gelecek Geliştirmeler

- [ ] Kullanıcı kimlik doğrulama (Login/Register)
- [ ] Öğretmen ve öğrenci rolü ayrımı
- [ ] Sınav sonuçlarının detaylı raporlaması
- [ ] Öğrenci ilerlemesinin grafik gösterimi
- [ ] E-posta bildirimleri
- [ ] Mobil uyumlu tasarım iyileştirmeleri
- [ ] REST API endpoints
- [ ] Sınav sonuç analizi ve istatistikleri
- [ ] Öğrenci katılım takibi
- [ ] Sertifika sistemi

---

## 💡 Kullanım İpuçları

1. **Yeni bir sınıf oluşturun** - Öğrencileri organize etmek için
2. **Ders ekleyin** - YouTube linkiyle zengin içerik sağlayın
3. **Öğrenciler ekleyin** - Her öğrenciyi uygun sınıfa atayın
4. **Sınavlar oluşturun** - Öğrenci başarısını değerlendirin
5. **Puanlar verin** - Öğrenci motivasyonunu arttırın

---

## 👨‍💻 Geliştirici Bilgileri

| Bilgi | Açıklama |
|-------|----------|
| **Proje Türü** | Bitirme Projesi |
| **Versiyonu** | 1.0.0 |
| **Lisans** | MIT License |
| **Python Versiyonu** | 3.7+ |
| **Son Güncelleme** | Ocak 2026 |

---

## 📝 Notlar

ElaAdmin, eğitim kurumlarında sınıf yönetimini ve öğrenme sürecini kolaylaştırmak amacıyla geliştirilmiştir. Sistem, öğretmen ve öğrenciler arasında etkileşimi arttırarak, eğitim kalitesini yükseltmek hedeflemektedir.

> **"Eğitim, geleceğin temelini oluşturur. ElaAdmin ile daha iyi bir öğrenme ortamı yaratın."**

---

## 📞 İletişim ve Destek

Herhangi bir soru veya sorun için lütfen iletişime geçiniz.

---

## 📄 Lisans

Bu proje MIT Lisansı altında yayımlanmıştır. Detaylar için LICENSE dosyasına bakınız.

---

**ElaAdmin © 2026 - Tüm hakları saklıdır.**