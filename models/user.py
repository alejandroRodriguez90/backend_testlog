from database.connect import cursor, conn

cursor = cursor


def create_table_user():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
    )
    conn.commit()

    return {
        "success": "ok",
        "message": "user table created"
    }


def insert_user(name, email):
    cursor.execute(
        "INSERT INTO user (name, email) VALUES (?, ?)", (name, email)
    )
    conn.commit()
    return "ok"
