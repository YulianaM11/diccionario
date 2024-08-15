def mostrar_menu():
    """
    Muestra el menú interactivo del diccionario informático.
    """
    print("\n////// Diccionario Informático //////")
    print("1. *Buscar un término*")
    print("2. *Agregar un término*")
    print("3. *Eliminar un término*")
    print("4. *Ver todos los términos*")
    print("5.       //Salir//")

def buscar_termino(diccionario, termino):
    """
    Busca un término en el diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.
    termino (str): Término a buscar.

    Retorna:
    str: Definición del término o un mensaje indicando que no se encontró.
    """
    try:
        return diccionario[termino.lower()]
    except KeyError:
        return f"El término '{termino}' no se encuentra en el diccionario."

def agregar_termino(diccionario, termino, definicion):
    """
    Agrega un nuevo término y su definición al diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.
    termino (str): Término a agregar.
    definicion (str): Definición del término.

    Retorna:
    str: Mensaje confirmando que el término fue agregado.
    """
    diccionario[termino.lower()] = definicion
    return f"El término '{termino}' ha sido agregado exitosamente."

def eliminar_termino(diccionario, termino):
    """
    Elimina un término del diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.
    termino (str): Término a eliminar.

    Retorna:
    str: Mensaje confirmando que el término fue eliminado o indicando que no se encontró.
    """
    try:
        del diccionario[termino.lower()]
        return f"El término '{termino}' ha sido eliminado exitosamente."
    except KeyError:
        return f"El término '{termino}' no se encuentra en el diccionario."

def ver_todos_terminos(diccionario):
    """
    Muestra todos los términos y definiciones del diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.

    Retorna:
    str: Términos y definiciones en formato de lista.
    """
    if not diccionario:
        return "El diccionario está vacío."
    return "\n".join([f"{term}: {definition}" for term, definition in diccionario.items()])

def main():
    """
    Función principal que ejecuta el menú interactivo del diccionario informático.
    """
    diccionario = {
        "middleware": "Software que actúa como intermediario entre diferentes aplicaciones o servicios.",
        "vpn": "Red privada virtual que crea una conexión segura y cifrada a través de una red pública.",
        "virus": "Programa malicioso que se replica y puede infectar otros archivos y sistemas.",
        "computadora": "es un dispositivo electrónico capaz de procesar y almacenar información, siguiendo instrucciones específicas para realizar una amplia variedad de tareas.",
        "ethernet": "Red cableada para conectar dispositivos en una red local.",
        "name": "se utiliza para nombrar algo dentro del código",
        "software": "Conjunto de instrucciones y datos que indican a un ordenador cómo realizar tareas.",
        "array": "Estructura de datos que almacena una colección de elementos en un orden específico.",
        "protocol": "Conjunto de reglas que determinan cómo se transmite y recibe información en una red.",
        "python": "Lenguaje de programación interpretado, conocido por su simplicidad.",
        "jpeg": "Formato de compresión de imágenes para reducir el tamaño de archivos gráficos.",
        "bandwidth": "Capacidad de transmisión de datos de una red en un tiempo determinado.",
        "bluetooth": "Estándar de tecnología inalámbrica para intercambiar datos a corta distancia.",
        "bit": "La unidad más pequeña de datos en un ordenador, representada como 0 o 1.",
        "cache": "Almacenamiento temporal de datos para acceso más rápido.",
        "cloud computing": "Distribución de servicios informáticos a través de internet.",
        "compiler": "Programa que traduce código fuente a código máquina.",
        "cybersecurity": "Práctica de proteger sistemas, redes y programas de ataques digitales.",
        "database": "Colección organizada de datos accesible y gestionable.",
        "debugging": "Proceso de encontrar y corregir errores en un programa.",
        "encryption": "Método para proteger información convirtiéndola en un formato seguro.",
        "firewall": "Sistema de seguridad de red que controla el tráfico de entrada y salida.",
        "frontend": "Parte de un sitio web o aplicación que interactúa directamente con el usuario.",
        "gigabyte": "Unidad de almacenamiento digital equivalente a 1,024 megabytes.",
        "hacker": "Persona que explora, manipula o accede a sistemas de manera no autorizada.",
        "http": "Protocolo de transferencia de hipertexto utilizado en la comunicación en la web.",
        "https": "Versión segura del protocolo HTTP, que cifra los datos enviados entre el navegador y el servidor.",
        "ip address": "Dirección única que identifica a un dispositivo en una red.",
        "iteration": "Repetición de un proceso en un bucle hasta que se cumpla una condición específica.",
        "latency": "Tiempo que tarda un paquete de datos en viajar desde el origen hasta el destino.",
        "machine learning": "Rama de la inteligencia artificial que permite a las máquinas aprender de los datos.",
        "malware": "Software malicioso diseñado para dañar o comprometer la seguridad de un sistema.",
        "megabyte": "Unidad de almacenamiento digital equivalente a 1,024 kilobytes.",
        "multithreading": "Capacidad de un procesador para ejecutar múltiples hilos simultáneamente.",
        "network": "Conjunto de computadoras y dispositivos interconectados.",
        "node": "Punto de conexión en una red que puede enviar, recibir o reenviar datos.",
        "open source": "Software cuyo código fuente está disponible para el público.",
        "packet": "Unidad de datos que se transmite a través de una red.",
        "pixel": "Unidad más pequeña de una imagen digital.",
        "byte": "Unidad de información digital que generalmente consta de 8 bits.",
        "algorithm": "Conjunto de instrucciones para realizar una tarea o resolver un problema.",
        "microprocessor": "Circuito integrado que realiza funciones de una computadora.",
        "servomotor": "Dispositivo similar a un motor de corriente continua que puede ubicarse en cualquier posición dentro de su rango de operación.",
        "motherboard": "Placa base que contiene los componentes principales de un ordenador.",
        "query": "Solicitud de información de una base de datos.",
        "ram": "Memoria de acceso aleatorio utilizada por el sistema operativo y las aplicaciones.",
        "runtime": "Período durante el cual un programa se está ejecutando.",
        "script": "Archivo de código que se ejecuta de forma automatizada.",
        "seo": "Proceso de mejorar la visibilidad de un sitio web en los resultados de búsqueda.",
        "server": "Computadora o sistema que proporciona recursos o servicios a otros dispositivos en una red.",
        "api": "Interfaz de programación de aplicaciones que permite la comunicación entre diferentes software.",
        "cookie": "Pequeño archivo que se almacena en el navegador del usuario para rastrear información sobre su actividad en la web.",
        "firmware": "Software que está permanentemente incrustado en un hardware.",
        "syntax": "Conjunto de reglas que definen cómo se deben escribir los programas en un lenguaje de programación.",
        "tcp/ip": "Conjunto de protocolos que permite la comunicación entre computadoras en una red.",
        "ui": "Interfaz de usuario, parte de una aplicación o sistema con la que el usuario interactúa.",
        "url": "Dirección utilizada para acceder a recursos en la web.",
        "virtual machine": "Software que emula un sistema operativo dentro de otro sistema operativo.",
        "xml": "Lenguaje de marcado utilizado para almacenar y transportar datos de manera estructurada.",
        "boot": "Proceso de iniciar un sistema operativo en un ordenador.",
        "chip": "Circuito integrado que contiene los componentes electrónicos necesarios para ejecutar tareas computacionales.",
        "dns": "Sistema que traduce nombres de dominio a direcciones IP.",
        "gigahertz": "Unidad de frecuencia utilizada para medir la velocidad de los procesadores.",
        "input": "Datos que se ingresan en un sistema o dispositivo.",
        "ip": "Protocolo de internet para el enrutamiento de paquetes de datos en una red.",
        "router": "Dispositivo que dirige el tráfico de datos entre diferentes redes.",
        "thread": "Secuencia de ejecución dentro de un proceso que puede ejecutarse concurrentemente con otros hilos."
    }


    while True:
        mostrar_menu()
        try:
            opcion = int(input("***  Selecciona una opción:  ***"))
            if opcion == 1:
                termino = input("Ingresa el término a buscar: ")
                print(buscar_termino(diccionario, termino))
            elif opcion == 2:
                termino = input("Ingresa el nuevo término: ")
                definicion = input("Ingresa la definición del término: ")
                print(agregar_termino(diccionario, termino, definicion))
            elif opcion == 3:
                termino = input("Ingresa el término a eliminar: ")
                print(eliminar_termino(diccionario, termino))
            elif opcion == 4:
                print(ver_todos_terminos(diccionario))
            elif opcion == 5:
                print("Saliendo del diccionario. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

if __name__ == "__main__":
    main()
