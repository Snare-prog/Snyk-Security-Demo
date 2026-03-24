import sqlite3
import os

# FIX 1: Use Environment Variables (Secure)
# Instead of hardcoding, we fetch the secret from the system environment.
# This prevents the password from ever being committed to GitHub.
DB_PASSWORD = os.getenv("DATABASE_SECURE_PASSWORD", "default_safe_value") 

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # FIX 2: Parameterized Query (Prevents SQL Injection)
    # We use '?' as a placeholder. The sqlite3 library will treat 
    # the 'username' variable strictly as DATA, not as CODE.
    query = "SELECT * FROM users WHERE username = ?"
    
    # Pass the variable as a tuple in the second argument
    cursor.execute(query, (username,))
    
    return cursor.fetchone()

# FIX 3: Remove Dead Code (Maintainability)
# The variable 'unused_metadata' was deleted because it added 
# no value and increased technical debt.

print("System initialized securely...")
