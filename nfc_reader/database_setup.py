import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
db = sqlite3.connect('db/nfc_logs.db')  # Make sure the 'db/' folder exists
cursor = db.cursor()

# Table for registered scans
cursor.execute("""
CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uid TEXT UNIQUE,
    name TEXT,
    timestamp TEXT
)
""")

# Table for logging all access attempts
cursor.execute("""
CREATE TABLE IF NOT EXISTS access_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_uid TEXT,
    access_time TEXT,
    result TEXT,
    method TEXT,
    block TEXT
)
""")

# Optional: table for user registration from web panel
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

db.commit()
db.close()

print(" Database setup completed successfully!")

