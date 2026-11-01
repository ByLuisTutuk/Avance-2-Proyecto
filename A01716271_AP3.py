"""
https://github.com/ByLuisTutuk/Avance-2-Proyecto.git
Muchas de estas funciones se hacen manualmente por el bien de hacer el código, a lo que me refiero es que, por ejemplo, el registro del vehículo
es algo que se haría por automático al entrar al campus, no algo que deberíamos hacer manualmente. También, tomé en cuenta que ese programa se realiza al entrar al campus
por lo que no tendría sentido poner como funcion principal el registrar vehiculo, como aun no hemos visto bases de datos o algo similar, el propósito del código sería que las estadísticas no
se reinicien al inicio de cada uno de las entradas. Las placas no tienen un formato específico, por lo que si alguien pone cualquier cosa, también se registra.

Cambios incorporados con respecto al avance anterior:
Administración de los espacios disponibles con listas
Control de espacios disponibles para evitar duplicadas usando upper
Recuperacion de espacios cuando se retira un vehiculo
Registro de vehiculos con diccionario
Actualizacion de estadísticas
"""
import random

#Listas y diccionarios globales

#Se utiliza una lista de listas, como en el memorama, para representar los estacionamientos, cada lista representa un estacionamiento.
estacionamientos = [[], [], [], [], [], []]

#Se utiliza la placa como identificador del vehiculo, así se almacena con facilidad.
vehiculos = {}

#Hacemos un diccionario global para almacenar las estadísticas de cuantas personas de cada tipo hay en el campus estacionados
estadisticas = {
    "alumno": 0,
    "profesor": 0,
    "asignado": 0,
    "visitante": 0,
    }


# Creamos los estacionamientos disponibles
def crear_estacionamientos():
    numero = 1
    for i in range(6):
        for j in range(100):
            estacionamientos[i].append(numero)
            numero += 1

# Función que determina la persona correspondiente
def tipopersona(persona1):
    
    match persona1:
        case "alumno":
            return tipoalumno()
        case "profesor":
            return tipoprofesor()
        case "asignado":
            return tipoasignado()
        case "visitante":
            return tipovisitante()


#Función que determina el estacionamiento correspondiente dependiendo de a donde te dirijes
#Aquí se escribe el cartel de si eres alumno y su función correspondiente
def tipoalumno():
    
    print("Si te diriges al Edificio 1 o al 2, escribe a continuación: Primer estacionamiento")
    print("Si te diriges a la zona cercana al edifio 3 o 4 o 5 escribe a continuación: Segundo estacionamiento")
    print("Si te diriges al auditorio, plaza roja o centro de congresos escribe a continuación: Tercer Estacionamiento")
    print("Si te diriges al complejo borregos 2 o al centro estudiantil escribe a continuación: Cuarto estacionamiento")
    print("Si te diriges al edificio 13, 14 o alrededores, escribe a continuación: Quinto estacionamiento")
    print("Si te diriges a PrepaTec escribe a continuación: Sexto estacionamiento")
    print("Si te diriges a parque tecnológico esta no es tu entrada.")
    print("Si no tienes un destino especifico, te asignaremos un espacio aleatorio en el tercer estacionamiento.")
    
    lugar = input("Selecciona una opción").lower()
    
    #Se determina el estacionamiento
    #Aquí el ciclo while evita errores con cualquier otro tipo de texto
    
    while lugar != "primer estacionamiento" and lugar != "segundo estacionamiento" and lugar != "tercer estacionamiento" and lugar != "cuarto estacionamiento" and lugar != "quinto estacionamiento" and lugar != "sexto estacionamiento" and lugar != "sin destino":
        print("Escribe una opción válida.")
        lugar = input("Inténtalo de nuevo: ").lower()
    if lugar == "primer estacionamiento":
        return 0
    elif lugar == "segundo estacionamiento":
        return 1
    elif lugar == "tercer estacionamiento":
        return 2
    elif lugar == "cuarto estacionamiento":
        return 3
    elif lugar == "quinto estacionamiento":
        return 4
    elif lugar == "sexto estacionamiento":
        return 5
    elif lugar == "sin destino":
        return 2
    
# Aquí se escribe el cartel de si eres profesor y su función correspondiente
def tipoprofesor():
    print("El estacionamiento al que se deberá dirigir es el del Welcome Center.")
    return None

#La función tipo asignado tendría dirigir a la persona a un espacio previamente adquirido, pero como no tengo aceso a bases datos o algo parecido, entonces lo mantengo
#con la misma estructura de profesor, pero la función debería recibir la placa correspondiente que ya deberia estar asignada y aumentar el contador de las estadísticas
#ademas de que ese espacio no debería estar disponible en la función de mostrar disponible
def tipoasignado():
    print("Diríjase hacia su lugar establecido.")
    return None


# Aquí se escribe el cartel de si eres visitante
# y se te asigna estacionamiento exclusivamente en el 3
def tipovisitante():
    
    print("Al ser visitante, se te asigno un estacionamiento en el 3")
    return 2


#asignamos un espacio del estacionamiento y eliminamos en la lista global
def asignar_espacio(estacionamiento):
    if len(estacionamientos[estacionamiento]) == 0:
        print("No hay espacios disponibles en este estacionamiento")
        return None
    else:
        posicion = random.randint(0, len(estacionamientos[estacionamiento]) - 1)
        espacio = estacionamientos[estacionamiento].pop(posicion)
        return espacio


#Funcion de registro que anteriormente no podía hacer
def registro():
    #ponemos la placa en mayúsculas para que no se pueda registrar otra igual
    print("Ingresa la placa de tu vehículo")
    placa = input().upper()
    
    if placa in vehiculos:
        print("Este vehículo ya está registrado")
        return False
    else:
        persona = input("¿Eres alumno, profesor, asignado o visitante?").lower()
        
        #Validamos el tipo de persona 
        while persona != "alumno" and persona != "profesor" and persona != "asignado" and persona != "visitante":
            print("Escribe una opción válida.")
            persona1 = input("Inténtalo de nuevo: ").lower()
            
        estacionamiento = tipopersona(persona)
        
        #Como profesor no queda en el estacionamiento general, aun asi lo tenemos que guardar en estadísticas
        if persona == "profesor":
            vehiculos[placa] = [persona, None, None]
            estadisticas[persona] += 1
            print("Vehículo registrado")
            return True
        #Pasa algo parecido con los asignados, pero como aun no esta distinguido que espacio es lo deamos igual que profesor
        if persona == "asignado":
            vehiculos[placa] = [persona, None, None]
            estadisticas[persona] += 1
            print("Vehículo registrado")
            return True
            
        if estacionamiento != None:
            espacio = asignar_espacio(estacionamiento)
            
            if espacio != None:
                #almacena datos del vehículo
                vehiculos[placa] = [persona, estacionamiento, espacio]
                estadisticas[persona] += 1
                print("Vehículo registrado")
                print("Tu espacio asignado es:", espacio)
                return True
            
        return False

# Hacemos una función para que al salir el espacio quede libre
def retirar_vehiculo():
    placa = input("Ingresa la placa de tu vehículo").upper()
    
    #Se busca la placa en el diccionario de vehículos y lo elimina, también de las estadísticas
    if placa in vehiculos:
        persona = vehiculos[placa][0]
        estacionamiento = vehiculos[placa][1]
        espacio = vehiculos[placa][2]
        
        estadisticas[persona] -= 1
        vehiculos.pop(placa)
        if estacionamiento != None:
            estacionamientos[estacionamiento].append(espacio)
            print("El espacio", espacio, "está disponible nuevamente.")
            
        print("Vehiculo retirado correctamente.")
        
    else:
        print("No se encontró ningún vehículo con dicha placa")


# Se muestran los espacios disponibles de cada estacionamiento
def mostrar_disponibles():
    for i in range(6):
        disponibles = len(estacionamientos[i])
        print("Estacionamiento", i+1,":", disponibles, "espacios disponibles")


#Función que muestra cuántos vehículos registrados permanecen dentro del campus
def mostrar_estadisticas():
    print("Estadísticas del campus:")
    for persona in estadisticas:
        print(persona,":", estadisticas[persona])


#Display del menú y opción
def menu():

    print("""
     Opciones disponibles:
     1. Retirar vehículo
     2. Consultar espacios disponibles
     3. Consultar estadísticas
     4. Salir
     5. Registrar otro vehículo (para pruebas)""")
    
    opcion = input("Seleccione una opción")
    
    return opcion


#Funcion principal donde se despliega el menú interaccionable
def main():
    crear_estacionamientos()
    print("Bienvenido a Tec de Monterrey Campus QRO")
    print("Registrate para poder avanzar.")
    op = input("s/n").lower()
    if op == "s":
        registrado = registro()
    else:
        registrado = False
        
    if registrado == False:
        print("No puede avanzar sin estar registrado.")
        
    while registrado:
        opcion = menu()
        
        match opcion:
            case "1":
                retirar_vehiculo()
            case "2":
                mostrar_disponibles()
            case "3":
                mostrar_estadisticas()
            case "4":
                registrado = False
            case "5":
                registro()
            case _:
                print("Selecicona una opción válida")


main()
