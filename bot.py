import os

token = os.getenv("TOKEN")

print("TOKEN ENCONTRADO:", token is not None)

if token:
    print("LONGITUD:", len(token))
else:
    print("TOKEN NO ENCONTRADO")
