# Ransomware Simples

Este é um exemplo básico de ransomware feito em Python usando a biblioteca `cryptography`. Ele não usa uma chave fixa: uma nova chave é gerada automaticamente e salva no arquivo `key.key` toda vez que é executado.

## Como funciona

- **encriptar.py**: Gera uma chave, salva em `key.key` e encripta o arquivo alvo (no exemplo, `alvo.txt`).
- **descriptografar.py**: Usa a chave de `key.key` para descriptografar o arquivo.

## Requisitos

Instale a biblioteca com:

```bash
pip install cryptography
