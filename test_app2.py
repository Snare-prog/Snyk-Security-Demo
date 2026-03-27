import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # TEST CASE 2: SQL Injection (Critical Vulnerability)
    # Why: Directly formatting a string with user input allows a hacker to 
    # bypass login or delete the database.
    query = "SELECT * FROM users WHERE username = '%s'" % username
    
    cursor.execute(query)
    return cursor.fetchone()

print("System initialized...")
