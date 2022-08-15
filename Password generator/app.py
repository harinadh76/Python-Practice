import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols = "(){}[]!@#$%^&*;'<>,./"

all = lower+upper+numbers+symbols

length = 12

password = "".join(random.sample(all, length))

print(f"password is {password}")