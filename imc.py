import sys 

def main():

    #Aqui es donde obtenemos la cantidad de personas
    while True:
        try:
            personas = int(input("Escribe el número de personas: "))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if personas <= 0:
            print("Debes escribir un número positivo y mayor a 0.")
            continue
        else:
            break

    #Aqui verificamos que la cantidad sea mayor a 0 si no, no tiene sentido pedir nada
    while personas > 0:
        #Le pedimos el nombre y lo guardamos en un input (Si usara Python 2.7 seria raw_input y no input pero usa python 3.7)
        while True:
            try:
                n = input("Su nombre por favor: ")
            except ValueError:
                print("Debes escribir el nombre.")
                continue

            if n == "":
                print("Debes escribir un nombre.")
                continue
            else:
                break

        #Se pide al edad que siempre es un entero por eso el int() 
        
        # Los CDC y la Academia Americana de Pediatría (AAP) 
        # recomiendan el uso del IMC para detectar el sobrepeso 
        # y la obesidad en los niños desde los 2 años de edad

        while True:
            try:
                e = int(input("Su edad en años por favor: "))
            except ValueError:
                print("Debes escribir la edad.")
                continue

            if e < 2:
                print("Debes escribir una edad de 2 años por lo menos.")
                continue
            else:
                break

        #como la altura es en metros y no centimetros hay que ponerle punto y por ende es un flotante float()
        
        # Los CDC y la Academia Americana de Pediatría (AAP) 
        # Las tablas del IMC inician con una estatura a partir de
        # los 85 cm
        # https://www.fantaproject.org/sites/default/files/resources/FANTA-BMI-charts-Enero2013-ESPANOL_0.pdf
        
        while True:
            try:
                print("Registrar la estatura en metros . centimetros")
                a = float(input("Su estatura en metros por favor: "))
            except ValueError:
                print("Debes escribir tu estatura.")
                continue

            if a < 0.85:
                print("Debes escribir una estatura mayor a 84 cm.")
                continue
            else:
                break

        #Aqui se duplica codigo pero bueno... decimos que est (de estatura) es igual a altura (No me diga)
        est = a
        #La masa en kilogramos si puede tener decimales asi que la dejamos flotante

        # Los CDC y la Academia Americana de Pediatría (AAP) 
        # Las tablas del IMC inician con un peso a partir de
        # los 10 kg

        while True:
            try:
                m = float (input("Su masa en kilogramos por favor :"))
            except ValueError:
                print("Debes escribir tu peso.")
                continue

            if m < 10:
                print("Debes escribir un peso de al menos 10 kg.")
                continue
            else:
                break

        #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
        IMC = m / est**2
        #Le decimos si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
        #Solo ruegue porque a nadie se le ocurra meter numeros negativos, le va a decir que es menor de edad
        print("\n")
        print(n)
        if(e < 18):
            print("Usted es menor de edad")
        else:
            print("Usted es mayor de edad")
        #Le imprimos el IMC para que se ponga sad
        print("Con un IMC: " + str(IMC) )

        #Hacemos las distintas validaciones
        
        if IMC >= 0 and IMC <= 15.99 :
            print("Relacionado con: ")
            print ("Delgadez severa")
        elif IMC >= 16.00 and IMC <= 16.99 :
            print("Relacionado con: ")
            print ("Delgadez moderada")
        elif IMC >= 17.00 and IMC <= 18.49:
            print("Relacionado con: ")
            print ("Delgadez leve")
        elif IMC >= 18.50 and IMC <= 24.99 :
            print ("Felicidades !! Normal")
        elif IMC >= 25.00 and IMC <= 29.99:
            print("Relacionado con: ")
            print ("Sobrepeso")
        elif IMC >= 30.00 and IMC <= 34.99:
            print("Relacionado con: ")
            print ("obesidad leve")
        elif IMC >= 35.00 and IMC <= 39.00:
            print("Relacionado con: ")
            print ("obesidad media")
        elif IMC >= 40.00:
            print("Relacionado con: ")
            print ("obesidad morbida")

        print("\n")

        input("Oprima enter para continuar")

        #Por cada persona a la que le pedimos los datos debemos restarle una (Porque ya la recorrimos)
        #si no el ciclo se vuelve infinito
        personas = personas - 1


if __name__ == "__main__":
    main()