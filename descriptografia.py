import os
from cryptography.fernet import Fernet

files = []

with open("chave.key", "rb") as key:
    secretkey = key.read()

for file in os.listdir():
    if file in ["Criptografia.py", "descriptografia.py", "chave.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()

    conteudo_decrypted = Fernet(secretkey).decrypt(conteudo)

    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_decrypted)

print("Arquivos descriptografados com sucesso.")