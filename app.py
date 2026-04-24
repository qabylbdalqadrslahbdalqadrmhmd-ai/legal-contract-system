import streamlit as st
import PyPDF2

def main():
    # Page Configuration
    st.set_page_config(page_title="Contract Analysis System", layout="wide")
    
    st.title("⚖️ Contract Analysis Dashboard")
    st.write("Upload a contract (PDF) to analyze clauses and extract information.")

    # File Uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        try:
            # Process PDF
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            st.success("File processed successfully!")

            # Clause Detection Logic
            st.subheader("Clause Detection Status")
            keywords = ["Termination", "Indemnity", "Arbitration", "Confidentiality", "Force Majeure"]
            
            # Create two columns for display
            col1, col2 = st.columns(2)
            
            for i, word in enumerate(keywords):
                found = word.lower() in text.lower()
                if i % 2 == 0:
                    with col1:
                        if found: st.success(f"Found: {word}")
                        else: st.error(f"Missing: {word}")
                else:
                    with col2:
                        if found: st.success(f"Found: {word}")
                        else: st.error(f"Missing: {word}")

            # Expandable text view
            with st.expander("View Full Extracted Text"):
                st.text(text)

        except Exception as e:
            st.error(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    main()
