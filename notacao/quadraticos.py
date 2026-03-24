import math

def resolver_quadratica(a: float, b:float, c:float):
    try:
        if a == 0:
            return "Nao eh uma equacao quadratica"
        delta = b**2 -4 *a*c

        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return (x1, x2)
        
        elif delta == 0:
            x = -b / (2*a)
            return (x,)
        else:
            return "Nao existem raizes reais"
    except Exception as e:
        return f"Erro: {e}"
    
print(resolver_quadratica(1, -3, 2))
print(resolver_quadratica(1, 6, 7))

def gerar_valores_quadratica(a: float, b: float, c: float, inicio:int, fim:int):
    valores = []
    for x in range(inicio, fim + 1):
        y = a*x**2 + b*x + c
        valores.append((x, y))
    return valores

for x, y in gerar_valores_quadratica(1, -3, 2, -5, 5):
    print(f"x={x}, y={y}")