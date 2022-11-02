# Autor: Romulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criacao: 28/10/22
# Ciencia da Computacao - UENF
# Disciplina: PLP

# Programa Python para implementacao do Quicksort Sort

# Esta implementacao utiliza o pivo como o ultimo elemento na
# lista
# Possui um ponteiro para acompanhar os elementos menores que o
# pivo
# No final da funcao partition(), o ponteiro e trocado
# pelo pivo para chegar a um numero "ordenado" relativo ao pivo


# Funcao para encontrar a posicao da particao
def partition(array, low, high):

    # Escolhe o elemento mais a direita como pivo
    pivot = array[high]

    # Ponteiro para o elemento maior
    i = low - 1

    # Percorre todos os elementos
    # Compara cada elemento com pivo
    for j in range(low, high):
        if array[j] <= pivot:

            # Se o elemento menor que o pivo for encontrado
            # troca com o elemento maior apontado por i
            i = i + 1

            # Trocando elemento em i com elemento em j
            (array[i], array[j]) = (array[j], array[i])

    # Troca o elemento pivo pelo elemento maior especificado por i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Retorna a posicao de onde a particao e feita
    return i + 1

# Funcao para executar quicksort


def quickSort(array, low, high):
    if low < high:

        # Encontra o elemento pivo tal que
        # elemento menor que pivo esta a esquerda
        # elemento maior que pivo esta a direita
        pi = partition(array, low, high)

        # Chamada recursiva a esquerda do pivo
        quickSort(array, low, pi - 1)

        # Chamada recursiva a direita do pivo
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Array nao ordenado")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Array ordenado em ordem crescente:')
print(data)
