print("===========[REVERTENDO PALAVRAS]===========\n")
palavra = input("Digite uma palavra: ")


def reverse(palavra: str):
    tamanho = len(palavra)
    palavra_list = list(palavra)

    for i in range(tamanho):
        j = (tamanho - 1) - i

        if i == j:
            break
        else:
            tmp = palavra[i]
            palavra_list[i] = palavra[j]
            palavra_list[j] = tmp

    print(f"・Reverso de {palavra} é", "".join(palavra_list))


reverse(palavra)
