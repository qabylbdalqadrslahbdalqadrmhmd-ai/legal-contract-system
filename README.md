import pdfplumber
import google.generativeai as genai

# 1. إعداد الـ API الخاص بـ Gemini
genai.configure(api_key="") 

# 2. وظيفة استخراج النص (حل مشكلة النصوص المقلوبة)
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# 3. وظيفة التحليل القانوني الذكي (الفرق بين القانونين)
def analyze_contract_legally(contract_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # هنا "عقل" التطبيق: نحدد له المعايير القانونية المصرية
    prompt = f"""
    أنت محامٍ خبير في القانون المصري، متخصص في عقود الإيجار.
    قم بتحليل نص عقد الإيجار التالي:
    "{contract_text}"
    
    المطلوب منك:
    1. تحديد هل العقد يخضع لقوانين الإيجار الاستثنائية (القديم) أم للقانون المدني (القانون رقم 4 لسنة 1996 - الجديد) بناءً على تاريخ العقد وشروط الامتداد.
    2. استخراج البيانات الجوهرية (تاريخ تحرير العقد، مدة الإيجار، القيمة الإيجارية، الغرض من الاستخدام).
    3. هل يوجد تعارض مع القانون المصري في أي بند من البنود؟
    4. إذا كان العقد "جديد"، هل صياغته تضمن للمؤجر استرداد العين بانتهاء المدة وفقاً للقانون؟
    
    أجب بصيغة تقرير قانوني واضح.
    """
    
    response = model.generate_content(prompt)
    return response.text

# طريقة الاستخدام في Streamlit:
# uploaded_file = st.file_uploader("ارفع العقد", type="pdf")
# if uploaded_file:
#     text = extract_text_from_pdf(uploaded_file)
#     analysis = analyze_contract_legally(text)
#     st.write(analysis)




