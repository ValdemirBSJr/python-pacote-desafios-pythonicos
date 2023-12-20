"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.

python.exe .\13_wordcount.py --count letras.txt
python.exe .\13_wordcount.py --topcount letras.txt
"""
import collections
import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.

import collections

def print_words(filename):
    '''
    primeiro eu crio uma lista que receberá as linhas do arquivo
    depois leio o arquivo salvando cada linha na lista com as letras em caixa baixa
    após isso uso um dicionario que receberá as letras e sua frequencia
    percorro a lista pegando cada item e retirando espaço vazio e quebra de linha
    depois percorro cada item da lista verificando se o dicionario tem uma chave com o valor da letra
    caso tenha, incrementa o valor, caso nao tenha recebe o valor padrão de 1
    por fim imprime as letras e ocorrencias

    Na segunda funcao eu ordeno o dicionario do menor para o maior de acordo com o valor e reverto
    para trazer do maior para o menor

    :param filename: arquivo que sera lido
    '''
    lista_com_as_linhas = []
    with open(filename.strip(), 'r') as arquivo:
        for linha in arquivo:
            lista_com_as_linhas.append(linha.lower())

    #print(lista_com_as_linhas)

    dicionario_contagem = {}
    for item in lista_com_as_linhas:
        item_sanitizado = item.replace(' ', '').replace('\n', '')
        for letra in item_sanitizado:
            if letra in dicionario_contagem:
                dicionario_contagem[letra] += 1
            else:
                dicionario_contagem[letra] = 1


    #print(dicionario_contagem)
    dicionario_contagem = collections.OrderedDict(sorted(dicionario_contagem.items()))
    for chave, valor in dicionario_contagem.items():
        print(f'{chave} {valor}')



def print_top(filename):
    lista_com_as_linhas = []
    with open(filename.strip(), 'r') as arquivo:
        for linha in arquivo:
            lista_com_as_linhas.append(linha.lower())

    # print(lista_com_as_linhas)

    dicionario_contagem = {}
    for item in lista_com_as_linhas:
        item_sanitizado = item.replace(' ', '').replace('\n', '')
        for letra in item_sanitizado:
            if letra in dicionario_contagem:
                dicionario_contagem[letra] += 1
            else:
                dicionario_contagem[letra] = 1

    dicionario_contagem = collections.OrderedDict(sorted(dicionario_contagem.items(), key=lambda x: x[1], reverse=True))
    for chave, valor in dicionario_contagem.items():
        print(f'{chave} {valor}')

def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
