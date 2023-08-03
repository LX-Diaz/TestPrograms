import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('xavierdg7@gmail.com','gkzptcadkaqqbqxv')
smtpObj.sendmail('xavierdg7@gmail.com', 'xavierdg@hotmail.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()
