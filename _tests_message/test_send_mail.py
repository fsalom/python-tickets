import os
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Configuración del servidor SMTP
servidor_smtp = "localhost"
puerto_smtp = 1025

# Información del correo
remitente = "from@example.com"
destinatario = "to@example.com"
asunto = "Prueba de servidor SMTP con adjunto"
cuerpo = "Este es un correo de prueba con un archivo adjunto."

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto

# Adjuntar el cuerpo del mensaje
mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

# Adjuntar el archivo
nombre_archivo = "test.pdf"
try:
    with open(nombre_archivo, "rb") as adjunto:
        parte = MIMEBase("application", "octet-stream")
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(nombre_archivo)}")
        mensaje.attach(parte)
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encontró")
    exit(1)

try:
    # Conectar al servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.sendmail(remitente, destinatario, mensaje.as_string())
    servidor.quit()
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
