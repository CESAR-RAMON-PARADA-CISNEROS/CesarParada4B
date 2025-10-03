#Práctica 4. Herencia
#Crear un clase Ticket con los atributos: id, tipo, prioridad, estado
#Crear dos tickets de ejemplo y mostrarlos en pantalla
import os
os.system("cls")

tickets = []

class Ticket:
    def __init__(self, id, tipo, prioridad):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "pendiente"
    
    def imprimir_ticket(self):
        return f"ID: {self.id}\nTipo: {self.tipo}\nPrioridad: {self.prioridad}\nEstado: {self.estado}\n"

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar_en_ticket(self, ticket):
        return f"El empleado {self.nombre} revisa el ticket {ticket.id}"

class Desarrollador(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print("Este tipo de empleado no puede resolver este tipo de ticket")

class Tester(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print("Este tipo de empleado no puede resolver este tipo de ticket")


class ProjectManager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} a el empleado: {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)

status = True
while status:
    os.system("cls")
    print("\n\t\t---Menú---")
    print("\t1. Crear un ticket")
    print("\t2. Ver tickets")
    print("\t3. Asignar tickets")
    print("\t4. Salir del programa\n")

    op = input("Selecciona una opción: ").strip()

    if op == "1":
        os.system("cls")
        id_ticket = len(tickets) + 1
        tipo = input("Tipo de ticket (software/prueba): ").strip().lower()
        prioridad = input("Prioridad (alta/media/baja): ").strip().lower()
        nuevo = Ticket(id_ticket, tipo, prioridad)
        tickets.append(nuevo)
        print("✅ Ticket creado correctamente.\n")
        input("\n...Presiona enter para continuar...")

    elif op == "2":
        os.system("cls")
        if not tickets:
            print("No hay tickets registrados.")
        else:
            for t in tickets:
                print(t.imprimir_ticket())
        
        input("\n...Presiona enter para continuar...")

    elif op == "3":
        os.system("cls")
        if not tickets:
            print("No hay tickets para asignar")
        else:
            for i in tickets:
                print(i.imprimir_ticket())
            id_ticket = int(input("Ingrese el ID del ticket a asignar: "))
            ticket_sel = next((tk for tk in tickets if tk.id == id_ticket), None)

            if ticket_sel:
                rol = input("Asignar a (desarrollador/tester): ").strip().lower()
                nombre = input("Nombre del empleado: ").strip()
                pm = ProjectManager("Project Manager")
                if rol == "desarrollador":
                    emp = Desarrollador(nombre)
                else:
                    emp = Tester(nombre)
                pm.asignar_ticket(ticket_sel, emp)
            else:
                print("❌ Ticket no encontrado.")

            input("\n...Presiona enter para continuar...")

    elif op == "4":
        print("...Saliste del Programa...")
        status = False


#Crear tickets y empleados (Instancias de objetos)

#ticket1 = Ticket(1, "software", "media")
#ticket2 = Ticket(2, "prueba", "alta")

#developer1 = Desarrollador("Messi")
#tester1 = Tester("Juan")
#pm1 = ProjectManager("Ana")

#pm1.asignar_ticket(ticket1, developer1)
#pm1.asignar_ticket(ticket2, tester1)

#Parte adicional
# Agregar un menú con while y con if que permita:
#1. Crear un ticket
#2. Ver tickets
#3. Asignar tickets
#4. Salir del programa
