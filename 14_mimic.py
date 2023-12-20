"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import re
import sys


def mimic_dict(filename) -> dict:
  """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
  dicionario_imitador = {}
  with open(filename.strip(), 'r') as arquivo:
    #separa as palavras em uma lista
    palavras = arquivo.read().split()
    #se a palavra nao conter caractere especial ela vai
    palavras = [palavra for palavra in palavras if palavra.isalpha()]
    #pega cada palavra do texto e salva como chave e as palavras subsequentes vem como valor dessa chave
    for palavra in range(len(palavras) - 1):
      dicionario_imitador[palavras[palavra]] = palavras[palavra + 1:]

  #print(dicionario_imitador)
  return dicionario_imitador


def print_mimic(mimic_dict: dict, word: str):
  """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
  if mimic_dict.get(word) is not None:
    print(f'Temos a chave {word} no nosso acervo')
    print('Gerando trololó...')

    palavras_da_chave = mimic_dict[word]
    qtde_palavras = len(palavras_da_chave)

    print(random.choices(palavras_da_chave, k=200))
    #caso nao queira que se repita, usar o random.sample()

  else:
    print('Não temos esta palavra no nosso acervo.')


# Chama mimic_dict() e print_mimic()
def main():
  dict = mimic_dict('small.txt')
  print_mimic(dict, 'We')


if __name__ == '__main__':
  main()
