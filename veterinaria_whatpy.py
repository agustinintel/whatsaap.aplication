import pywhatkit as kit
import time

# Diccionario con números de teléfono y nombres
contactos = {
   # "+5492616527630": "Veterinaria Nueva Ciudad", #enviado 
   # "+5492616147019": "Veterinaria Clinica Animal Fénix", #enviado
   # "+542616906010": "Veterinaria del Plata", #enviado
   # "+5492614212305": "Centro Veterinario VillaNueva",  #numero no valido
   # "+5492614318747": "Veterinaria del Sol", #numero no valido
   # "+5492618044907": "VETERINARÍA DAL SANTO" #numero no valido
     "+5492616161263": "Veterinaria Cadore",
     "+5492614642588": "Veterinaria Sanfrancisco",
     "+5492617136380": "Biomas Especialidades Veterinarias",
     "+5492615914370": "Centro Clínico Quirúrgico Veterinario",
     "+5492614454142": "Veterinaria Picho's I"
}

# Mensaje base que deseas enviar, utilizando `{nombre}` como marcador de posición
mensaje_base = "Hola {nombre}, soy Agustín, desarrollador web. Vi que no tienen una página para mostrar sus actividades. Desde aloclick.com podemos ayudarte a mejorar tu presencia en línea. Si te interesa, puedo enviarte un PDF con nuestras propuestas digitales. ¡Saludos!"

# Intervalo de espera entre envíos en segundos
intervalo_espera = 60  # 1 minuto entre cada mensaje para evitar bloqueos

for numero, nombre in contactos.items():
    # Mensaje personalizado para cada contacto
    mensaje_personalizado = mensaje_base.format(nombre=nombre)
    
    # Enviar mensaje de forma instantánea
    try:
        kit.sendwhatmsg_instantly(numero, mensaje_personalizado)
        print(f"Mensaje enviado a {nombre} ({numero})")
        
        # Espera antes de enviar el siguiente mensaje
        time.sleep(intervalo_espera)
    except Exception as e:
        print(f"No se pudo enviar el mensaje a {nombre} ({numero}): {e}")
