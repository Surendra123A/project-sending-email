import smtplib

sender = 'surendrademoacc@gmail.com'
recevier = ['surendrap792@gmail.com']

message = '''
this is a demo mail sent using python and its libs
Pwned Passwords are hundreds of millions of real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts. They're searchable online below as well as being downloadable for use in other online systems. Read more about how HIBP protects the privacy of searched passwords.
'''

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('surendrademoacc@gmail.com', 'hhlrtsgxihxvntmk')
    smtp.sendmail(sender,recevier,message)
    print('Mail Sent!!!')