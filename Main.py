numeros_teste = [
    12, 42, 83, 25, 67, 71, 3, 4, 94, 53, 100, 48, 19, 61, 86, 33, 13, 43, 84, 28,
    81, 60, 6, 49, 40, 41, 38, 64, 44, 36, 45, 27, 11, 89, 63, 39, 9, 58, 52, 17,
    88, 77, 26, 62, 30, 96, 56, 65, 98, 99, 76, 73, 16, 95, 35, 87, 68, 69, 51,
    92, 37, 75, 90, 82, 8, 18, 23, 93, 57, 10, 15, 97, 14, 29, 7, 24, 31, 59,
    78, 85, 5, 70, 55, 91, 47, 72, 2, 20, 34, 74, 50, 66, 32, 22, 54, 79, 21,
    1, 80, 46
]

def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    tamanho = len(lista)

    for i in range(tamanho):
        for j in range(tamanho - i - 1):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return comparacoes, trocas 


def selection_sort(lista):
    comparacoes = 0
    trocas = 0
    tamanho = len(lista)

    for i in range(tamanho):
        indice_menor = i
        for j in range(i + 1, tamanho):
            comparacoes += 1
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
            trocas += 1

    return comparacoes, trocas


def insertion_sort(lista):
    comparacoes = 0
    trocas = 0

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1
            if lista[j] > atual:
                lista[j + 1] = lista[j]
                trocas += 1
                j -= 1
            else:
                break

        lista[j + 1] = atual
        trocas += 1

    return comparacoes, trocas


def shell_sort(lista):
    comparacoes = 0
    trocas = 0
    tamanho = len(lista)
    intervalo = tamanho // 2

    while intervalo > 0:
        for i in range(intervalo, tamanho):
            valor = lista[i]
            j = i

            while j >= intervalo:
                comparacoes += 1
                if lista[j - intervalo] > valor:
                    lista[j] = lista[j - intervalo]
                    trocas += 1
                    j -= intervalo
                else:
                    break

            lista[j] = valor
            trocas += 1

        intervalo //= 2

    return comparacoes, trocas


def merge_sort(lista):
    metricas = {"comparacoes": 0, "trocas": 0}

    def merge_sort_aux(sublista):
        if len(sublista) > 1:
            meio = len(sublista) // 2
            esquerda = sublista[:meio]
            direita = sublista[meio:]

            merge_sort_aux(esquerda)
            merge_sort_aux(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                metricas["comparacoes"] += 1
                if esquerda[i] < direita[j]:
                    sublista[k] = esquerda[i]
                    i += 1
                else:
                    sublista[k] = direita[j]
                    j += 1
                metricas["trocas"] += 1
                k += 1

            while i < len(esquerda):
                sublista[k] = esquerda[i]
                i += 1
                k += 1
                metricas["trocas"] += 1

            while j < len(direita):
                sublista[k] = direita[j]
                j += 1
                k += 1
                metricas["trocas"] += 1

    merge_sort_aux(lista)
    return metricas["comparacoes"], metricas["trocas"]


def quick_sort(lista):
    metricas = {"comparacoes": 0, "trocas": 0}

    def particionar(inicio, fim):
        pivo = lista[fim]
        indice = inicio - 1

        for j in range(inicio, fim):
            metricas["comparacoes"] += 1
            if lista[j] <= pivo:
                indice += 1
                lista[indice], lista[j] = lista[j], lista[indice]
                metricas["trocas"] += 1

        lista[indice + 1], lista[fim] = lista[fim], lista[indice + 1]
        metricas["trocas"] += 1
        return indice + 1

    def quick_sort_aux(inicio, fim):
        if inicio < fim:
            posicao_pivo = particionar(inicio, fim)
            quick_sort_aux(inicio, posicao_pivo - 1)
            quick_sort_aux(posicao_pivo + 1, fim)

    quick_sort_aux(0, len(lista) - 1)
    return metricas["comparacoes"], metricas["trocas"]


def heap_sort(lista):
    metricas = {"comparacoes": 0, "trocas": 0}
    tamanho = len(lista)

    def ajustar_heap(tam, raiz):
        maior = raiz
        esquerda = 2 * raiz + 1
        direita = 2 * raiz + 2

        if esquerda < tam:
            metricas["comparacoes"] += 1
            if lista[esquerda] > lista[maior]:
                maior = esquerda

        if direita < tam:
            metricas["comparacoes"] += 1
            if lista[direita] > lista[maior]:
                maior = direita

        if maior != raiz:
            lista[raiz], lista[maior] = lista[maior], lista[raiz]
            metricas["trocas"] += 1
            ajustar_heap(tam, maior)

    for i in range(tamanho // 2 - 1, -1, -1):
        ajustar_heap(tamanho, i)

    for i in range(tamanho - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        metricas["trocas"] += 1
        ajustar_heap(i, 0)

    return metricas["comparacoes"], metricas["trocas"]


def counting_sort(lista):
    comparacoes = len(lista)
    trocas = 0

    maior = max(lista)
    contagem = [0] * (maior + 1)
    resultado = [0] * len(lista)

    for numero in lista:
        contagem[numero] += 1
        trocas += 1

    for i in range(1, len(contagem)):
        contagem[i] += contagem[i - 1]

    for i in range(len(lista) - 1, -1, -1):
        resultado[contagem[lista[i]] - 1] = lista[i]
        contagem[lista[i]] -= 1
        trocas += 1

    for i in range(len(lista)):
        lista[i] = resultado[i]
        trocas += 1

    return comparacoes, trocas


algoritmos = {
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Shell Sort": shell_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
    "Counting Sort": counting_sort
}

print(f"{'algoritmo', 'comparações', 'trocas'}")

for nome, funcao in algoritmos.items():
    lista = numeros_teste.copy()
    comparacoes, trocas = funcao(lista)

    print(f"{nome, comparacoes, trocas}") 