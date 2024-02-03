# Import necessary libraries
import streamlit as st
import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('resumes.db')
cursor = conn.cursor()

# Create a table to store resumes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        skills TEXT,
        experience TEXT
    )
''')
conn.commit()

# Streamlit UI
st.title('Resume ATS System')

# Input form for resume details
name = st.text_input('Full Name')
email = st.text_input('Email')
phone = st.text_input('Phone')
skills = st.text_area('Skills')
experience = st.text_area('Experience')

if st.button('Submit Resume'):
    # Insert resume details into the database
    cursor.execute('''
        INSERT INTO resumes (name, email, phone, skills, experience) VALUES (?, ?, ?, ?, ?)
    ''', (name, email, phone, skills, experience))
    conn.commit()
    st.success('Resume submitted successfully!')

# Display all resumes
st.subheader('All Resumes')
resumes = cursor.execute('SELECT * FROM resumes').fetchall()

for resume in resumes:
    st.write(f"**ID:** {resume[0]}, **Name:** {resume[1]}, **Email:** {resume[2]}, **Phone:** {resume[3]}")
    st.write(f"**Skills:** {resume[4]}")
    st.write(f"**Experience:** {resume[5]}")
    st.write('---')

# Close the database connection
conn.close()
