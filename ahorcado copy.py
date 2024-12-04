import os  # Importa el módulo 'os' que permite interactuar con el sistema operativo (en este caso, para limpiar la pantalla).
import random  # Importa el módulo 'random' para generar valores aleatorios.

def play():
    # Lista de lenguajes de programación posibles en el juego.
    lenguajes = ["SQL", "JAVA", "PYTHON", "RUBY", "PHP", "JAVASCRIPT", "TYPESCRIPT", "C++", "REACT", "DART"]
    
    # Representación gráfica del ahorcado en distintas etapas, dependiendo del número de intentos fallidos.
    lista = [
        "      M", 
        "      M\n    -   -", 
        "      M\n    -   -\n    °   °", 
        "      M\n    -   -\n    °   °\n ///  3  ///", 
        "      M\n    -   -\n    °   °\n ///  3  ///\n    ----", 
        "      M\n    -   -\n    °   °\n ///  3  ///\n    ----\n=============", 
        "      M\n    -   -\n    x   x\n ///  3  ///\n    ----\n============="
    ]
    
    # Selecciona un lenguaje de la lista de lenguajes de forma aleatoria.
    aleatorio = random.choice(lenguajes)
    
    # Inicializa algunas variables
    j = 0  # Índice para recorrer la palabra seleccionada.
    b = len(lista) - 1  # Índice para llevar el control de los intentos restantes.
    condicion = True  # Variable de control del bucle principal (juego sigue mientras sea True).
    
    # Crea una lista para almacenar las letras adivinadas por el jugador.
    mostrar = []
    
    # Bucle que muestra la palabra con guiones bajos (representando las letras no adivinadas).
    while j < len(aleatorio):
        mostrar.append("_")  # Añade un guion bajo por cada letra de la palabra.
        print(aleatorio[j], end=" ")  # Imprime la letra actual con un espacio (esto no es necesario, se puede eliminar).
        j += 1  # Incrementa el índice para la siguiente letra.
    print("")  # Salto de línea después de imprimir la palabra oculta.
    
    # Bucle principal del juego, que sigue mientras la variable 'condicion' sea True.
    while condicion:
        # Solicita una letra al jugador (se convierte a mayúscula).
        letra = input("Ingrese una letra: ").upper()
        
        # Limpia la pantalla del terminal.
        os.system("cls")
        
        a = 0  # Índice para recorrer la palabra aleatoria.
        i = 0  # Contador para verificar si la letra adivinada está en la palabra.
        
        # Recorre la palabra para comprobar si la letra está en ella.
        while a < len(aleatorio):
            if aleatorio[a] != letra:  # Si la letra en la posición 'a' no coincide con la ingresada...
                i += 1  # Incrementa el contador.
                
                # Si no se encontró la letra en toda la palabra, disminuye los intentos.
                if i == len(aleatorio):
                    b -= 1  # Reduce la cantidad de intentos restantes.
                
                # Si los intentos se acaban, termina el juego y muestra el mensaje de derrota.
                if b == -1:
                    b = 0  # Evita que 'b' se vuelva negativo.
                    print("PERDISTE")  # Imprime mensaje de derrota.
                    condicion = False  # Cambia la condición a False para terminar el juego.
            
            else:
                # Si la letra está en la palabra, la coloca en la lista 'mostrar' en la misma posición.
                print("Bien")  # Indica que la letra es correcta.
                mostrar[a] = letra  # Reemplaza el guion bajo por la letra adivinada en la lista 'mostrar'.
            
            j = 0  # Restablece el índice para imprimir la palabra actualizada.
            
            # Al final de una vuelta, imprime la palabra actualizada y el estado del ahorcado.
            if a == len(aleatorio) - 1:
                while j < len(mostrar):
                    print(mostrar[j], end=" ")  # Imprime la palabra con las letras adivinadas.
                    j += 1
                print("")  # Salto de línea después de mostrar la palabra actualizada.
                print(lista[b])  # Muestra el estado actual del dibujo del ahorcado basado en los intentos restantes.
            a += 1  # Incrementa el índice 'a' para comprobar la siguiente letra.
        
        # Verifica si el jugador ha adivinado todas las letras correctamente.
        f = 0  # Contador para comprobar las letras adivinadas.
        d = 0  # Contador para contar las letras correctamente adivinadas.
        
        while f < len(aleatorio):
            if mostrar[f] == aleatorio[f]:  # Si la letra en la posición 'f' coincide con la de la palabra...
                d += 1  # Aumenta el contador de letras correctamente adivinadas.
                
                # Si todas las letras han sido adivinadas, el jugador gana y termina el juego.
                if d == len(aleatorio):
                    os.system("cls")  # Limpia la pantalla.
                    print("GANASTE")  # Imprime el mensaje de victoria.
                    condicion = False  # Cambia la condición a False para terminar el juego.
            f += 1  # Incrementa el contador 'f' para revisar la siguiente letra.
    
    # Al final, imprime la palabra final después de que el juego termine.
    j = 0
    while j < len(mostrar):
        print(mostrar[j], end=" ")  # Imprime la palabra con las letras adivinadas al final del juego.
        j += 1

# Llama a la función para comenzar el juego.
play()
