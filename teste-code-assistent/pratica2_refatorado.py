def calcular_soma_e_quantidade(numeros):
    """
    Calcula a soma e a quantidade de números da lista.
    """

    soma_total = sum(numeros)

    quantidade = len(numeros)

    return {
        "soma": soma_total,
        "quantidade": quantidade
    }


lista_numeros = [10, 20, 30]

resultado = calcular_soma_e_quantidade(lista_numeros)

print(resultado)