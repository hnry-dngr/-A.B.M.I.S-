# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:40:50 2024

@author: HNRYDNGR
"""

# import streamlit as st
# import pandas as pd
# import base64
# from io import BytesIO
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import os

# # Function to encode the image to base64
# def get_base64_image(image_path):
#     """Convert image to base64 format."""
#     with open(image_path, "rb") as img_file:
#         b64_string = base64.b64encode(img_file.read()).decode()
#     return b64_string

# # Function to set the background image and text styles
# def set_background_image(image_path):
#     """Set a background image using base64 encoding and style text elements."""
#     b64_image = get_base64_image(image_path)
#     page_bg_img = f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{b64_image}");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     h1, h2, h3, h4, h5, h6 {{
#         color: black !important;
#     }}
#     .stMarkdown p {{
#         color: black !important;
#     }}
#     </style>
#     """
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# # Function to style the sidebar
# def style_sidebar():
#     """Add custom styling to the sidebar menu."""
#     sidebar_style = """
#     <style>
#     [data-testid="stSidebar"] {{
#         background-color: #87CEEB;  /* Set the sidebar background color */
#     }}
#     [data-testid="stSidebar"] .css-1d391kg {{
#         color: white;  /* Set the sidebar text color */
#     }}
#     [data-testid="stSidebar"] .css-1d391kg button {{
#         background-color: #ffffff;  /* Set the button background color */
#         color: #87CEEB;  /* Set the button text color */
#     }}
#     </style>
#     """
#     st.markdown(sidebar_style, unsafe_allow_html=True)

# # Function to check user credentials
# USER_CREDENTIALS = {
#     "kosi": {"password": "henry123", "state": "delta", "local_gov": "oshimili north"},
#     "henry": {"password": "henry321", "state": "edo", "local_gov": "oshimili north"}
# }

# def check_credentials(username, password):
#     """Check if the entered username and password match the stored credentials."""
#     user = USER_CREDENTIALS.get(username)
#     if user and user.get('password') == password:  # Correctly checks the password now
#         return True
#     return False


# # Function to create a downloadable Excel file
# def to_excel(df):
#     output = BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')
#     df.to_excel(writer, index=False, sheet_name='Sheet1')
#     writer.save()
#     processed_data = output.getvalue()
#     return processed_data

# # Function to create a downloadable PDF file
# def to_pdf(df):
#     output = BytesIO()
#     p = canvas.Canvas(output, pagesize=letter)
#     p.drawString(100, 750, "Data Export")
    
#     for i, row in enumerate(df.itertuples()):
#         p.drawString(100, 730 - i * 20, f"{row}")
    
#     p.save()
#     pdf_data = output.getvalue()
#     return pdf_data

# # Function to download file as Excel or PDF
# def download_file(df, format):
#     if format == "Excel":
#         file = to_excel(df)
#         b64 = base64.b64encode(file).decode()
#         href = f'<a href="data:application/octet-stream;base64,{b64}" download="data.xlsx">Download Excel File</a>'
#         st.markdown(href, unsafe_allow_html=True)
#     elif format == "PDF":
#         file = to_pdf(df)
#         b64 = base64.b64encode(file).decode()
#         href = f'<a href="data:application/octet-stream;base64,{b64}" download="data.pdf">Download PDF File</a>'
#         st.markdown(href, unsafe_allow_html=True)



# def initialize_data():
#     """Initialize or load data from CSV files into session state."""
#     data = "C:/Users/HP/Desktop/PROJECT1 DEMO/csv_data"  # Provide the directory path where your CSV files are stored
    
#     data_dict = {
#         'INDEPENDENT REVENUE (12000000)': 'INDEPENDENT_REVENUE_12000000.csv',
#         'TAX REVENUE (12010000)': 'TAX_REVENUE_12010000.csv',
#         'PERSONAL TAXES (12010100)': 'PERSONAL_TAXES_12010100.csv',
#         'NON-TAX REVENUE (12020000)': 'NON-TAX_REVENUE_12020000.csv',
#         'LICENSE GENERAL (120201)': 'LICENSE_GENERAL_120201.csv',
#         'FEES GENERAL (120204)': 'FEES_GENERAL_120204.csv',
#         'FINES GENERAL (120205)': 'FINES_GENERAL_.csv',
#     }

#     for key, file_name in data_dict.items():
#         file_path = os.path.join(data, file_name)
#         if os.path.exists(file_path):
#             df = pd.read_csv(file_path)
            
#             # Store the DataFrame in session state
#             st.session_state[key] = df
#         else:
#             st.warning(f"File {file_path} not found.")

# # Function to add a record to a DataFrame in session state and overwrite the CSV
# def add_record(df_key, record, csv_file):
#     """Add a record to the selected DataFrame in session state and overwrite the CSV."""
#     if not all(record.values()):
#         st.error("All fields must be filled out!")
#     else:
#         # Append the new record to the DataFrame in session state
#         df = st.session_state[df_key]
#         df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)

#         # Save the updated DataFrame to the CSV file (overwrite the file)
#         df.to_csv(csv_file, index=False)
#         st.session_state[df_key] = df  # Update session state with the new DataFrame
#         st.success(f"Record added successfully to {csv_file}!")
        
#         # Reload the data to immediately reflect changes
#         initialize_data()  # Reinitialize data after adding a record to refresh view




#  # Function to delete a record from a DataFrame in session state
# def delete_record(df_key, index):
#      """Delete a record from the selected DataFrame in session state."""
#      if 0 <= index < len(st.session_state[df_key]):
#          st.session_state[df_key] = st.session_state[df_key].drop(index).reset_index(drop=True)
#      else:
#          st.error("Index out of range.")

#  # Function to add a new user (Sign Up)
# def add_user(username, password, state, local_gov):
#      """Add a new user to the USER_CREDENTIALS dictionary."""
#      if username in USER_CREDENTIALS:
#          st.error("Username already exists. Please choose another one.")
#      else:
#          USER_CREDENTIALS[username] = {"password": password, "state": state, "local_gov": local_gov}
#          st.success("User registered successfully. You can now log in.")

#  # Main function to run the Streamlit app
# def main():
#     # Initialize session state for 'logged_in'
#     if 'logged_in' not in st.session_state:
#         st.session_state['logged_in'] = False
#     if 'username' not in st.session_state:
#         st.session_state['username'] = ""
#     if 'state' not in st.session_state:
#         st.session_state['state'] = ""
#     if 'local_gov' not in st.session_state:
#         st.session_state['local_gov'] = ""

#     # Set background image based on login status
#     if st.session_state['logged_in']:
#         # Use a different background image when logged in
#         set_background_image("C:/Users/HP/Desktop/PROJECT1 DEMO/LOGIN BACKGROUND.jpg")
#     else:
#         # Default background image
#         set_background_image("C:/Users/HP/Desktop/PROJECT1 DEMO/BACKGROUND.webp")

#     # Style the sidebar
#     style_sidebar()

#     # Title with a sky-blue tab-like base
#     st.markdown('<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><h1>AUTOMATED BUDGET MANAGEMENT AND INFORMATION SERVICES (A.B.M.I.S)</h1></div>', unsafe_allow_html=True)

#     # Sidebar Menu for Login and Sign Up
#     menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])

#     if menu == "Login":
#         if st.session_state['logged_in']:
#             # Welcome the user
#             st.markdown(f'<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><p>Welcome, {st.session_state["username"]}!</p><p>State: {st.session_state["state"]}, Local Government: {st.session_state["local_gov"]}</p></div>', unsafe_allow_html=True)

#             # Initialize DataFrames
#             initialize_data()

#             # Dashboard Menu
#             dashboard_menu = st.sidebar.selectbox("Dashboard", ["Home", "View Data", "Add Information", "Delete Record", "Download", "Logout"])
            

#             if dashboard_menu == "Home":
#                  st.markdown('<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><h2>Home - A.B.M.I.S</h2><p>Use the menu to navigate through different operations.</p></div>', unsafe_allow_html=True)

#             elif dashboard_menu == "View Data":
#                 # Select a DataFrame to view
#                 df_key = st.selectbox("Select DataFrame", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
#                 df = st.session_state.get(df_key, pd.DataFrame())  # Ensure it's a DataFrame
#                 if isinstance(df, pd.DataFrame):
#                     st.markdown(f'<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><h2>Viewing: {df_key}</h2></div>', unsafe_allow_html=True)
#                     st.dataframe(df)
#                 else:
#                     st.error("Selected item is not a DataFrame.")

#             elif dashboard_menu == "Add Information":
#                 # Select a DataFrame to add a record
#                 df_key = st.selectbox("Select DataFrame", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
#                 df = st.session_state[df_key]
            
#                 # Assuming the CSV file name matches the DataFrame key for simplicity
#                 csv_file = f"{df_key.replace(' ', '_').replace('(', '').replace(')', '')}.csv"
            
#                 # Create input fields for each column in the selected DataFrame
#                 new_record = {}
#                 for col in df.columns:
#                     if "BUDGET" in col or "TOTAL" in col or "ACTUAL" in col:
#                         new_record[col] = st.number_input(f"Enter {col}", key=f"{col}_add_{df_key}")
#                     else:
#                         new_record[col] = st.text_input(f"Enter {col}", key=f"{col}_add_{df_key}")
            
#                 # Add the record when the button is clicked
#                 if st.button("Add Record"):
#                     add_record(df_key, new_record, csv_file)
                
#             elif dashboard_menu == "Download":
#                  # Select a DataFrame to download
#                  df_key = st.selectbox("Select DataFrame to Download", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
#                  df = st.session_state.get(df_key, pd.DataFrame())
                 
#                  if isinstance(df, pd.DataFrame):
#                      # Choose download format
#                      format_choice = st.radio("Choose the format to download:", ("Excel", "PDF"))
                     
#                      # Download button
#                      if st.button("Download"):
#                          download_file(df, format_choice)



#             elif dashboard_menu == "Delete Record":
#                 # Select a DataFrame to delete a record
#                 df_key = st.selectbox("SELECT FROM TABLES", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
#                 df = st.session_state[df_key]
#                 index_to_delete = st.number_input("Enter index to delete", min_value=0, max_value=len(df)-1, step=1)
#                 if st.button("Delete Record"):
#                     delete_record(df_key, index_to_delete)
#                     st.success(f"Record at index {index_to_delete} deleted successfully.")

#             elif dashboard_menu == "Logout":
#                 # Logout user
#                 st.session_state['logged_in'] = False
#                 st.rerun()
    
#         else:
#             # Login form
#             with st.sidebar:
#                 st.subheader("Login")
#                 username = st.text_input("Username")
#                 password = st.text_input("Password", type="password")
#                 if st.button("Login"):
#                     if check_credentials(username, password):
#                         # Set session state for logged-in user
#                         st.session_state['logged_in'] = True
#                         st.session_state['username'] = username
#                         st.session_state['state'] = USER_CREDENTIALS[username]['state']
#                         st.session_state['local_gov'] = USER_CREDENTIALS[username]['local_gov']
#                         st.rerun()
#                     else:
#                         st.error("Incorrect username or password.")
    
#     elif menu == "Sign Up":
#         # Sign-up form
#         with st.sidebar:
#             st.subheader("Sign Up")
#             new_username = st.text_input("Enter a new username")
#             new_password = st.text_input("Enter a new password", type="password")
#             new_state = st.text_input("Enter your State")
#             new_local_gov = st.text_input("Enter your Local Government Area")
#             if st.button("Sign Up"):
#                 if new_username and new_password and new_state and new_local_gov:
#                     add_user(new_username, new_password, new_state, new_local_gov)
#                 else:
#                     st.error("Please fill in all fields to sign up.")
    
#      # Run the Streamlit app
# if __name__ == "__main__":
#     main()









import streamlit as st
import pandas as pd
import base64
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# Function to encode the image to base64
def get_base64_image(image_path):
    """Convert image to base64 format."""
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return b64_string

# Function to set the background image and text styles
def set_background_image(image_path):
    """Set a background image using base64 encoding and style text elements."""
    b64_image = get_base64_image(image_path)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{b64_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: black !important;
    }}
    .stMarkdown p {{
        color: black !important;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to style the sidebar
def style_sidebar():
    """Add custom styling to the sidebar menu."""
    sidebar_style = """
    <style>
    [data-testid="stSidebar"] {{
        background-color: #87CEEB;  /* Set the sidebar background color */
    }}
    [data-testid="stSidebar"] .css-1d391kg {{
        color: white;  /* Set the sidebar text color */
    }}
    [data-testid="stSidebar"] .css-1d391kg button {{
        background-color: #ffffff;  /* Set the button background color */
        color: #87CEEB;  /* Set the button text color */
    }}
    </style>
    """
    st.markdown(sidebar_style, unsafe_allow_html=True)

# Function to check user credentials
USER_CREDENTIALS = {
    "Itoje": {"password": "itoje123", "state": "DELTA", "local_gov": "OSHIMILI NORTH"},
    "Henry": {"password": "henry321", "state": "DELTA", "local_gov": "OSHIMILI NORTH"}
}

# Function to download the consolidated budget summary as Excel
def download_consolidated_summary():
    summary_df, revenue_source_df = create_consolidated_budget_summary()

    # Convert the summary to Excel format
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        summary_df.to_excel(writer, sheet_name='Consolidated Budget Summary', index=False)
        revenue_source_df.to_excel(writer, sheet_name='Revenue Source Summary', index=False)
    writer.save()
    output.seek(0)

    # Encode the Excel file for download
    b64 = base64.b64encode(output.read()).decode()

    # Provide a download link for the user
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="consolidated_budget_summary.xlsx">Download Consolidated Budget Summary</a>'
    st.markdown(href, unsafe_allow_html=True)



# Function to summarize all tables in the session state
def display_all_tables_summary():
    """Display a summary of all DataFrames stored in session state."""
    
    # Iterate over all items in session state
    for df_key, df in st.session_state.items():
        # Check if the item is a DataFrame
        if isinstance(df, pd.DataFrame):
            st.markdown(f"### Table: {df_key}")
            st.markdown(f"**Shape**: {df.shape[0]} rows × {df.shape[1]} columns")
            
            # Optionally display a preview of the first few rows (head of the DataFrame)
            st.dataframe(df.head())  # Show first 5 rows for a preview
            
            # Optional: Add space between tables
            st.markdown("---")  # Separator between tables


# Function to calculate totals for specific numeric columns in a DataFrame
def calculate_totals_for_df(df, columns_to_sum):
    """Return a Series of totals for the specified numeric columns in the DataFrame."""
    totals = {}
    for col in columns_to_sum:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            totals[col] = df[col].sum()
    return pd.Series(totals)




def check_credentials(username, password):
    """Check if the entered username and password match the stored credentials."""
    user = USER_CREDENTIALS.get(username)
    if user and user.get('password') == password:  # Correctly checks the password now
        return True
    return False

# Function to calculate totals for numeric columns and append a 'Total' row
def add_totals_row(df, columns_to_sum):
    """Append a 'Total' row at the bottom of the DataFrame for specific numeric columns."""
    
    # Convert only the specified columns to numeric, handling errors
    for col in columns_to_sum:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, replacing non-numeric values with NaN
            df[col] = df[col].fillna(0)  # Replace NaN with 0 for summing purposes

    # Create a dictionary for the total row
    total_row = {}

    # Iterate over the columns in the DataFrame
    for col in df.columns:
        if col in columns_to_sum:  # Only sum specific numeric columns
            total_row[col] = df[col].sum()  # Calculate sum for specified numeric columns
        else:
            total_row[col] = 'Total' if col == 'DESCRIPTION' else ''  # Label non-numeric or non-summed columns with 'Total' or keep blank

    # Append the total row to the DataFrame
    df_with_total = df.append(total_row, ignore_index=True)

    return df_with_total







def display_all_tables_summary_with_download():
    """Display all tables summary and offer download as Excel."""
    st.markdown("### Summary of All Tables")

    # Display each table summary
    for df_key, df in st.session_state.items():
        if isinstance(df, pd.DataFrame):
            st.markdown(f"### Table: {df_key}")
            st.markdown(f"**Shape**: {df.shape[0]} rows × {df.shape[1]} columns")
            st.dataframe(df.head())  # Show first 5 rows for a preview
            st.markdown("---")

    # Add buttons to download the summary as an Excel file
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Download All Tables as Excel", key="download_all_tables"):
            download_excel_summary()  # Existing function to download all tables
    with col2:
        if st.button("Download Consolidated Budget Summary", key="download_consolidated_summary"):
            download_consolidated_summary()


# Function to create the consolidated budget summary DataFrame
def create_consolidated_budget_summary():
    summary_list = []

    # Loop through each item in session state
    for df_key, df in st.session_state.items():
        if isinstance(df, pd.DataFrame):
            # Identify department DataFrames by their keys or a specific attribute
            if any(keyword in df_key for keyword in ['Department', 'Office', 'Audit']):
                # Calculate totals for the department
                total_staff = df.get('NO. OF STAFF', pd.Series([0])).sum()
                budget_2024_total = df.get('BUDGET 2024', pd.Series([0])).sum()
                budget_2025_total = df.get('BUDGET 2025', pd.Series([0])).sum()
                budget_2026_total = df.get('BUDGET 2026', pd.Series([0])).sum()
                total_three_years = df.get('TOTAL THREE YEARS', pd.Series([0])).sum()
                actual_2023_total = df.get('ACTUAL 2023', pd.Series([0])).sum()
                budget_2023_total = df.get('BUDGET 2023', pd.Series([0])).sum()

                # Create a summary row for the department
                summary_list.append({
                    'CODE': df_key,
                    'DESCRIPTION OF EXPENDITURE': df_key,
                    'NO. OF STAFF': total_staff,
                    'BUDGET 2024': budget_2024_total,
                    'BUDGET 2025': budget_2025_total,
                    'BUDGET 2026': budget_2026_total,
                    'TOTAL THREE YEARS': total_three_years,
                    'ACTUAL 2023': actual_2023_total,
                    'BUDGET 2023': budget_2023_total
                })

    # Create a DataFrame from the summary
    summary_df = pd.DataFrame(summary_list)

    # Calculate grand totals
    grand_total_row = {
        'CODE': 'GRAND TOTAL',
        'DESCRIPTION OF EXPENDITURE': '',
        'NO. OF STAFF': summary_df['NO. OF STAFF'].sum(),
        'BUDGET 2024': summary_df['BUDGET 2024'].sum(),
        'BUDGET 2025': summary_df['BUDGET 2025'].sum(),
        'BUDGET 2026': summary_df['BUDGET 2026'].sum(),
        'TOTAL THREE YEARS': summary_df['TOTAL THREE YEARS'].sum(),
        'ACTUAL 2023': summary_df['ACTUAL 2023'].sum(),
        'BUDGET 2023': summary_df['BUDGET 2023'].sum()
    }

    # Append the grand total row
    summary_df = summary_df.append(grand_total_row, ignore_index=True)

    return summary_df

# Function to create the Excel file with the two DataFrames
def create_excel_summary():
    summary_df, revenue_source_df = create_consolidated_budget_summary()

    # Create a BytesIO buffer to hold the Excel file in memory
    output = BytesIO()
    
    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        workbook = writer.book

        # Write the consolidated budget summary to one sheet
        worksheet1 = workbook.add_worksheet('Consolidated Budget Summary')
        writer.sheets['Consolidated Budget Summary'] = worksheet1

        # Add a title at the top
        worksheet1.write('A1', 'CONSOLIDATED BUDGET SUMMARY')
        summary_df.to_excel(writer, sheet_name='Consolidated Budget Summary', startrow=2, index=False)

        # Write the revenue source summary to another sheet
        worksheet2 = workbook.add_worksheet('Revenue Source Summary')
        writer.sheets['Revenue Source Summary'] = worksheet2

        # Add a title for Revenue Source section
        worksheet2.write('A1', 'REVENUE SOURCE SUMMARY')
        revenue_source_df.to_excel(writer, sheet_name='Revenue Source Summary', startrow=2, index=False)

        # Set column widths for readability
        for sheet in ['Consolidated Budget Summary', 'Revenue Source Summary']:
            worksheet = writer.sheets[sheet]
            worksheet.set_column('A:A', 30)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:H', 20)

    # Save the Excel file to the BytesIO buffer
    writer.save()

    # Get the contents of the BytesIO buffer (the Excel file)
    output.seek(0)  # Reset the buffer position to the start
    return output

# Function to generate the consolidated and revenue tables and allow download
def download_excel_summary():
    summary_df = create_consolidated_budget_summary()

    # Independent Revenue example (replace with your real data)
    revenue_df = pd.DataFrame({
        'DESCRIPTION': ['NON-TAX REVENUE (12020000)', 'TAX REVENUE (12010000)'],
        'BUDGET 2024': [4500, 1000],
        'BUDGET 2025': [4725, 1050],
        'BUDGET 2026': [4961.25, 1102.5],
        'TOTAL THREE YEARS': [14186.25, 3152.5],
        'ACTUAL 2023': [4100, 900],
        'BUDGET 2023': [4285.714286, 952.3809524]
    })

    # Generate the Excel file with the consolidated budget and revenue tables
    excel_file = format_excel_output(summary_df, revenue_df)

    # Create download link for Excel file
    b64 = base64.b64encode(excel_file.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="consolidated_budget_summary.xlsx">Download Consolidated Budget Summary</a>'
    st.markdown(href, unsafe_allow_html=True)




# Function to format the Excel output with headers and merged cells
def format_excel_output(summary_df, revenue_df):
    output = io.BytesIO()

    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        # Write the consolidated budget summary DataFrame
        workbook = writer.book

        # Add formatting for merged title cells
        merge_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 14
        })

        # Write the consolidated summary
        summary_df.to_excel(writer, sheet_name='Consolidated Summary', startrow=3, index=False)
        worksheet = writer.sheets['Consolidated Summary']

        # Merge cells for the title and set the title
        worksheet.merge_range('A1:I1', 'CONSOLIDATED BUDGET SUMMARY', merge_format)

        # Add the Independent Revenue part
        revenue_df.to_excel(writer, sheet_name='Consolidated Summary', startrow=summary_df.shape[0] + 6, index=False)
        worksheet.merge_range(f'A{summary_df.shape[0] + 5}:I{summary_df.shape[0] + 5}', 'INDEPENDENT REVENUE (12000000)', merge_format)

    output.seek(0)
    return output


# Function to create a downloadable Excel file
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

# Function to create a downloadable PDF file
def to_pdf(df):
    output = BytesIO()
    p = canvas.Canvas(output, pagesize=letter)
    p.drawString(100, 750, "Data Export")
    
    for i, row in enumerate(df.itertuples()):
        p.drawString(100, 730 - i * 20, f"{row}")
    
    p.save()
    pdf_data = output.getvalue()
    return pdf_data

# Function to download file as Excel or PDF
def download_file(df, format):
    if format == "Excel":
        file = to_excel(df)
        b64 = base64.b64encode(file).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="data.xlsx">Download Excel File</a>'
        st.markdown(href, unsafe_allow_html=True)
    elif format == "PDF":
        file = to_pdf(df)
        b64 = base64.b64encode(file).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="data.pdf">Download PDF File</a>'
        st.markdown(href, unsafe_allow_html=True)



# Function to initialize DataFrames and load them into session state
def initialize_data():
    """Initialize or load data into session state if not already loaded."""
    data_dict = {
        'INDEPENDENT REVENUE (12000000)': pd.DataFrame({
            'ECONOMIC_CODE': ['12010000', '12020000'],
            'RS_CODE': ['12000000', '12000000'],
            'DESCRIPTION': ['TAX REVENUE', 'NON-TAX REVENUE'],
            'BUDGET 2024': [1000, 2000],
            'BUDGET 2025': [1050, 2100],
            'BUDGET 2026': [1102.50, 2205],
            'TOTAL THREE YEARS': [3152.50, 6305],
            'ACTUAL 2023': [900, 1800],
            'BUDGET 2023': [952.38, 1904.76]
            }),
        
        'TAX REVENUE (12010000)': pd.DataFrame({
            'ECONOMIC_CODE': ['12010100'],
            'IR_CODE': ['12010000'],
            'DESCRIPTION': ['PERSONAL TAXES'],
            'BUDGET 2024': [1000],
            'BUDGET 2025': [1050],
            'BUDGET 2026': [1102.50],
            'TOTAL THREE YEARS': [3152.50],
            'ACTUAL 2023': [900],
            'BUDGET 2023': [952.38]
            }),
        
        "PERSONAL TAXES (12010100)": pd.DataFrame({
            'ECONOMIC_CODE': ['12010101', '12010104', '12010105'],
            'TR_CODE': ['12010000', '12010000', '12010000'],
            'DESCRIPTION': ['COMMUNITY DEVELOPMENT / POLL TAX', 'ARREAR OF COMMUNITY POLL TAX','CATTLE TAX'],
            'BUDGET 2024': [1000, 2000, 1500],
            'BUDGET 2025': [1050, 2100, 1575],
            'BUDGET 2026': [1102.50, 2205, 1653.75],
            'TOTAL THREE YEARS': [3152.50, 6305, 4728.75],
            'ACTUAL 2023': [900, 1800, 1400],
            'BUDGET 2023': [952.38, 1904.76, 1428.57]
            }),
        
        'NON-TAX REVENUE (12020000)': pd.DataFrame({
            'ECONOMIC_CODE': ['120201', '120204', '120205'],
            'IR_CODE': ['12020000', '12020000', '12020000'],
            'DESCRIPTION': ['LICENSE GENERAL', 'FEES GENERAL', 'FINES GENERAL'],
            'BUDGET 2024': [1000, 2000, 1500],
            'BUDGET 2025': [1050, 2100, 1575],
            'BUDGET 2026': [1102.50, 2205, 1653.75],
            'TOTAL THREE YEARS': [3152.50, 6305, 4728.75],
            'ACTUAL 2023': [900, 1800, 1400],
            'BUDGET 2023': [952.38, 1904.76, 1428.57]
            }),
        
        "LICENSE GENERAL (120201)": pd.DataFrame({
            'ECONOMIC_CODE': ['12020102', '12020105', '12020107'],
            'N.TR_CODE': ['12020000', '12020000', '12020000'],  # This list length is correct (78 elements)
            'DESCRIPTION': ['GOLDSMITHS & GOLD DEALERS LICENSE', 'RADIO /TELEVISION STATION LICENSES', 'BOATS & CANOE (SMALL CRAFT) LICENSES'],
            'BUDGET 2024': [1000, 2000, 1500],
            'BUDGET 2025': [1050, 2100, 1575],
            'BUDGET 2026': [1102.50, 2205, 1653.75],
            'TOTAL THREE YEARS': [3152.50, 6305, 4728.75],
            'ACTUAL 2023': [900, 1800, 1400],
            'BUDGET 2023': [952.38, 1904.76, 1428.57]
            }),

        "FEES GENERAL (120204)": pd.DataFrame({
            'ECONOMIC_CODE': ['12020404', '12020417', '12020418'],
            'N.TR_CODE': ['12020000', '12020000', '12020000'],
            'DESCRIPTION': ['TRADE UNION FEES', 'CONTRACTOR REGISTRATION FEES', 'MARRIAGE / DIVORCE FEES'],
            'BUDGET 2024': [1000, 2000, 1500],
            'BUDGET 2025': [1050, 2100, 1575],
            'BUDGET 2026': [1102.50, 2205, 1653.75],
            'TOTAL THREE YEARS': [0.50, 6305, 4728.75],
            'ACTUAL 2023': [900, 1800, 1400],
            'BUDGET 2023': [952.38, 1904.76, 1428.57]
            }),
        
        "FINES GENERAL ()": pd.DataFrame({
            'ECONOMIC_CODE': ['12020501', '12020502', '12020503'],
            'N.TR_CODE': ['12020000', '12020000', '12020000'],
            'DESCRIPTION': ['FINES AND PENALTIES', 'TOWING OF VEHICLES', 'ENVIRONMENTAL SANITATION FINE'],
            'BUDGET 2024': [1000, 2000, 1500],
            'BUDGET 2025': [1050, 2100, 1575],
            'BUDGET 2026': [1102.50, 2205, 1653.75],
            'TOTAL THREE YEARS': [3152.50, 6305, 4728.75],
            'ACTUAL 2023': [900, 1800, 1400],
            'BUDGET 2023': [952.38, 1904.76, 1428.57]
            }),
        # Department of Finance and Supply
        "Department of Finance and Supply" : pd.DataFrame({
            "ECONOMIC_CODE": ["21010101", "21010102", "21020101"],
            "DESCRIPTION": ["SALARY", "OVERTIME PAYMENT", "NON REGULAR ALLOWANCES"],
            "NO. OF STAFF": [120, 0.00, 0.00],
            "BUDGET 2024": [191272168.24, 0.00, 0.00],
            "BUDGET 2025": [200835776.65, 0.00, 0.00],
            "BUDGET 2026": [210877565.48, 0.00, 0.00],
            "TOTAL THREE YEARS": [602985510.37, 0.00, 0.00],
            "ACTUAL 2023": [104709753.19, 0.00, 0.00],
            "BUDGET 2023": [156335592.15, 0.00, 0.00]
        }),

        # Department Planning and Budget/Research and Statistic Office
        "Department Planning and Budget" : pd.DataFrame({
            "ECONOMIC_CODE": ["21010101", "21010102", "21020101"],
            "DESCRIPTION": ["SALARY", "OVERTIME PAYMENT", "NON REGULAR ALLOWANCES"],
            "NO. OF STAFF": [4, 0.00, 0.00],
            "BUDGET 2024": [7517029.80, 0.00, 0.00],
            "BUDGET 2025": [7892881.29, 0.00, 0.00],
            "BUDGET 2026": [8287525.35, 0.00, 0.00],
            "TOTAL THREE YEARS": [23697436.44, 0.00, 0.00],
            "ACTUAL 2023": [3068857.24, 0.00, 0.00],
            "BUDGET 2023": [2933315.55, 0.00, 0.00]
        }),

        # Legal Department
        "Legal Department" : pd.DataFrame({
            "ECONOMIC_CODE": ["21010101", "21010102", "21020101"],
            "DESCRIPTION": ["SALARY", "OVERTIME PAYMENT", "NON REGULAR ALLOWANCES"],
            "NO. OF STAFF": [3, 0.00, 0.00],
            "BUDGET 2024": [14905741.95, 0.00, 0.00],
            "BUDGET 2025": [15651029.05, 0.00, 0.00],
            "BUDGET 2026": [16433580.50, 0.00, 0.00],
            "TOTAL THREE YEARS": [46990351.50, 0.00, 0.00],
            "ACTUAL 2023": [6192809.40, 0.00, 0.00],
            "BUDGET 2023": [1992994.80, 0.00, 0.00]
        }),

        # Department of Education
        "Department of Education" : pd.DataFrame({
            "ECONOMIC_CODE": ["21010101", "21010102"],
            "DESCRIPTION": ["SALARY", "OVERTIME PAYMENT"],
            "NO. OF STAFF": [19, 0.00],
            "BUDGET 2024": [34152979.33, 0.00],
            "BUDGET 2025": [35860628.29, 0.00],
            "BUDGET 2026": [37653659.71, 0.00],
            "TOTAL THREE YEARS": [107667267.32, 0.00],
            "ACTUAL 2023": [16297674.70, 0.00],
            "BUDGET 2023": [33496371.60, 0.00]
        }),

        # Department of Health Care
        "Department of Health Care" : pd.DataFrame({
            "ECONOMIC_CODE": ["21010101", "21010102", "21020101"],
            "DESCRIPTION": ["SALARY", "OVERTIME PAYMENT", "NON REGULAR ALLOWANCES"],
            "NO. OF STAFF": [92, 0.00, 0.00],
            "BUDGET 2024": [262908906.75, 0.00, 0.00],
            "BUDGET 2025": [276054352.09, 0.00, 0.00],
            "BUDGET 2026": [289857069.69, 0.00, 0.00],
            "TOTAL THREE YEARS": [828820328.53, 0.00, 0.00],
            "ACTUAL 2023": [141342425.79, 0.00, 0.00],
            "BUDGET 2023": [224842335.00, 0.00, 0.00]
        }),

        # Internal Audit
        "Internal Audit" : pd.DataFrame({
            "ECONOMIC_CODE": ["21010101", "21010102", "21020101"],
            "DESCRIPTION": ["SALARY", "OVERTIME PAYMENT", "NON REGULAR ALLOWANCES"],
            "NO. OF STAFF": [2, 0.00, 0.00],
            "BUDGET 2024": [6479326.20, 0.00, 0.00],
            "BUDGET 2025": [6803292.51, 0.00, 0.00],
            "BUDGET 2026": [7143457.14, 0.00, 0.00],
            "TOTAL THREE YEARS": [20426075.85, 0.00, 0.00],
            "ACTUAL 2023": [0.00, 0.00, 0.00],
            "BUDGET 2023": [816046.35, 0.00, 0.00]
        }),

        # Office of Personnel Management
        "Office of Personnel Management" : pd.DataFrame({
            "ECONOMIC_CODE": ["21010101", "21010102", "21020101"],
            "DESCRIPTION": ["SALARY", "OVERTIME PAYMENT", "NON REGULAR ALLOWANCES"],
            "NO. OF STAFF": [125, 0.00, 0.00],
            "BUDGET 2024": [191333493.86, 0.00, 0.00],
            "BUDGET 2025": [200900168.56, 0.00, 0.00],
            "BUDGET 2026": [210945176.98, 0.00, 0.00],
            "TOTAL THREE YEARS": [603178839.40, 0.00, 0.00],
            "ACTUAL 2023": [120693810.95, 0.00, 0.00],
            "BUDGET 2023": [152383761.00, 0.00, 0.00]
        })
        
        
    }
        


    for key, df in data_dict.items():
        # Calculate the required fields
        df['BUDGET 2023'] = df['BUDGET 2024'] / 1.05
        df['BUDGET 2025'] = df['BUDGET 2024'] * 1.05
        df['BUDGET 2026'] = df['BUDGET 2025'] * 1.05
        df['TOTAL THREE YEARS'] = df['BUDGET 2024'] + df['BUDGET 2025'] + df['BUDGET 2026']

        if key not in st.session_state:
            st.session_state[key] = df

 # Function to add a record to a DataFrame in session state
# Define constant values for specific fields
CONSTANT_CODES = {
    "RS_CODE": "12000000",
    "IR_CODE": "12010000",
    "TR_CODE": "12010100",
    "N.TR_CODE": "12010200"
}



# Function to add a record to a DataFrame in session state with calculated fields
def add_record(df_key, record):
    """Add a record to the selected DataFrame in session state with calculated fields."""
    
    # Retrieve the DataFrame to determine which columns are required
    df = st.session_state[df_key]
    
    # Required fields for every table
    required_fields = ['ECONOMIC_CODE', 'DESCRIPTION', 'BUDGET 2024', 'ACTUAL 2023']

    # Optional fields (columns other than the required ones)
    optional_fields = [col for col in df.columns if col not in required_fields]

    # Check that all required fields are filled in
    if not all([record.get(field) for field in required_fields]):
        st.error(f"Please fill out all required fields: {', '.join(required_fields)}!")
    else:
        try:
            # Ensure 'BUDGET 2024' and 'ACTUAL 2023' are numbers
            budget_2024 = float(record['BUDGET 2024'])
            actual_2023 = float(record['ACTUAL 2023'])

            # Calculate the additional fields
            record['BUDGET 2023'] = budget_2024 / 1.05
            record['BUDGET 2025'] = budget_2024 * 1.05
            record['BUDGET 2026'] = record['BUDGET 2025'] * 1.05
            record['TOTAL THREE YEARS'] = budget_2024 + record['BUDGET 2025'] + record['BUDGET 2026']

            # Append record to the DataFrame in session state
            st.session_state[df_key] = st.session_state[df_key].append(record, ignore_index=True)
            st.success("Record added successfully with calculated fields!")
        except ValueError:
            st.error("Please ensure 'BUDGET 2024' and 'ACTUAL 2023' are valid numbers!")


 # Function to delete a record from a DataFrame in session state
def delete_record(df_key, index):
     """Delete a record from the selected DataFrame in session state."""
     if 0 <= index < len(st.session_state[df_key]):
         st.session_state[df_key] = st.session_state[df_key].drop(index).reset_index(drop=True)
     else:
         st.error("Index out of range.")

 # Function to add a new user (Sign Up)
def add_user(username, password, state, local_gov):
     """Add a new user to the USER_CREDENTIALS dictionary."""
     if username in USER_CREDENTIALS:
         st.error("Username already exists. Please choose another one.")
     else:
         USER_CREDENTIALS[username] = {"password": password, "state": state, "local_gov": local_gov}
         st.success("User registered successfully. You can now log in.")

 # Main function to run the Streamlit app
def main():
     # Initialize session state for 'logged_in'
     if 'logged_in' not in st.session_state:
         st.session_state['logged_in'] = False
     if 'username' not in st.session_state:
         st.session_state['username'] = ""
     if 'state' not in st.session_state:
         st.session_state['state'] = ""
     if 'local_gov' not in st.session_state:
         st.session_state['local_gov'] = ""

     # Set background image based on login status
     if st.session_state['logged_in']:
         # Use a different background image when logged in
         set_background_image("C:/Users/HP/Desktop/PROJECT1 DEMO/LOGIN BACKGROUND.jpg")  # Replace with your logged-in background image path
     else:
         # Default background image
         set_background_image("C:/Users/HP/Desktop/PROJECT1 DEMO/BACKGROUND.webp")  # Replace with your local image path

     # Style the sidebar
     style_sidebar()

     # Title with a sky-blue tab-like base
     st.markdown('<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><h1>AUTOMATED BUDGET MANAGEMENT AND INFORMATION SERVICES (A.B.M.I.S)</h1></div>', unsafe_allow_html=True)

     # Sidebar Menu for Login and Sign Up
     menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])
     
     

     if menu == "Login":
         if st.session_state['logged_in']:
             # Welcome the user
             st.markdown(f'<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><p>Welcome, {st.session_state["username"]}!</p><p>State: {st.session_state["state"]}, Local Government: {st.session_state["local_gov"]}</p></div>', unsafe_allow_html=True)

             # Initialize DataFrames
             initialize_data()

             # Dashboard Menu
             dashboard_menu = st.sidebar.selectbox("Dashboard", ["Home", "View Data", "Add Information", "Delete Record", "Download", "Summary of All Tables", "Logout"])

             if dashboard_menu == "Home":
                 st.markdown('<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><h2>Home - A.B.M.I.S</h2><p>Use the menu to navigate through different operations.</p></div>', unsafe_allow_html=True)

             elif dashboard_menu == "View Data":
                # Select a DataFrame to view
                df_key = st.selectbox("Select DataFrame", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
                df = st.session_state.get(df_key, pd.DataFrame())  # Ensure it's a DataFrame
            
                if isinstance(df, pd.DataFrame):
                    st.markdown(f'<div class="tab-base" style="background-color: #87CEEB; padding: 10px; border-radius: 8px;"><h2>Viewing: {df_key}</h2></div>', unsafe_allow_html=True)
                    
                    # Define the specific columns to sum
                    columns_to_sum = ['BUDGET 2023', 'BUDGET 2024', 'BUDGET 2025', 'BUDGET 2026', 'TOTAL THREE YEARS', 'ACTUAL 2023', 'BUDGET 2023']
            
                    # Add the totals row to the DataFrame
                    df_with_total = add_totals_row(df, columns_to_sum)
            
                    # Display the DataFrame with totals
                    st.dataframe(df_with_total)
                else:
                    st.error("Selected item is not a DataFrame.")
                
             elif dashboard_menu == "Download":
                 # Select a DataFrame to download
                 df_key = st.selectbox("Select DataFrame to Download", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
                 df = st.session_state.get(df_key, pd.DataFrame())
                 
                 if isinstance(df, pd.DataFrame):
                     # Choose download format
                     format_choice = st.radio("Choose the format to download:", ("Excel", "PDF"))
                     
                     # Download button
                     if st.button("Download"):
                         download_file(df, format_choice)
                         
                         
             elif dashboard_menu == "Summary of All Tables":
                if st.session_state['logged_in']:
                    # Display a summary of all tables
                    display_all_tables_summary_with_download()

                    # Add this button to trigger the download
                    if st.button("Download Consolidated Budget Summary"):
                        download_excel_summary()
            
                    
                    
             elif dashboard_menu == "Add Information":
                # Select a DataFrame to add a record
                df_key = st.selectbox("SELECT FROM TABLES", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
                df = st.session_state[df_key]
            
                # Create a dictionary to store new record
                new_record = {}
            
                # Iterate through the columns in the DataFrame and provide input fields accordingly
                for col in df.columns:
                    # Automatically set constant values for specific columns
                    if col in CONSTANT_CODES:
                        new_record[col] = CONSTANT_CODES[col]
                    elif col == 'BUDGET 2024' or col == 'ACTUAL 2023':
                        new_record[col] = st.text_input(f"Enter {col}", key=f"{col}_add_{df_key}")
                    else:
                        new_record[col] = st.text_input(f"Enter {col} (Optional)", key=f"{col}_add_{df_key}")
            
                # Add the record to the DataFrame
                if st.button("Add Record"):
                    add_record(df_key, new_record)

             elif dashboard_menu == "Delete Record":
                 # Select a DataFrame to delete a record
                 df_key = st.selectbox("SELECT FROM TABLES", options=[key for key in st.session_state.keys() if isinstance(st.session_state[key], pd.DataFrame)])
                 df = st.session_state[df_key]
                 index_to_delete = st.number_input("Enter index to delete", min_value=0, max_value=len(df)-1, step=1)
                 if st.button("Delete Record"):
                     delete_record(df_key, index_to_delete)
                     st.success(f"Record at index {index_to_delete} deleted successfully.")

             elif dashboard_menu == "Logout":
                 # Logout user
                 st.session_state['logged_in'] = False
                 st.rerun()
              
         else:
             # Login form
             with st.sidebar:
                 st.subheader("Login")
                 username = st.text_input("Username")
                 password = st.text_input("Password", type="password")
                 if st.button("Login"):
                     if check_credentials(username, password):
                         # Set session state for logged-in user
                         st.session_state['logged_in'] = True
                         st.session_state['username'] = username
                         st.session_state['state'] = USER_CREDENTIALS[username]['state']
                         st.session_state['local_gov'] = USER_CREDENTIALS[username]['local_gov']
                         st.rerun()
                     else:
                         st.error("Incorrect username or password.")

     elif menu == "Sign Up":
         # Sign-up form
         with st.sidebar:
             st.subheader("Sign Up")
             new_username = st.text_input("Enter a new username")
             new_password = st.text_input("Enter a new password", type="password")
             new_state = st.text_input("Enter your State")
             new_local_gov = st.text_input("Enter your Local Government Area")
             if st.button("Sign Up"):
                 if new_username and new_password and new_state and new_local_gov:
                     add_user(new_username, new_password, new_state, new_local_gov)
                 else:
                     st.error("Please fill in all fields to sign up.")

 # Run the Streamlit app
if __name__ == "__main__":
    main()