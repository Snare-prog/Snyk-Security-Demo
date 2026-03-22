import sqlite3

# TEST CASE 1: Hardcoded Secret (Security Risk)
# Why: Hackers scan repos for these to gain access to systems.
DB_PASSWORD = "Admin_Password_123!" 

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # TEST CASE 2: SQL Injection (Critical Vulnerability)
    # Why: Directly formatting a string with user input allows a hacker to 
    # bypass login or delete the database.
    query = "SELECT * FROM users WHERE username = '%s'" % username
    
    cursor.execute(query)
    return cursor.fetchone()

# TEST CASE 3: Code Smell (Maintenance Issue)
# Why: Unused variables clutter code and make it harder to read.
unused_metadata = "v1.0.2-beta" 

print("System initialized...")
