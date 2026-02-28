import os
from cryptography.fernet import Fernet

files = []

# Pra não criar nova chave toda vez que executa
if not os.path.exists("chave.key"):
    key = Fernet.generate_key()
    with open("chave.key", "wb") as chave:
        chave.write(key)
else:
    with open("chave.key", "rb") as chave:
        key = chave.read()

for file in os.listdir():
    if file in ["Criptografia.py", "descriptografia.py", "chave.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()

    conteudo_encrypted = Fernet(key).encrypt(conteudo)

    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)


print("Arquivos criptografados com sucesso.")