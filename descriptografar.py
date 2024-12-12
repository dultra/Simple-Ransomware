from cryptography.fernet import Fernet

def descriptografar_arquivo(nome_arquivo):

    with open("key.key", "rb") as chave_arquivo:
        chave = chave_arquivo.read()
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as arquivo:
        dados_encriptados = arquivo.read()

    dados_desencriptados = fernet.decrypt(dados_encriptados)

    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(dados_desencriptados)

if __name__ == "__main__":
    descriptografar_arquivo("alvo.txt")
    print("Destrancado :(")
