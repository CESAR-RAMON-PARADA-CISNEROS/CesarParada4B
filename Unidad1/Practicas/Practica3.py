#Práctica 3. Introducción al polimorfismo
#Simular un sistema de cobro con múltiples opciones de pago

class pago_tarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta bancaria"
    
class transferencia:
    def procesar_pago(self, cantidad):
        return f"Procesando pago con transferencia por la cantidad de ${cantidad}"
    
class deposito:
    def procesar_pago(self, cantidad):
        return f"Procesando pago por medio deposito en ventanilla por la cantidad de ${cantidad}"
    
class paypal:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} por medio de paypal"
    
#Instancia
metodos_pago = [pago_tarjeta(), transferencia(), deposito(), paypal()]

#for m in metodos_pago:
#    print(m.procesar_pago(200))


# ACTIVIDAD PROCESAR PAGO CON DIFERENTES CANTIDADES EN CADA UNO DE LAS FORMAS DE PAGO
# EJEMPLO: 100 CON TARJETA, 500 CON TRANSFERENCIA , 2000 CON PAYPAL, 400 CON DEPOSITO

pago1 = pago_tarjeta()
pago2 = transferencia()
pago3 = deposito()
pago4 = paypal()

#Polimorfismo: Mismo método con diferentes objetos.
print(pago1.procesar_pago(100))
print(pago2.procesar_pago(500))
print(pago3.procesar_pago(400))
print(pago4.procesar_pago(2000))


#ACTIVIDAD 2
#Simular el envio de una notificacion desde distitas aplicaciones
#Creacion de Clases
class whatsapp():
    def enviar_notificacion(self, aplicacion):
        return f"La notificación se envió via {aplicacion}"

class mensajes():
    def enviar_notificacion(self, aplicacion):
        return f"La notificación mando por la aplicacion de {aplicacion}"
    
class correo_electronico():
    def enviar_notificacion(self, aplicacion):
        return f"La notificación se mandó via {aplicacion}"

class telegram():
    def enviar_notificacion(self, aplicacion):
        return f"La notificación se mandó via la aplicación {aplicacion}"
    
#Creacion de Instancias
notificacion1 = whatsapp()
notificacion2 = mensajes()
notificacion3 = correo_electronico()
notificacion4 = whatsapp()

#Muestra del resultado
print(notificacion1.enviar_notificacion("WhatsApp"))
print(notificacion2.enviar_notificacion("Mensajes"))
print(notificacion3.enviar_notificacion("Correo Electrónico"))
print(notificacion4.enviar_notificacion("Telegram"))