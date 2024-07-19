import os
from email import message_from_bytes
from email.header import decode_header

from domain.ports.mailserver_port import MailServerPort


class MailServer(MailServerPort):

    async def handle_DATA(self, server, session, envelope):
        print('Peer:', session.peer)
        print('Mail from:', envelope.mail_from)
        print('Rcpt to:', envelope.rcpt_tos)

        msg = message_from_bytes(envelope.content)

        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')
        print("Asunto:", subject)

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode(part.get_content_charset('utf-8'))
                    print("Cuerpo:", body)

                # Si hay un archivo adjunto
                elif "attachment" in content_disposition:
                    filename = part.get_filename()
                    if filename:
                        folder = '_tests_message/temporary_files'
                        if not os.path.isdir(folder):
                            os.mkdir(folder)
                        filepath = os.path.join(folder, filename)
                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        print(f"Adjunto guardado: {filepath}")
        else:
            body = msg.get_payload(decode=True).decode(msg.get_content_charset('utf-8'))
            print("Cuerpo:", body)

        return '250 OK'

