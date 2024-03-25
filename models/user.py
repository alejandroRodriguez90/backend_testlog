from database.connect import cursor, conn

def create_table_user():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
    )
    conn.commit()

    return {
        "success": "ok",
        "message": "user table created"
    }


create_table_user()

def insert_user():
    cursor.execute(
        "INSERT INTO user (name, email) VALUES (?, ?)", ("david", "correo@test.com")
    )
    conn.commit()
    return "ok"

insert_user()


