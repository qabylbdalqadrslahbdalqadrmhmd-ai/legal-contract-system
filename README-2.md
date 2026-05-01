# 🕷️ Spider Library

<div align="center">

![Spider Library](https://img.shields.io/badge/Spider%20Library-v1.0-7c3aed?style=for-the-badge&logo=streamlit)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**مكتبة مشاريع ذكية — ثلاث أدوات، منصة واحدة**

[🚀 تجربة مباشرة](#) · [📖 التوثيق](#-الاستخدام) · [🐛 الإبلاغ عن مشكلة](../../issues)

</div>

---

## 📦 المشاريع المضمنة

| الأداة | الوصف | التقنية |
|--------|-------|---------|
| ⚖️ **محلل العقود** | تحليل شامل للعقود القانونية مع تقييم المخاطر والبنود الناقصة | Google Gemini AI |
| 🤖 **Decision Shadow AI** | نظام تحليل القرارات التجارية باستخدام Machine Learning | Random Forest · Scikit-learn |
| 🕷️ **Spider Hub** | لوحة تحكم مركزية تجمع الأدوات وتعرض الإحصائيات | Streamlit Dashboard |

---

## ⚡ التشغيل السريع

### 1. استنسخ المستودع
```bash
git clone https://github.com/YOUR_USERNAME/spider-library.git
cd spider-library
```

### 2. ثبّت المتطلبات
```bash
pip install -r requirements.txt
```

### 3. شغّل التطبيق
```bash
streamlit run app.py
```

---

## ☁️ النشر على Streamlit Cloud

1. ارفع المشروع على GitHub (هذا المستودع)
2. اذهب إلى [share.streamlit.io](https://share.streamlit.io)
3. اختر **New app** ← اختر المستودع ← الملف `app.py`
4. اضغط **Deploy**

> **ملاحظة:** لاستخدام محلل العقود تحتاج Gemini API Key مجاني من [aistudio.google.com](https://aistudio.google.com)

---

## 🗂️ هيكل المشروع

```
spider-library/
│
├── app.py                  # التطبيق الرئيسي (Spider Library)
├── requirements.txt        # المتطلبات
├── README.md               # هذا الملف
└── .gitignore              # ملفات مستثناة
```

---

## 🛠️ التقنيات المستخدمة

- **[Streamlit](https://streamlit.io/)** — واجهة التطبيق
- **[Google Gemini AI](https://ai.google.dev/)** — تحليل العقود بالذكاء الاصطناعي
- **[Scikit-learn](https://scikit-learn.org/)** — نموذج Random Forest للتنبؤ
- **[PyMuPDF](https://pymupdf.readthedocs.io/)** — استخراج نص PDF
- **[python-docx](https://python-docx.readthedocs.io/)** — قراءة ملفات Word
- **[Plotly](https://plotly.com/)** — الرسوم البيانية التفاعلية

---

## 👩‍💻 إعداد

**الاء** · مشروع Spider Library

---

## 📄 الرخصة

MIT License — استخدم حر مع الإشارة للمصدر.
