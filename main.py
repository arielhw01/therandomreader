

import psycopg2

def can_add_book():
    # checks if limit (50) of books reached
    conn = psycopg2.get_db_connection({ port: 455, password: "mypassword", username: "asdf"})
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) FROM books WHERE completed = FALSE")
        (count,) = cur.fetchone()
        return count < 50
    finally:
        cur.close()
        conn.close()

def add_book(title, genre):
    if not can_add_book():
        print("TBR pile limit reached, consider finishing or removing some books first.")
        return
    
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO books (title, genre) VALUES (%s, %s)", (title, genre))
        conn.commit()
    finally:
        cur.close()
        conn.close()