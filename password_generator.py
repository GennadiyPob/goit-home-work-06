import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Згенерувати пароль довжиною 8 символів
password = generate_password(8)
print(password)
