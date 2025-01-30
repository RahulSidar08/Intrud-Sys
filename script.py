import smtplib
 smtpUser = 'rahulsidar1700@gmail.com'
 smtpPass = 'axij regg sgps pawc'
 toAdd = 'rahulsidar2056@gmail.com'
 fromAdd = smtpUser
 subject = 'TEST EMAIL using PYTHON'
 header = 'To:' + toAdd + '\n' + 'From: ' + fromAdd + '\n' +
 'Subject:' + subject
 body = 'INTRUSION DETECTED IN YOUR SYSTEM'
 print (header + '\n' + body)
 s =smtplib.SMTP('smtp.gmail.com',587)
 s.ehlo()
 s.starttls()
 s.ehlo()
 s.login(smtpUser, smtpPass)
 print("Login Successful")
 s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
 s.quit()
