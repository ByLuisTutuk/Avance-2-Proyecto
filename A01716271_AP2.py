import random
"""AL NO HABER UN REGISTRO DE ESTACIONAMIENTO LITERAL, LO QUE HICE FUE GENERAR UNO ALEATORIAMENTE PARA EL USO TEMPORAL DEL PROGRAMA."""
#Todas estas funciones asignan un valor de estacionamiento.
def asignacion1(x):
    #Aquí se generará un espacio aleatorio dependiendo de hacia qué parte del campus se dirige.
    estacionamiento = random.randint(1,100)
    return estacionamiento
def asignacion2(x):
    #Aquí se generará un espacio aleatorio dependiendo de hacia qué parte del campus se dirige.
    estacionamiento = random.randint(101,200)
    return estacionamiento
def asignacion3(x):
    #Aquí se generará un espacio aleatorio dependiendo de hacia qué parte del campus se dirige.
    estacionamiento = random.randint(201,300)
    return estacionamiento
def asignacion4(x):
    #Aquí se generará un espacio aleatorio dependiendo de hacia qué parte del campus se dirige.
    estacionamiento = random.randint(301,400)
    return estacionamiento
def asignacion5(x):
    #Aquí se generará un espacio aleatorio dependiendo de hacia qué parte del campus se dirige.
    estacionamiento = random.randint(401,500)
    return estacionamiento
def asignacion6(x):
    #Aquí se generará un espacio aleatorio dependiendo de hacia qué parte del campus se dirige.
    estacionamiento = random.randint(501,600)
    return estacionamiento
def registro():
    #Aquí se registra el vehiculo para hacer estudios.
    #Esto se usará posteriormente
    print("Vehículo registrado")
def tipopersona(persona1):
    #Función que determina la persona correspondiente
    #Aquí se elige qué tipo de persona es para ver hacía donde se debería de dirigir.
    # El ciclo while repite la función hasta que escoges una de las opciones válidas
    while persona1 != "alumno" and persona1 != "profesor" and persona1 != "asignado" and persona1 != "visitante":
        print("Escribe una opción válida.")
        persona1 = input("Inténtalo denuevo.").lower()
    #Se utiliza while 
    match persona1:
        case "alumno":
            return tipoalumno()
        case "profesor":
            tipoprofesor()
        case "asignado":
            tipoasignado()
        case "visitante":
            return tipovisitante()
def tipoalumno():
    #Función que determina el estacionamiento correspondiente dependiendo de a donde te dirijes
    #Aquí se escribe el cartel de si eres alumno y su función correspondiente
    print("Si te diriges al Edificio 1 o al 2, escribe a continuación: Primer estacionamiento")
    print("Si te diriges a la zona cercana al edifio 3 o 4 o 5 escribe a continuación: Segundo estacionamiento")
    print("Si te diriges al auditorio, plaza roja o centro de congresos escribe a continuación: Tercer Estacionamiento")
    print("Si te diriges al complejo borregos 2 o al centro estudiantil escribe a continuación: Cuarto estacionamiento")
    print("Si te diriges al edificio 13, 14 o alrededores, escribe a continuación: Quinto estacionamiento")
    print("Si te diriges a PrepaTec escribe a continuación: Sexto estacionamiento")
    print("Si te diriges a parque tecnológico este no es tu entrada.")
    print("Si no tienes un destino especifico, te asignaremos un espacio aleatorio en el tercer estacionamiento.")
    lugar = input("Selecciona una opción").lower()
    #Se le asigna un valor aleatorio diferente dependiendo de qué estacionamiento selecciona
    #Aquí el ciclo while evita errores con cualquier otro tipo de texto
    while lugar != "primer estacionamiento" and lugar != "segundo estacionamiento" and lugar != "tercer estacionamiento" and lugar != "cuarto estacionamiento" and lugar != "quinto estacionamiento" and lugar != "sexto estacionamiento" and lugar != "sin destino":
        print("Escribe una opción válida.")
        lugar = input("Inténtalo de nuevo: ").lower()
    if lugar == "primer estacionamiento":
        estacionamiento = asignacion1(lugar)
        return estacionamiento
    elif lugar == "segundo estacionamiento":
        estacionamiento = asignacion2(lugar)
        return estacionamiento
    elif lugar == "tercer estacionamiento":
        estacionamiento = asignacion3(lugar)
        return estacionamiento
    elif lugar == "cuarto estacionamiento":
        estacionamiento = asignacion4(lugar)
        return estacionamiento
    elif lugar == "quinto estacionamiento":
        estacionamiento = asignacion5(lugar)
        return estacionamiento
    elif lugar == "sexto estacionamiento":
        estacionamiento = asignacion6(lugar)
        return estacionamiento
    elif lugar == "sin destino":
        estacionamiento = asignacion3(lugar)
        return estacionamiento
def tipoprofesor():
    #Aquí se escribe el cartel de si eres profesor y su función correspondiente
    print("El estacionamiento al que se deberá dirigir es el del welcome center.")
    exit()
    #Aquí termina el código porque si eres profesor se supone que ya tienes un edificio asignado especificamente
    #Esto se puede cambiar en versiones futuras.
def tipoasignado():
    #Aquí se escribe el cartel de si ya tienes un lugar asignado y su función correspondiente
    print("Dirijase hacia su lugar establecido.")
    exit()
def tipovisitante():
    #Aquí se escribe el cartel de si eres un visitante, y se te asigna estacionamiento exclusivamente en el 3
    print("Al ser visitante, dirigete al estacionamiento 3.")
    estacionamiento = asignacion3("tercer estacionamiento")
    return estacionamiento
def main():
    #Función principal donde se ejecuta la base del programa
    print("Bienvenido al estacionamiento del Campus, por temas de organización te asignaremos un espacio de acuerdo hacia donde se dirija.")
    persona = input("Escribe a continuación si eres Alumno, Profesor o si cuentas con un estacionamiento ya asignado anteriormente.").lower()
    estacionamiento = tipopersona(persona)
    #Aquí se hace una cadena de returns para devolver el valor desde la función asignación hasta el main
    #Este if se usa para dar una mejor explicación de a dónde se debería de dirigir.
    if estacionamiento >= 1 and estacionamiento <= 100:
        print("Su lugar de estacionamiento asignado es: ",estacionamiento, ", en el primer estacionamiento")
    elif estacionamiento >= 101 and estacionamiento <= 200:
        print("Su lugar de estacionamiento asignado es: ",estacionamiento, ", en el segundo estacionamiento")
    elif estacionamiento >= 201 and estacionamiento <= 300:
        print("Su lugar de estacionamiento asignado es: ",estacionamiento, ", en el tercer estacionamiento")
    elif estacionamiento >= 301 and estacionamiento <= 400:
        print("Su lugar de estacionamiento asignado es: ",estacionamiento, ", en el cuarto estacionamiento")
    elif estacionamiento >= 401 and estacionamiento <= 500:
        print("Su lugar de estacionamiento asignado es: ",estacionamiento, ", en el quinto estacionamiento")
    elif estacionamiento >= 501 and estacionamiento <= 600:
        print("Su lugar de estacionamiento asignado es: ",estacionamiento, ", en el sexto estacionamiento")
main()