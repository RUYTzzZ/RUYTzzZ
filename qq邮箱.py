import smtplib
from email.mime.text import MIMEText



def mail():

   _user = "hhulibrary@foxmail.com"
   _pwd = "jeevkarioentcije"
   _to =sjr

   msg = MIMEText(neirong)
   msg["Subject"] = "关于签到的通知"
   msg["From"] = _user
   msg["To"] = _to

   try:
     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
     s.login(_user, _pwd)
     s.sendmail(_user, _to, msg.as_string())
     s.quit()
     print "Success!"
   except smtplib.SMTPException,e:
     print "Falied,%s"%e 

sjr='1570044080@qq.com'
neirong='内容测试'
mail()