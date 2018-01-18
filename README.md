# GetHired

1) Edit these lines GetHired.py(Line 15-18) according to your account:

MY_ADDRESS = ''
PASSWORD = ''
ATTACHMENT = ['Prateek_Roy.pdf']
SUBJECT = "Summer Internship"

2) Add your email body message in message.txt

3) Edit GetHired.py(Line 136) for customizing your body:
message = message_template.substitute(PERSON_NAME=recruiter.firstname, COMPANY_NAME=recruiter.org)

All attachments, .csv files should be in same folder as script.
4) Run python GetHired.py

You might want to change account setting of gmail to allow less secure apps to send mail. Follow https://support.google.com/accounts/answer/6010255?hl=en
