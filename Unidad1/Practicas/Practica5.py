#Práctica 5. Patrones de diseño

class Logger:
    #Creamos un atributo a clase donde se guarda la unica instancia
    _instancia = None

    # __new__ es el método que controla la creación del objeto antes de init. Sirve para asegurarnos
    #de que solo exista una unica instancia de la clase Logger
    def __new__(cls, *args, **kwargs):
       #*args es un argumento posicional que permite recibir multiples parametros.
       #**kwargs permite cualquier contidad de parametros con nombre.

       # Validar si existe o no la instancia aun:
        if cls._instancia is None:
           cls._instancia = super().__new__(cls) #Creamos instancia de logger. Agregando un atributo "archivo"
           #que apunta a un archivo fisico "a" significa append = Todo lo que se escriba se agrega al final del archivo.
           cls._instancia.archivo = open("app.log", "a")
        return cls._instancia #Devolvernos siempre la misma instancia
    
    def log(self, mensaje):
        #Simulando un registro de logs
        self.archivo.write(mensaje + "\n")
        self.archivo.flush() #Método para guardar en el disco

logger1 = Logger() #Creamos la primera y unica instancia.
logger2 = Logger() #Devolver la misma instancia, sin crear una nueva.

logger1.log("Inicio de sesión en la aplicación")
logger2.log("El usuario se autentificó")

#Comprobar que sea la misma instancia en memoria
print(logger1 is logger2)


#Actividad de la práctica

class Presidente:
    _instancia = None

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.historial = []
        return cls._instancia
    
    def accion(self, accion):
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)

#Varios presidentes intentan tomar el poder
p1 = Presidente("AMLO")
p2 = Presidente("Peña Nieto")
p3 = Presidente("Fox")

#Todos apuntan al mismo presidente
p1.accion("Firmó decreto")
p2.accion("Visitó España")
p3.accion("Aprobó un presupuesto")

print("\nHistorial del presidente:")
print(p1.historial)

#Validacion de singleton
print(p1 is p2 is p3) #True o False


#1. ¿Que pasaria si eliminamos la verificacion if cls._instancia is None en el metodo new?
#2. ¿Que significa el "True" en el p1 is p2 is p3 en el contexto del motodo singleton?
#3. Es buena idea usar Singlenton para todo lo que se global? Menciona un ejemplo donde no seria recomendable.