#!/bin/bash
# Este script configurará y ejecutará Postfix

# Crear certificados SSL usando Let's Encrypt
certbot certonly --standalone --non-interactive --agree-tos --email "$EMAIL" -d mail."$DOMAIN"

# Configurar Postfix para usar los certificados SSL
postconf -e 'smtpd_tls_cert_file=/etc/letsencrypt/live/mail.'"$DOMAIN"'/fullchain.pem'
postconf -e 'smtpd_tls_key_file=/etc/letsencrypt/live/mail.'"$DOMAIN"'/privkey.pem'

# Iniciar Postfix
service postfix start

# Mantener el contenedor en ejecución
tail -f /var/log/mail.log
