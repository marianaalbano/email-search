#!/usr/bin/python3

import imaplib
import email
import os
import datetime
from time import sleep


class Search():
    def __init__(self, email_box):
            email = os.environ['EMAIL']
            passwd = os.environ['PASSWD']
            connect = os.environ['CONNECT']
            self.mail = imaplib.IMAP4_SSL(connect)
            self.mail.login(email, passwd)
            self.mail.list()
            self.mail.select(email_box)


    def search_body(self, search):
        try:
            result, data = self.mail.search(None, '(BODY "%s")' %search)
            
            ids = data[0]
            id_message = ids.split()
            return id_message
        except Exception as e:
            return ("Search Body error: %s" %e)


    def search_subject(self, search):
        try:
            result, data = self.mail.search(None, '(HEADER Subject "%s")' %search)
            
            ids = data[0]
            id_message = ids.split()
            return id_message
        except Exception as e:
            return ("Search Subject error: %s" %e)
    

    def search_from(self, search):
        try:
            result, data = self.mail.search(None, '(HEADER From "%s")' %search)
            
            ids = data[0]
            id_message = ids.split()
            return id_message
        except Exception as e:
            return ("Search From error: %s" %e)


    def message(self,id_messages):
        try:
            messages = []
            for id_message in id_messages:
                info = {}

                result, data = self.mail.fetch(id_message.decode(), "(RFC822)")
                raw_email = data[0][1].decode()

                email_message = email.message_from_string(raw_email)

                message = []
                if email_message.is_multipart():
                    for payload in email_message.walk():
                        if payload.get_content_type() == "text/plain":
                            message.append(payload.get_payload(decode=True).decode())
                        else:
                            continue
                            # message.append(email_message.get_payload(decode=True))

                info["Date"] = email_message['Date']
                info["To"] = email_message['To']
                info["From"] = email.utils.parseaddr(email_message['From'])[1]
                info["Subject"] = email_message['Subject']
                info["Body"] = message

                messages.append(info)

            return messages
            
        except Exception as e:
            print("erro %s" %e)
            return ("Parsing error: %s", e)


    def date_message(self, id_message):
        try:
            date_message = []
            messages = self.message(id_message)
            for message in messages:
                date_message.append(message["Date"])
            return date_message
        except Exception as e:
            return ("[Date] error: %s" %e)

        
    def from_message(self, id_message):
        try:
            from_message = []
            messages = self.message(id_message)
            for message in messages:
                from_message.append(message["From"])
            return from_message
        except Exception as e:
            return ("[From] error: %s" %e)


    def to_message(self, id_message):
        try:
            to_message = []
            messages = self.message(id_message)
            for message in messages:
                to_message.append(message["To"])
            return to_message
        except Exception as e:
            return ("[To] error: %s" %e)
    

    def body_message(self, id_message):
        try:
            body_message = []
            messages = self.message(id_message)
            for message in messages:
                body_message.append(message["Body"][0].replace("\r\n","\n"))
            return body_message
        except Exception as e:
            return ("[Body] error: %s" %e)


    def subject_message(self, id_message):
        try:
            subject_message = []
            messages = self.message(id_message)
            #print(messages)
            for message in messages:
                subject_message.append(message["Subject"])
                print(message["From"])
            return subject_message
        except Exception as e:
            return ("[Subject] error: %s" %e)


if __name__ == '__main__':
    # print ('Executando script')
    # sleep(1)
    # os.system('clear')    
    # mensagens = []
    # print('Conectando ao e-mail...')
    # #se = Search("inbox")
    # #print ('Buscando as mensagens')
    # #conteudo = se.search_body('Devops')
    # #mensagens.extend(conteudo)
    # #assunto = se.search_from("xxxxxxx")
    # #print(len(assunto))
    # #print(assunto)
    # # os.system('clear')    
    # # print ('Gravando mensagens... \n')
    # # print (mensagens)
    # # #x = se.message(mensagens)
    # # #print (x)
    # # x = se.date_message(["21"])
    # # print (x)
    # # x = se.body_message(["21"])
    # # print (x)
    # # x = se.from_message(["21"])
    # # print (x)
    # # x = se.to_message(["21"])
    # # print (x)
    # x = se.subject_message(assunto)
    # for item in x:
    #     print (item)
    # #print (x)
    # #print(len(x))
    #     #print("=============")
    #     #break

    # #import datetime
    
    # #print(date_str)
    # #print(type(date_str))
    # #format_str = '%d/%b/%Y' # The format
    # #datetime_obj = datetime.datetime.strptime(date_str, format_str)
    # #print(type(datetime.date.today() - datetime.timedelta(1)))
    # #print(datetime.datetime(2017,04,01))
    # #print(datetime_obj.date())

    
    # #for mensagem in mensagens:
    #     #print(se.message(mensagem))
    #     #print(se.date_message(mensagem))
    #     #print(se.body_message(mensagem))
    #     #print(se.from_message(mensagem))
    #     #print(se.to_message(mensagem))
    #     #print(se.subject_message(mensagem))
    # #    break
