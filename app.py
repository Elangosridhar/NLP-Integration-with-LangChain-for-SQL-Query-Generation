from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import pandas as pd

import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Genai Key
# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    llm = genai.GenerativeModel('gemini-pro')
    response = llm.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database and return as DataFrame
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

# Define your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name FACULITY and has the following columns - FAC_NAME, STAFF_NAME, STAFF_ID, FAC_TYPE, FAC_STATUS, FAC_ADDRESS, FAC_CITY, FAC_AVAIL_BEDS, FAC_START_DATE, FAC_EXIT_DATE \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM FACILITY ;
    \nExample 2 - Tell me all the staff members , 
    the SQL command will be something like this SELECT STAFF_NAME FROM FACILITY; 
    \nExample 2 - Tell me  the staffid of jack sparrow , 
    the SQL command will be something like this SELECT STAFF_ID FROM FACILITY WHERE STAFF_NAME = "Jack sparrow"; 
    always generate first name first letter upper case and second name first letter will be  lowercas of names like "robert.jr","jack sparrow","jack daniels","john cena" in sql command generate first letter upper case "Robert.jr",,"Jack sparrow","Jack daniels","John cena"
    always generate a  e if  in sql command generate second name first letter lower case "John cena"
    also the SQL code should not have ``` in beginning or end and sql word in output
    """
]

import base64

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
    return encoded_string

# Example usage:
image_path = "cdph.png"
encoded_image = encode_image(image_path)
print(encoded_image)


# Set page configuration
st.set_page_config(page_title="I can Retrieve Any SQL query", page_icon=":bar_chart:", layout="wide")

# Add custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color:  black; /* Set background color */
        }
        h1 {
            color: white; /* Set header text color */
            text-align: center; /* Center-align header text */
            font-size: 36px; /* Set header font size */
        }
        .st-navbar {
            background-color: #2c3e50; /* Set navbar background color */
        }
        img {
            height: 100px; /* Set maximum height for the image in navbar */
            width: 100px
            padding: 5px; /* Add padding around the image */

         p{
            color:black
         }   
        }
    </style>
""", unsafe_allow_html=True)

# Add image to navbar

# Encoded image string
encoded_image = encode_image("cdph.png")

# Display the image using Markdown
st.markdown(f'<img src="data:image/png;base64,{encoded_image}" alt="Your Image">', unsafe_allow_html=True)

# Add header with custom style
st.markdown("<h1>Generate SQL Query and Its Data</h1>", unsafe_allow_html=True)

# Input field for SQL query
question = st.text_input("Enter Here")

# Tabs for Query and Table
tab_title = ['Query', 'Table']
tabs = st.tabs(tab_title)

# If submit is clicked
if question:
    response = get_gemini_response(question, prompt)
    with tabs[0]:
        st.subheader("Generated Query")
        st.write(response)

    # print("Executing SQL query:", sql_query)
    # Execute the SQL query and display as DataFrame
    df = read_sql_query(response, "Facilities.db")
    with tabs[1]:
        st.subheader("Query As Table")
        st.write(df)
        print(df)
    # print("Executing SQL query:", sql_query)
    # df = read_sql_query(sql_query, "Facilities.db")
    # print("DataFrame:", df)