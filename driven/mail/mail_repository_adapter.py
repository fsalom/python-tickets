import email
import imaplib
import os
import re
from email.header import decode_header

import pdfplumber

from application.ports.driven.mail.mail_repository_port import MailRepositoryPort
from domain.mail import Mail


class MailRepositoryAdapter(MailRepositoryPort):
    def read(self) -> [Mail]:
        mails = []
        imap_server = "imap.gmail.com"
        imap_port = 993

        username = "misticketsmercadona@gmail.com"
        password = "tsur sier mchu seep"

        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(username, password)
        mail.select("inbox")
        status, messages = mail.search(None, 'UNSEEN')
        mail_ids = messages[0].split()
        temp_folder = "tempfiles"
        if not os.path.isdir(temp_folder):
            os.mkdir(temp_folder)

        for mail_id in mail_ids:
            status, msg_data = mail.fetch(mail_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    print("Asunto:", subject)

                    from_ = msg.get("From")
                    print("De:", from_)
                    name, from_email = self.extract_name_and_email(from_)

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if "attachment" in content_disposition:
                                filename = part.get_filename()
                                if filename:
                                    filename, encoding = decode_header(filename)[0]
                                    if isinstance(filename, bytes):
                                        filename = filename.decode(encoding if encoding else "utf-8")
                                    filepath = os.path.join(temp_folder, filename)
                                    with open(filepath, "wb") as f:
                                        f.write(part.get_payload(decode=True))
                                    print(f"Archivo adjunto guardado como: {filepath}")
                                    content = self.read_attachment(filepath)
                                    mails.append(Mail(email=from_email,
                                                      subject=subject,
                                                      content=content,
                                                      date_raw=self.get_raw_date(subject)))
        mail.logout()
        return mails

    @staticmethod
    def extract_name_and_email(text):
        pattern = r"(.+?)\s*<(.+?)>"
        match = re.match(pattern, text)

        if match:
            name = match.group(1).strip()  # Captura el nombre
            email = match.group(2).strip()  # Captura el email
            return name, email
        else:
            return None

    @staticmethod
    def get_raw_date(subject) -> str:
        pattern = r"\b\d{8}\b"
        match = re.search(pattern, subject)
        if match:
            date = match.group()
            return date
        else:
            return "-"

    @staticmethod
    def read_attachment(pdf_path) -> str:
        text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    text += page.extract_text()
        finally:
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
                print(f"El archivo '{pdf_path}' ha sido eliminado correctamente.")
            else:
                print(f"El archivo '{pdf_path}' no existe o ya ha sido eliminado.")

        return text
