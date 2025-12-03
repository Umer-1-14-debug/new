import random
import string
length = int(input("Enter password length: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
all_chars = lower + upper + numbers
password_list = [random.choice(all_chars) for _ in range(length)]
random.shuffle(password_list)
password = "".join(password_list)
print("Generated Password:", password)
