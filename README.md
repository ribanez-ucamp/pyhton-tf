# pyhton-tf-mod1
# Repositorio para el trabajo final del módulo 1

Requisitos del proyecto final del módulo 1:
El proyecto debe realizarse de forma individual.
Los participantes deben entregar el link de su repositorio público de GitHub donde en el README.md detallen como hicieron su programa y qué reflexiones les ha dejado el bootcamp hasta ahora.
Entregables

Link del repositorio público de GitHub con la solución del problema en un archivo .py en la cuenta del participante donde en el README.md detalle como hicieron su programa y qué reflexiones les ha dejado el bootcamp hasta ahora.



Criterios de evaluación
NOTA: Los puntos totales deben sumar 100


Actividad
Puntos
Observaciones
Captura de datos del usuario
20
El estudiante pudo obtener exitosamente los datos del teclado del usuario y guardar cada dato en una variable diferente 
Validación de datos del usuario
25
El estudiante logró mostrar un mensaje de error si el usuario introduce un dato erróneo o no introduce dato alguno
Uso de operadores aritméticos
25
El estudiante pudo calcular exitosamente el IMC
Salida de datos
20
El estudiante fue capaz de imprimir todos los datos introducidos por el usuario junto con el cálculo del IMC
Repositorio de GitHub
10
El estudiante subió su programa de Python a un repositorio público de GitHub en su cuenta personal y requisito correctamente el README.md







NOTAS:

Se pide validar:

Primero vamos a agregar un bucle (while) para que pida que se ingrese un nuevo valor hasta que agregue uno válido. Después agregamos un try/catch para comprobar si el valor dado es un entero.
Si es un número entonces continúa
Si no es un número entonces se imprime un mensaje y luego le mandamos continue para comience nuevamente el bucle y por ende pida al usuario que escriba otro valor.
Si el valor entregado es un número entonces entra a una validación para saber si el valor es cero o mayor que cero. 
Si es menor que cero, entonces le manda un mensaje y luego nuevamente le pasamos continue para que comience el bucle nuevamente y el usuario escriba otro valor.
Si el valor es cero o mayor entonces le pasamos break para que se salga del bucle.
Si todo está bien entonces ya podremos usar el valor escrito por el usuario para el fin que deseemos.

Se realiza lo siguiente:

Se obtiene la cantidad de personas.
Se verifica que la cantidad sea mayor a 0, hasta obtener un número positivo.
Solicitamos el nombre y lo guardamos en un input.
Se pide al edad que siempre es un entero por eso el int(). 
Consideramos que los CDC (Centers for Disease Control and Prevention)  y la Academia Americana de Pediatría (AAP) recomiendan el uso del IMC para detectar el sobrepeso y la obesidad en los niños a partir de los 2 años de edad, por lo tanto, se solicita edad mínima de 2 años.
Como la altura es en metros y no centímetros hay que ponerle punto y por ende es un dato flotante float().
Los CDC y la Academia Americana de Pediatría (AAP) cuentan con tablas del IMC que inician con una estatura a partir de  los 85 cm:
https://www.fantaproject.org/sites/default/files/resources/FANTA-BMI-charts-Enero2013-ESPANOL_0.pdf
Se duplica código y decimos que est (de estatura) es igual a altura
La masa en kilogramos si se puede tener decimales así que la dejamos flotante
Los CDC y la Academia Americana de Pediatría (AAP), las tablas del IMC inician con un peso a partir de los 10 kg, por lo tanto, solicitamos al menos 10 Kg.
El cálculo del IMC, es la masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado:
IMC = m / est**2
Si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
Imprimimos el IMC para que se ponga “sad”
Se hacen las distintas validaciones
        Si  IMC >= 0 y IMC <= 15.99 :
            El índice está relacionado con Delgadez severa
        Si no Si IMC >= 16.00 and IMC <= 16.99 :
             El índice está relacionado con: Delgadez moderada
        Si no Si IMC >= 17.00 and IMC <= 18.49:
            El índice está relacionado con: Delgadez leve
        Si no Si IMC >= 18.50 and IMC <= 24.99 :
            Imprimir: ¡Felicidades !! Normal")
        Si no Si IMC >= 25.00 and IMC <= 29.99:
            El índice está relacionado con: Sobrepeso
        Si no Si IMC >= 30.00 and IMC <= 34.99:
            El índice está relacionado con: obesidad leve
        Si no Si IMC >= 35.00 and IMC <= 39.00:
            El índice está relacionado con: obesidad media
        Si no Si IMC >= 40.00:
            El índice está relacionado con: obesidad mórbida
        Saltar una línea


        Hacemos una espera


        Por cada persona a la que le pedimos los datos debemos restarle una (Porque
       ya la recorrimos)
        si no el ciclo se vuelve infinito.
Al cumplir los cálculos por el número de personas, terminamos.

