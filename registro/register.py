from models.user import cursor, insert_user


def get_user(email):
    users = cursor.execute("select * from user")
    users = users.fetchall()
    for user in users:
        if email == user[2]:
            return True
    return False


def create_user(name, email):
    if get_user(email):
        print("El correo ya existe")
    else:
        insert_user(name, email)
        print("Usuario creado correctamente")



