import sqlite3

# Connect to the database (creates the database file if it doesn't exist)
conn = sqlite3.connect("help_desk.db")
cursor = conn.cursor()

# Create the table to store the data
cursor.execute("""
CREATE TABLE IF NOT EXISTS calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    status TEXT
)
""")

# Function to add a new call to the database
def add_call(date, time, status):
    cursor.execute("""
    INSERT INTO calls (date, time, status)
    VALUES (?, ?, ?)
    """, (date, time, status))
    conn.commit()

# Example usage: add a call on 2/1/2023 at 12:30 PM with status "unresolved"
add_call("2/1/2023", "12:30 PM", "unresolved")

# Function to retrieve all calls from the database
def get_all_calls():
    cursor.execute("""
    SELECT * FROM calls
    """)
    return cursor.fetchall()

# Example usage: retrieve all calls from the database
print(get_all_calls())

# Close the database connection when finished
conn.close()
