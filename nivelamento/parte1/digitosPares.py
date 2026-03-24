def contar_pares(numero: int) -> int:
    numero_texto = str(abs(numero))
    contador = 0

    for digito in str(numero_texto):
        if int(digito) % 2 == 0:
            contador += 1
    return contador

numero = int(input("Digite algum numero: "))
resultado = contar_pares(numero)
print(f"O numero {numero} tem {resultado} digitos pares")