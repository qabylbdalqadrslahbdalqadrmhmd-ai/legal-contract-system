
import streamlit as st
import google.generativeai as genai
import PyPDF2

# Page configuration
st.set_page_config(page_title="LegalTech AI Advisor", layout="wide")

# Sidebar for API Key
st.sidebar.title("إعدادات النظام")
api_key = st.sidebar.text_input("أدخل مفتاح Gemini API", type="password")

# Main Title
st.title("⚖️ المستشار القانوني الذكي")
st.markdown("---")

def extract_text(uploaded_file):
    """Extracts text from the uploaded PDF file."""
    reader = PyPDF2.PdfReader(uploaded_file)
    text_content = ""
    for page in reader.pages:
        text_content += page.extract_text()
    return text_content

def analyze_contract(text, key):
    """Sends the contract text to Gemini for professional legal analysis."""
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro')
    
    # Prompt explicitly commanding Arabic output and specific legal focus
    prompt = f"""
    You are a professional legal expert in Egyptian and International law. Analyze the following contract thoroughly.
    
    Provide the response ONLY in professional Arabic. Your report must include:
    1. A comprehensive summary of the contract.
    2. A clause-by-clause analysis for: Termination, Arbitration, Force Majeure, Indemnity, and Confidentiality.
       - For each: State if it's present, assess its strength/weakness, and provide a legal improvement suggestion if needed.
    3. Professional legal recommendations to protect the parties involved.
    
    Contract text:
    {text}
    """
    
    response = model.generate_content(prompt)
    return response.text

# Main UI Logic
uploaded_file = st.file_uploader("ارفع العقد القانوني (PDF)", type=["pdf"])

if uploaded_file and api_key:
    if st.button("بدء التحليل القانوني الذكي"):
        with st.spinner("جاري تحليل العقد، يرجى الانتظار..."):
            try:
                # Process PDF
                full_text = extract_text(uploaded_file)
                
                # Perform AI Analysis
                analysis_result = analyze_contract(full_text, api_key)
                
                # Display Results
                st.success("تم تحليل العقد بنجاح!")
                st.markdown("### 📝 تقرير التحليل القانوني")
                st.markdown(analysis_result)
                
            except Exception as e:
                st.error(f"حدث خطأ تقني: {e}")
                
elif not api_key:
    st.warning("يرجى إدخال مفتاح الـ API الخاص بـ Gemini في القائمة الجانبية.")

# Footer
st.markdown("---")
st.markdown("تم التطوير بواسطة: المستشار القانوني الرقمي")


برنامج العقود 
