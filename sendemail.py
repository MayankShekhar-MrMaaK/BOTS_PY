/*SEND MULTIPLE EMAIL....EMAIL_AUTOMATION*/
import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('urmail@gmail.com','password')
mailto=['ms9222934@gmail.com','mayankshekhar91970@gmail.com']
for m in mailto:
	message="Subject: Welcome\n\nDear {}\n i love programming".format(m)
	conn.sendmail('mmmayanksshekhar@gmail.com',m,message)
conn.quit()