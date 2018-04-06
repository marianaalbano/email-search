import imaplib
import email
import os
from time import sleep


class Search():
    def __init__(self):
        email = os.environ['EMAIL']
        passwd = os.environ['PASSWD']
        connect = os.environ['CONNECT']
        self.mail = imaplib.IMAP4_SSL(connect)
        self.mail.login(email, passwd)
        self.mail.list()
        self.mail.select("inbox")


    def search_body(self, search):
        result, data = self.mail.search(None, '(BODY "%s")' %search)
        
        ids = data[0]
        id_message = ids.split()
        return id_message

    
    def search_subject(self, search):
        result, data = self.mail.search(None, '(HEADER Subject "%s")' %search)
        
        ids = data[0]
        id_message = ids.split()
        return id_message



    def info_message(self,id_message):
        try:
            info = {}

            result, data = self.mail.fetch(id_message.decode(), "(RFC822)")
            raw_email = data[0][1].decode()

            email_message = email.message_from_string(raw_email)

            message = []
            if email_message.is_multipart():
                for payload in email_message.get_payload():
                    message.append(payload.get_payload(decode=True).decode())
            else:
                message.append(email_message.get_payload(decode=True).decode())

            info["Date"] = email_message['Date']
            info["To"] = email_message['To']
            info["From"] = email.utils.parseaddr(email_message['From'])[1]
            info["Subject"] = email_message['Subject']
            info["Body"] = message

            return info
            
        except Exception as e:
            print ("Erro: %s"%e)


if __name__ == '__main__':
    print ('Executando script')
    sleep(1)
    os.system('clear')    
    mensagens = []
    print('Conectando ao e-mail...')
    se = Search()
    print ('Buscando as mensagens')
    conteudo = se.search_body('Devops')
    mensagens.extend(conteudo)
    assunto = se.search_subject('Devops')
    mensagens.extend(assunto)
    os.system('clear')    
    print ('Gravando mensagens... \n')
    
    for mensagem in mensagens:
        print(se.info_message(mensagem))
        break