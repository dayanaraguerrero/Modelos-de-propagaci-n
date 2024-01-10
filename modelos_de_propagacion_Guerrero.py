import math

def espacio_libre():
    print("PROPAGACIÓN ESPACIO LIBRE")
    f1 = int(input("Ingrese el valor de la frecuencia en Hz: "))
    d1 = int(input("Ingrese el valor de la distancia en metros: "))
    
    print("Seleccione el entorno:")
    print("1. Espacio libre (Free Space)")
    print("2. Área urbana celular (2.7 a 3.5)")
    print("3. Área sombreada de radio celular (3 a 5)")
    print("4. Línea de visión en edificio (1.6 a 1.8)")
    print("5. Edificio obstruido (4 a 6)")
    print("6. Fábricas obstruidas (2 a 3)")
    
    opcion_entorno = int(input("Seleccione la opción correspondiente al entorno: "))

    if 1 <= opcion_entorno <= 6:
        exponente_n = [2, 2.7, 3, 1.6, 4, 2][opcion_entorno - 1]
        atenuacion = 20 * math.log10(f1) + 10 * exponente_n * math.log10(d1) - 147.56
        print("La atenuación en este entorno es:", atenuacion)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        print("Opción no válida... vuelva a intentarlo")

def okumura_hata():
    print("MODELO OKUMURA HATA")
    print("Escoja la opción que requiere:")
    print("1. Ciudades Medianas")
    print("2. Grandes Ciudades")
    opc3 = int(input("Qué opción desea escoger: "))

    if opc3 == 1:
        print("Ciudades Medianas")
        hr = float(input("Ingrese valor de hr: "))
        fc = int(input("Ingrese el valor de fc en MHz: "))
        
        Ahr = (1.1 * math.log10(fc) - 0.7) * hr - (1.56 * math.log10(fc) - 0.8)
        print("El valor de Ahr es:", Ahr)
        
        ht = float(input("Ingrese el valor de ht: "))
        d = float(input("Ingrese el valor de d: "))
        
        Ldbm = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - Ahr + (44.9 - 6.55 * math.log10(ht)) * math.log10(d)
        print("La pérdida en una ciudad mediana sería:", Ldbm)
        
        print("1. Urbana")
        print("2. Abierta")
        opc4 = int(input("Ingrese la opción: "))
        
        if opc4 == 1:
            Ldbu = Ldbm - 2 * (math.log10(fc / 28))**2 - 5.4
            print("La pérdida en la ciudad urbana sería:", Ldbu)
        elif opc4 == 2:
            Ldba = Ldbm - 4.78 * (math.log10(fc))**2 - 18.733 * math.log10(fc) - 40.98
            print("La pérdida que se obtiene en la ciudad abierta es de:", Ldba)
        else:
            print("Opción no válida")
    elif opc3 == 2:
        print("Grandes Ciudades")
        print("Escoja si desea fc mayor o menor")
        print("1. Para fc <= 300 MHz ")
        print("2. Para fc >= 300 MHz ")
        opc2 = int(input("Qué opción desea escoger: "))

        if opc2 == 1 or opc2 == 2:
            hr = float(input("Ingrese valor de hr: "))
  
            if opc2 == 1:
                Ahr = 8.29 * (math.log10(1.54 * hr))**2 - 1.1
            else:
                Ahr = 3.2 * (math.log10(11.75 * hr))**2 - 4.97
            print("El valor de Ahr es:", Ahr)
            
            ht = float(input("Ingrese el valor de ht: "))
            d = float(input("Ingrese el valor de d: "))
            fc = int(input("Ingrese el valor de fc en MHz: "))

            Ldbg = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - Ahr + (44.9 - 6.55 * math.log10(ht)) * math.log10(d)
            print("La pérdida en la ciudad es:", Ldbg)
        else:
            print("Opción no válida... vuelva a intentarlo")
    else:
        print("Opción no válida... vuelva a intentarlo")

print("MODELOS DE PROPAGACIÓN")
print("¿Qué modelo de Propagación desea escoger?")
print("1. Propagación Espacio Libre")
print("2. Modelo Okumura Hata")
opc = int(input("¿Con qué modelo va trabajar?:"))

if opc == 1:
    espacio_libre()
elif opc == 2:
    okumura_hata()
else:
    print("No es correcto: Revise bien...")

