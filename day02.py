# basic authentication

import json

file = open("secret.json", "r")

data = file.read()
file.close()



auth = json.loads(data)

username = input("Adja meg a felhasználónevét")
pswd = input("Adja meg a jelszavát")

if username == auth["usarname"] and pswd== [ "password"]:
    print (" Üdv Mesztör")

else:
    ("fdjghdhgjkfdhgjkf")

