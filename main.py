import streamlit as st
import pandas as pd
from vcard import gen_vcard
from utils import textedit
from utils import columncheck

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
    
    # File upload section
    st.markdown('<div class="section-header">📤 Upload Your File</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Drag and drop your file here", type=["xlsx", "csv", "tsv"])
    
    # Help section for file upload
    with st.expander("ℹ️ Need help with file upload?", expanded=False):
        st.markdown("""
        ### File Upload Instructions
        
        **Supported file formats:**
        - **Excel (.xlsx)**: Spreadsheets created in Microsoft Excel
        - **CSV (.csv)**: Comma-separated values files
        - **TSV (.tsv)**: Tab-separated values files
        
        **Tips for preparing your file:**
        1. Make sure your file has a header row with column names
        2. Each row should represent one contact
        3. The file should be properly formatted without corruption
        4. Common columns to include: name, phone number, email, address, etc.
        
        **What happens next:**
        After uploading, the app will automatically detect the file type and load your data.
        """)
    
    if uploaded_file is not None:
        # Auto-detect file type based on extension
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        if file_extension == 'xlsx':
            df = pd.read_excel(uploaded_file)
            file_type_message = "📊 Excel file detected - Perfect for structured data!"
        elif file_extension == 'csv':
            df = pd.read_csv(uploaded_file)
            file_type_message = "📄 CSV file detected - Great for simple comma-separated data!"
        elif file_extension == 'tsv':
            df = pd.read_csv(uploaded_file, sep='\t')
            file_type_message = "📋 TSV file detected - Ideal for tab-separated data!"
        else:
            st.error("Unsupported file type.")
            return
        
        st.success(file_type_message)
        
        df = df.dropna(axis=1, how='all')  # Remove empty columns
        df = df.reset_index(drop=True)  # Reset index after dropping columns
        df = df.dropna(how='all')  # Remove rows that are completely empty
            
        filename = uploaded_file.name.split('.')[0]
        st.success(f"✅ File loaded successfully: **{filename}**")
        
        # After file is processed and before data preview
        # Ask if the vCard is intended for iOS
        st.markdown('<div class="section-header">⚙️ vCard Settings</div>', unsafe_allow_html=True)
        is_ios = st.checkbox("Is this vCard for iOS devices?", help="Check if you want to optimize the vCard for iOS compatibility")
        st.session_state["is_ios"] = is_ios
        
        # Help section for iOS setting
        with st.expander("ℹ️ Need help with vCard settings?", expanded=False):
            st.markdown("""
            ### vCard Settings Instructions
            
            **iOS Compatibility:**
            - If checked, the app will generate vCards in version 2.1 format, which is more compatible with iOS devices
            - If unchecked, the app will use the newer vCard 3.0 format
            
            **When to check this option:**
            - If you plan to import contacts to an iPhone or iPad
            - If you've had issues with vCards not importing correctly on Apple devices
            - If you're unsure which recipients will be using the vCard files
            
            **Note:** Most modern devices support both formats, but iOS sometimes handles vCard 2.1 better for certain fields.
            """)
        
        # Data preview section
        st.markdown('<div class="section-header">👀 Data Preview</div>', unsafe_allow_html=True)
        with st.expander("View your data", expanded=False):
            st.dataframe(df, use_container_width=True)
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
                    value = columncheck(column)
                    if value:
                        st.success(f"Auto-mapped to: {value}")
                        st.info(f"Auto-mapped to: {value}. You can change this if needed.")
                        value = st.selectbox(f"Map '{column}' to:", options=columnoptions, index=columnoptions.index(value) if value in columnoptions else 0, key=column)
                    else:
                        value = st.selectbox(f"Map '{column}' to:", options=columnoptions, key=column)
                    
                    if value == "Phone Number" or value == "Email":
                        typ = st.selectbox(f"Select type for {value}", options=["Mobile" , "Work", "Home"], key=f"{column}_type")
                        value = value + "+" + typ
                
                value = value + str(ind)
                if value != "NONE":
                    assign[value] = column
        
        # Help section for column mapping
        with st.expander("ℹ️ Need help with column mapping?", expanded=False):
            st.markdown("""
            ### Column Mapping Instructions
            
            **What is this step for?**  
            This step connects your spreadsheet columns to the correct contact fields in the vCard format.
            
            **How to use:**
            1. For each column in your data, select the appropriate vCard field from the dropdown
            2. If a column doesn't contain contact information, select "NONE"
            3. For Phone Numbers and Email addresses, specify the type (Mobile, Work, or Home)
            4. The app will try to automatically map columns based on their names
            
            **Field descriptions:**
            - **Name**: Person's name (first, last, or full name)
            - **Address**: Physical address information
            - **Phone Number**: Telephone numbers (requires specifying type)
            - **Email**: Email addresses (requires specifying type)
            - **Suffix**: Name suffixes like Jr., Sr., MD, PhD
            - **Organization**: Company or organization name
            - **Job Title**: Position or role within organization
            - **NOTE**: Additional notes or comments about the contact
            """)
        
        # Additional fields section
        st.markdown('<div class="section-header">➕ Additional Fields</div>', unsafe_allow_html=True)
        is_there = st.checkbox("Add common fields to all contacts", help="Add fields that will be the same for all contacts")
        
        # Help section for additional fields
        with st.expander("ℹ️ Need help with additional fields?", expanded=False):
            st.markdown("""
            ### Additional Fields Instructions
            
            **What is this step for?**  
            This allows you to add information that should appear in ALL contacts in your vCard file.
            
            **When to use:**
            - Add your company name to all contacts
            - Add a department or division to all contacts
            - Add standard notes to all contacts
            
            **How to use:**
            1. Check the box to enable additional fields
            2. Specify how many fields you want to add
            3. For each field, enter the value and select the field type
            4. These values will be added to EVERY contact in the final vCard
            """)
        
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
        
        # Help section for vCard generation
        with st.expander("ℹ️ Need help with vCard generation?", expanded=False):
            st.markdown("""
            ### vCard Generation Instructions
            
            **What happens during generation:**
            1. The app processes each row in your data
            2. It maps the columns to the appropriate vCard fields based on your selections
            3. It creates a vCard record for each contact
            4. All vCards are combined into a single .vcf file
            
            **After generation:**
            - You'll see a success message with the number of contacts processed
            - A download button will appear to save the .vcf file
            - You can import this file into most contact applications and smartphones
            
            **Importing tips:**
            - On iOS: Email the .vcf file to yourself and open it on your device
            - On Android: Copy the file to your device and open it with your contacts app
            - On desktop: Most email clients can import .vcf files directly
            """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            generate_btn = st.button("🎯 Generate vCard", key="generate_vcard", use_container_width=True)
        
        # Help section for vCard generation
        with st.expander("ℹ️ Need help with vCard generation?", expanded=False):
            st.markdown("""
            ### vCard Generation Instructions
            
            **What happens during generation:**
            1. The app processes each row in your data
            2. It maps the columns to the appropriate vCard fields based on your selections
            3. It creates a vCard record for each contact
            4. All vCards are combined into a single .vcf file
            
            **After generation:**
            - You'll see a success message with the number of contacts processed
            - A download button will appear to save the .vcf file
            - You can import this file into most contact applications and smartphones
            
            **Importing tips:**
            - On iOS: Email the .vcf file to yourself and open it on your device
            - On Android: Copy the file to your device and open it with your contacts app
            - On desktop: Most email clients can import .vcf files directly
            """)
        
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
                    if column != "NONE":
                        st.write(f"**{textedit(column)}:** {textedit(value)}")

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