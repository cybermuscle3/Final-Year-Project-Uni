import sqlite3
from datetime import datetime
import hashlib

# Path to your SQLite database
db_path = "db/nfc_logs.db"  # Adjust if needed

# Connect to database
def connect():
    return sqlite3.connect(db_path)

# Hash the UID for privacy (SHA-256)
def hash_uid(uid):
    return hashlib.sha256(uid.encode()).hexdigest()

# Add a log entry (hashed UID + optional block number)
def add_log(uid, result, method, block=None):
    conn = connect()
    cursor = conn.cursor()
    hashed = hash_uid(uid)
    cursor.execute("""
        INSERT INTO access_logs (card_uid, access_time, result, method, block)
        VALUES (?, ?, ?, ?, ?)""",
        (hashed, datetime.now(), result, method, block))
    conn.commit()
    conn.close()

# Get all logs ordered by most recent
def get_logs():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM access_logs ORDER BY access_time DESC")
    logs = cursor.fetchall()
    conn.close()
    return logs

# Register a new user
def register_user(name, email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

