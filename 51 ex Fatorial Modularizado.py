''' 51. Faça uma função que receba um número inteiro,
 calcule e retorne seu fatorial
(idem exemplo anterior, porém, agora, modularizado).'''

def fatorial(n):
    fat = 1

    # itera do 1 até o número desejado
    for i in range(1, n+1):
        fat = fat * i  # realiza a multiplicação

    return fat  # retorna o resultado final
f = int(input("\nDigite o fatorial: "))
print(f"\nRESULTADO : {fatorial(f)}\n")