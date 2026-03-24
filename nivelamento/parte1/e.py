n = 2048

for i in str(n):
    digito = (n//10**i)%10
    if digito % 2 == 0:
        print(f"{digito} Par")
    else:
        print(f"{digito} Impar")


