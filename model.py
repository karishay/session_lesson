ADMIN_USER="hackbright"
ADMIN_PASSWORD=5980025637247534551
#The README lied about the above.   The answer is not, in fact, 42.

def authenticate(username, password):
    print password
    print hash(password)
    if username == ADMIN_USER and hash(password) == ADMIN_PASSWORD:
        return ADMIN_USER
    else:
        return None