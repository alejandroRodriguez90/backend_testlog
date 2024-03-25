users = [
    "test1@test.com",
    "test2@test.com",
    "test3@test.com",
    "test4@test.com",
    "test5@test.com",
]

def get_user(email):
    if email in users:
        print("users already exist")

    else:
        return email



def resgister_user(email):
    new_user=get_user(email)
    users.append(new_user)
    return users


print (resgister_user("test8@test.com"))






#get_user("test3@test.com")
#get_user("test4555@test.com")