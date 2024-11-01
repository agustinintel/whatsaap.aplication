import pywhatkit as kit
import time

# Diccionario con números de teléfono y nombres
contactos = {
    "+5492612388045": "Agustín",
    "+5492616005809": "Mónica",
    "+5492615007986": "Adrian"
}

# Mensaje base que deseas enviar, utilizando `{nombre}` como marcador de posición
mensaje_base = "¡Hola, {nombre}! Quiero contarte sobre una excelente oportunidad que puede interesarte."

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
