def substituir_vogais(texto):
    vogais = 'aeiouAEIOU'
    for vogal in vogais:
        texto = texto.replace(vogal, '*')
    return texto
    
print(substituir_vogais("Ola, como voce vai"))