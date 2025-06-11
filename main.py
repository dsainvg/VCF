import streamlit as st
import pandas as pd
import openpyxl
from vcard import gen_vcard

def apply_custom_css():
    st.markdown("""
    <style>
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
    }
    
    /* Title styling */
    .main-title {
        color: #00d4ff;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    
    /* Subtitle styling */
    .subtitle {
        color: #a0a0a0;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    
    /* Section headers */
    .section-header {
        color: #00ff88;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding: 0.5rem 0;
        border-bottom: 2px solid #00ff88;
    }
    
    /* Custom selectbox styling */
    .stSelectbox > div > div {
        background-color: #2d2d44;
        border: 2px solid #444;
        border-radius: 10px;
        cursor: pointer;
    }
    
    .stSelectbox > div > div:hover {
        cursor: pointer;
    }
    
    /* Selectbox dropdown arrow */
    .stSelectbox svg {
        cursor: pointer;
    }
    
    /* File uploader styling */
    .stFileUploader > div {
        background-color: #2d2d44;
        border: 2px dashed #00d4ff;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        cursor: pointer;
    }
    
    .stFileUploader > div:hover {
        cursor: pointer;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #00d4ff, #00ff88);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
        cursor: pointer;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.4);
        cursor: pointer;
    }
    
    /* Download button styling */
    .stDownloadButton > button {
        background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
        cursor: pointer;
    }
    
    .stDownloadButton > button:hover {
        cursor: pointer;
    }
    
    /* Card-like containers */
    .custom-card {
        background: rgba(45, 45, 68, 0.8);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #444;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    /* Column preview styling */
    .column-preview {
        background: rgba(0, 212, 255, 0.1);
        border-left: 4px solid #00d4ff;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 10px 10px 0;
    }
    
    /* Warning and error styling */
    .stAlert {
        border-radius: 10px;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* Number input styling */
    .stNumberInput > div > div > input {
        background-color: #2d2d44;
        color: white;
        border: 2px solid #444;
        border-radius: 8px;
        cursor: pointer;
    }
    
    .stNumberInput > div > div > input:hover {
        cursor: pointer;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: #2d2d44;
        color: white;
        border: 2px solid #444;
        border-radius: 8px;
        cursor: pointer;
    }
    
    .stTextInput > div > div > input:hover {
        cursor: pointer;
    }
    
    /* Checkbox styling */
    .stCheckbox {
        color: #00ff88;
        cursor: pointer;
    }
    
    .stCheckbox > label {
        cursor: pointer;
    }
    
    .stCheckbox > label > div {
        cursor: pointer;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        cursor: pointer;
    }
    
    /* General interactive elements */
    .stSelectbox, .stFileUploader, .stButton, .stDownloadButton, 
    .stNumberInput, .stTextInput, .stCheckbox, .streamlit-expanderHeader {
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_css()
    
    st.markdown('<h1 class="main-title">📱 VCF Generator Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transform your contact data into vCard format with style</p>', unsafe_allow_html=True)
    
    # File type selection section
    st.markdown('<div class="section-header">📁 Select File Type</div>', unsafe_allow_html=True)
    options=["EXCEL File", "CSV File", "TSV File"]
    typeoffile = st.selectbox("Choose your file format", options, help="Select the format of your contact data file")
    
    with st.container():
        if typeoffile == "EXCEL File":
            st.success("📊 Excel file selected - Perfect for structured data!")
        elif typeoffile == "CSV File":
            st.success("📄 CSV file selected - Great for simple comma-separated data!")
        elif typeoffile == "TSV File":
            st.success("📋 TSV file selected - Ideal for tab-separated data!")

    # File upload section
    st.markdown('<div class="section-header">📤 Upload Your File</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Drag and drop your file here", type=["xlsx", "csv", "tsv"])
    
    if uploaded_file is not None:
        if typeoffile == "EXCEL File":
            df = pd.read_excel(uploaded_file)
        elif typeoffile == "CSV File":
            df = pd.read_csv(uploaded_file)
        elif typeoffile == "TSV File":
            df = pd.read_csv(uploaded_file, sep='\t')
        else:
            st.error("Unsupported file type.")
            return
        
        filename = uploaded_file.name.split('.')[0]
        st.success(f"✅ File loaded successfully: **{filename}**")
        
        # Data preview section
        st.markdown('<div class="section-header">👀 Data Preview</div>', unsafe_allow_html=True)
        with st.expander("View your data", expanded=False):
            st.dataframe(df, use_container_width=True)
        # Ask if the vCard is intended for iOS
        is_ios = st.checkbox("Is this vCard for iOS devices?", help="Check if you want to optimize the vCard for iOS compatibility")
        st.session_state["is_ios"] = is_ios
        # Column mapping section
        st.markdown('<div class="section-header">🔗 Column Mapping</div>', unsafe_allow_html=True)
        st.info("Map each column in your data to the appropriate vCard field")
        
        column_names = df.columns.tolist()
        columnoptions = ["NONE","Address", "Name", "Phone Number", "Email","Suffix","Organization", "Job Title","NOTE"]
        
        assign = {}
        ind = 0
        
        for column in column_names:
            ind += 1
            with st.container():
                st.markdown(f'<div class="column-preview"><strong>Column:</strong> {column}</div>', unsafe_allow_html=True)
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    st.write("Sample data:")
                    st.code(str(df[column].iloc[0]) if not df[column].empty else "No data")
                
                with col2:
                    if column in columnoptions:
                        value = column
                        st.success(f"Auto-mapped to: {value}")
                    else:
                        value = st.selectbox(f"Map '{column}' to:", options=columnoptions, key=column)
                    
                    if value == "Phone Number" or value == "Email":
                        typ = st.selectbox(f"Select type for {value}", options=["Mobile" , "Work", "Home"], key=f"{column}_type")
                        value = value + "+" + typ
                
                value = value + str(ind)
                if value != "NONE":
                    assign[value] = column
        
        # Additional fields section
        st.markdown('<div class="section-header">➕ Additional Fields</div>', unsafe_allow_html=True)
        is_there = st.checkbox("Add common fields to all contacts", help="Add fields that will be the same for all contacts")
        ver = 2.1 if st.session_state.get("is_ios", False) else 3.0
        if is_there:
            no_of_such = int(st.number_input("Number of additional fields", key="new_value", min_value=1, max_value=10, step=1))
            
            for i in range(no_of_such):
                ind += 1
                col1, col2 = st.columns(2)
                
                with col1:
                    new_value = st.text_input(f"Value for field {i+1}", key=f"new_value_{i}", placeholder="Enter the value...")
                
                with col2:
                    value = st.selectbox(f"Field type {i+1}", options=columnoptions, key=f"new_value{i}")
                
                value = "!" + value + str(ind)
                if new_value:
                    assign[value] = new_value
        
        # Generation section
        st.markdown('<div class="section-header">🚀 Generate vCard</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            generate_btn = st.button("🎯 Generate vCard", key="generate_vcard", use_container_width=True)
        
        if generate_btn:
            with st.spinner("Generating vCard... Please wait!"):
                vcardtext = ""
                progress_bar = st.progress(0)
                total_rows = len(df)
                
                for index, row in df.iterrows():
                    vcardtext += gen_vcard(row=row, assign=assign, version=ver)
                    progress_bar.progress((index + 1) / total_rows)
                
                st.success(f"✅ Generated vCard for {total_rows} contacts!")
                
                with col2:
                    st.download_button(
                        "📥 Download vCard", 
                        vcardtext, 
                        file_name=f"{filename}.vcf",
                        mime="text/vcard",
                        use_container_width=True
                    )
        
        # Assignment summary
        if assign:
            st.markdown('<div class="section-header">📋 Mapping Summary</div>', unsafe_allow_html=True)
            with st.expander("View column assignments"):
                for column, value in assign.items():
                    st.write(f"**{column}:** {value}")
    
    else:
        st.warning("⚠️ Please upload a file to continue.")
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h3 style="color: #666;">Supported file formats:</h3>
            <p style="color: #888;">📊 Excel (.xlsx) • 📄 CSV (.csv) • 📋 TSV (.tsv)</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()