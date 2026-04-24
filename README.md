streamlit
google-generativeai
PyPDF2
 import streamlit as st
import google.generativeai as genai
import PyPDF2

# 1. إعداد الصفحة (العنوان واللغة)
st.set_page_config(page_title="محلل العقود الذكي", layout="centered")

# 2. التنسيق العربي (RTL)
st.markdown("""
    <style>
        .stApp { direction: rtl; text-align: right; }
        .stButton>button { width: 100%; border-radius: 10px; background-color: #2e7d32; color: white; font-weight: bold; }
        h1, h2, h3 { color: #1a237e; }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان والترحيب
st.title("⚖️ محلل العقود الذكي")
st.subheader("لوحة تحكم قانونية مدعومة بالذكاء الاصطناعي")
st.write("قم برفع العقد (PDF) وسيقوم النظام باستخراج الأطراف، البنود، والمخاطر فوراً.")

# 4. تأمين الاتصال بـ Gemini
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("⚠️ خطأ في الاتصال: تأكد من إضافة مفتاح GOOGLE_API_KEY في إعدادات Streamlit.")
    st.stop()

# 5. رفع الملف
uploaded_file = st.file_uploader("📂 اسحب ملف العقد أو اختره هنا", type=["pdf"])

if uploaded_file is not None:
    # قراءة الملف
    with st.spinner("جاري معالجة الملف..."):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    
    st.success("تم رفع الملف بنجاح!")
    
    # 6. زر التحليل
    if st.button("بدء التحليل القانوني الآن"):
        with st.spinner("جاري التحليل بواسطة الذكاء الاصطناعي..."):
            
            prompt = f"""
            أنت خبير قانوني ومحامي محترف. قم بتحليل العقد التالي واستخرج البيانات التالية بدقة:
            1. الأطراف المتعاقدة.
            2. البنود الجوهرية (التزامات وحقوق).
            3. المخاطر القانونية المحتملة في العقد.
            4. التوصيات القانونية (بماذا تنصح الطرف الذي يراجع العقد).
            
            نص العقد:
            {text[:15000]}
            
            يرجى الإجابة باللغة العربية بأسلوب قانوني منظم ومرتب.
            """
            
            try:
                response = model.generate_content(prompt)
                st.subheader("📝 تقرير التحليل القانوني:")
                st.write(response.text)
            except Exception as e:
                st.error("حدث خطأ أثناء التحليل، يرجى المحاولة مرة أخرى.")

