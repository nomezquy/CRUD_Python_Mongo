import smtplib

remitente = 'dnomezquy@gmail.com'
destinatario = 'dnomezquy@gmail.com'
msg ='correo de prueba'

#datos

username= 'dnomezquy@gmail.com'
password = 'aquí iria la pss'


#ejecución

server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(remitente,destinatario,msg)
server.quit()