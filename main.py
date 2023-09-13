import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import platform
import interface
import log_generator
import getpass

so = platform.system()
if so == "Windows":
    comando = "cls"
else:
    comando = "clear"

def get_email():
    interface.welcome()
    os.system(comando)
    email = input("Email to receive the file: ")
    if "@" not in email:
        print("Email not real")
        input("Press ENTER to try again...")
        get_email()
    else:
        get_caminho_arquivo(email)
    
def get_caminho_arquivo(email):
    os.system(comando)
    email = email
    caminho = input("File path: ")
    if not os.path.exists(caminho):
        print("File not found")
        input("Press ENTER to try again...")
        get_caminho_arquivo()
    else:
        send_email(email, caminho)

def send_email(email, caminho):
    # Informações da conta de e-mail
    email_sender = "senderemailbot47@gmail.com"
    email_receiver = email
    senha = "vxtq gdro ttuw wnhx"

    # Configurações do servidor SMTP (no exemplo, é o Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Crie uma mensagem MIMEMultipart
    mensagem = MIMEMultipart()
    mensagem["From"] = email_sender
    mensagem["To"] = email_receiver
    mensagem["Subject"] = f"Arquivo enviado por {getpass.getuser()}"

    # Adicione o corpo do e-mail (opcional)
    corpo = ""
    mensagem.attach(MIMEText(corpo, "plain"))

    # Anexe o arquivo que você deseja enviar
    arquivo_anexo = caminho
    with open(arquivo_anexo, "rb") as arquivo:
        part = MIMEApplication(arquivo.read())
        part.add_header("Content-Disposition", f"attachment; filename={arquivo_anexo}")
        mensagem.attach(part)

    # Conecte-se ao servidor SMTP e envie o e-mail
    try:
        servidor_smtp = smtplib.SMTP(smtp_server, smtp_port)
        servidor_smtp.starttls()
        servidor_smtp.login(email_sender, senha)
        texto_do_email = mensagem.as_string()
        servidor_smtp.sendmail(email_sender, email_receiver, texto_do_email)
        servidor_smtp.quit()
        log_generator.generate_success_log("E-mail successfully sent!")
    except Exception as e:
        log_generator.generate_error_log(f"Error : {str(e)}")

get_email()
