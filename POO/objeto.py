from learn import Learn

neurona = Learn(0.0,0.0,0,0.005)

neurona.entrenar(40,0,9)



print ("APRENDIENDO A SUMAR ENTRE 0 Y 9\n")


while True:

    a = int(input("Introduce un primer número entre 0 y 9: "))
    b = int(input("Introduce un segundo número entre 0 y 9: "))

    res = neurona.usar(a,b)

    print(f"El resultado de {a} + {b} = {res}")

    repetir = input("¿Quieres probar de nuevo: S/N?")

    if repetir.upper() == "N":

        break 

    



