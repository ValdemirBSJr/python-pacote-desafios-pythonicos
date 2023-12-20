"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def divide_e_devolve_resto(valor):
    if len(valor) % 2 == 0:
        metade_texto = len(valor) // 2
        parte_1 = valor[:metade_texto]
        parte_2 = valor[metade_texto:]
        return parte_1, parte_2
    else:
        metade_texto = len(valor) // 2
        parte_1 = valor[:(metade_texto + 1)]
        parte_2 = valor[(metade_texto + 1):]
        return parte_1, parte_2

def front_back(a, b):
    valor_1parte1,valor_1parte2  = divide_e_devolve_resto(a)
    valor_2parte1,valor_2parte2 = divide_e_devolve_resto(b)

    return valor_1parte1 + valor_2parte1 + valor_1parte2 + valor_2parte2


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
