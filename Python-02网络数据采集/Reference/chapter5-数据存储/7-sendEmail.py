import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "lafitehhq@126.com"
msg['To'] = "648725844@qq.com"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()