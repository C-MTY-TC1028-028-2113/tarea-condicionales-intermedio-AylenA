import math

def main():
    # Escribe tu código abajo de esta línea
    radio = float(input("Introduce el radio: ")) #Radio
    x1 = float(input("Introduce x1: ")) # Coordenada X1 del centro de la circunferencia
    y1 = float(input("Introduce y1: ")) # Coordenada Y1 del centro de la circunferencia
    x2 = float(input("Introduce x2: ")) # Coordenada X2 del Punto a evaluar si esta dentro o fuera
    y2 = float(input("Introduce y2: ")) # Coordenada Y2 del Punto a evaluar si esta dentro o fuera
    dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if dis>radio:
        print("FUERA")
    elif dis==radio:
        print("SOBRE")
    else:
        print("DENTRO")

if __name__ == '__main__':
    main()
