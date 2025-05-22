import sqlite3

conn = sqlite3.connect('transactions.db', check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            type TEXT,
            amount REAL,
            description TEXT
        )
    ''')
    conn.commit()

def add_transaction(date, type, amount, description):
    cursor.execute("INSERT INTO transactions (date, type, amount, description) VALUES (?, ?, ?, ?)", 
                   (date, type, amount, description))
    conn.commit()

def fetch_all_transactions():
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    return cursor.fetchall()

def delete_transaction(id):
    cursor.execute("DELETE FROM transactions WHERE id = ?", (id,))
    conn.commit()

def update_transaction(id, date, type, amount, description):
    cursor.execute('''
        UPDATE transactions
        SET date = ?, type = ?, amount = ?, description = ?
        WHERE id = ?
    ''', (date, type, amount, description, id))
    conn.commit()

def get_expense_distribution():
    cursor.execute("""
        SELECT description, SUM(amount) FROM transactions
        WHERE type = 'Debit'
        GROUP BY description
    """)
    return cursor.fetchall()

def get_credit_debit_summary():
    cursor.execute("""
        SELECT type, SUM(amount) FROM transactions
        GROUP BY type
    """)
    return cursor.fetchall()

create_table()
