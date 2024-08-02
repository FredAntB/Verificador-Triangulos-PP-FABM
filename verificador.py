print(f"{'='*5} VERIFICADOR DE TRIANGULOS {'='*5}")

try:
    side_A = int(input("Ingrese el lado A del triangulo: "))
    side_B = int(input("Ingrese el lado B del triangulo: "))
    side_C = int(input("Ingrese el lado C del triangulo: "))
    n_sides = len(set([side_A, side_B, side_C]))
except ValueError:
    print("Debes ingresar un número...")

if n_sides == 1:
    print("Es un triangulo Equilatero!...")
if n_sides == 2:
    print("Es un triangulo isósceles!...")
if n_sides == 3:
    print("Es un triangulo Escaleno!...")