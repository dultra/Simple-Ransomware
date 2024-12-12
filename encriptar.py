from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("key.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

def encriptar_arquivo(nome_arquivo):

    with open("key.key", "rb") as chave_arquivo:
        chave = chave_arquivo.read()
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as arquivo:
        dados = arquivo.read()

    dados_encriptados = fernet.encrypt(dados)

    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(dados_encriptados)

if __name__ == "__main__":
    gerar_chave()
    encriptar_arquivo("alvo.txt")
    print("TÁ TRANCADO!!!! KKKKKKK")
