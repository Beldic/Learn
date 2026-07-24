from learn import Learn

neurona = Learn(0.0,0.0,0,0.005)

neurona.entrenar(500,0,1000,1000,True)



print ("APRENDIENDO A SUMAR ENTRE 0 Y 1000\n")


while True:

    a = int(input("Introduce un primer número entre 0 y 1000: "))
    b = int(input("Introduce un segundo número entre 0 y 1000: "))

    res = neurona.usar(a,b)

    print(f"El resultado de {a} + {b} = {res}")

    repetir = input("¿Quieres probar de nuevo: S/N?")

    if repetir.upper() == "N":

        break 

    



