# Esse código foi criado com base na vídeo aula do professor Adriano Santos ( https://youtu.be/_BVkHcPiNDM ).
# Apartir do pseudo código obtivemos a seguinte implementação em Python.

# Função de chamada do Quick Sort recursiva.
def quickSort(A, p, r):
    if(p < r):
        q = particao(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


# Essa função separa todos os valores menores que o pivô a esquerda e os maiores a direita.
# i é o índice do menor elemento
def particao(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


# Função main, onde será declarado o vetor e chamada inicial do Quick Sort.
# A é nosso vetor
# p será nosso índice inicial
# r será o índice final do vetor.
def main():
    A = [9, 10, -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0]
    print('\nVetor antes da ordenação: ', A)
    quickSort(A, 0, len(A)-1)
    print('\nVetor após a ordenação: ', A)


main()
