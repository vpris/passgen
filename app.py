import random, string
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--lenght", dest = "password_lenght", default = "16", help="Password length")

args = parser.parse_args()

password_characters = string.ascii_letters + string.digits

password = []

for i in range(int(args.password_lenght)):
    password.append(random.choice(password_characters))

random_password = (''.join(password))

print(random_password)
