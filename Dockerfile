# Usar una imagen base de Ubuntu
FROM ubuntu:20.04

# Actualizar e instalar Postfix y Certbot
RUN apt-get update && apt-get install -y \
    postfix \
    libsasl2-modules \
    mailutils \
    opendkim opendkim-tools \
    certbot

# Configurar Postfix
RUN postconf -e 'smtpd_sasl_auth_enable=yes'
RUN postconf -e 'smtpd_tls_auth_only=yes'
RUN postconf -e 'smtpd_tls_security_level=may'
RUN postconf -e 'smtp_tls_security_level=may'
RUN postconf -e 'smtpd_tls_received_header=yes'
RUN postconf -e 'myhostname=mail.tu-dominio.com'
RUN postconf -e 'mydestination=mail.tu-dominio.com, localhost'
RUN postconf -e 'mynetworks=127.0.0.0/8'
RUN postconf -e 'inet_interfaces=all'
RUN postconf -e 'inet_protocols=all'
RUN postconf -e 'relay_domains='

# Añadir un archivo de entrada para el servicio
# COPY entrypoint.sh /entrypoint.sh

# Establecer el punto de entrada
# ENTRYPOINT ["/entrypoint.sh"]
