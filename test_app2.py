import sqlite3
def get_user_data(username):
    conn = sqlite3.connect(':memory:') 
    cursor = conn.cursor()
    
    # TEST CASE 2: SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    
    cursor.execute(query)
    return cursor.fetchone()

# TAINTED SOURCE
# We are simulating a user typing into a prompt.
user_input = input("Enter username: ")
get_user_data(user_input)

print("System initialized...")
