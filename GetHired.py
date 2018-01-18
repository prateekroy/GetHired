import smtplib

from string import Template

from os.path import basename
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import io
import shutil

from cmpCSV import Recruiter, Contacts

MY_ADDRESS = ''
PASSWORD = ''
ATTACHMENT = ['Prateek_Roy.pdf']
SUBJECT = "Summer Internship"

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with io.open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with io.open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_mail(send_from, send_to, subject, text, smtp, files=None):

    msg = MIMEMultipart()
    msg['From'] = send_from
    # msg['To'] = COMMASPACE.join(send_to)
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with io.open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp.sendmail(send_from, send_to, msg.as_string())


# def run_txt_version():
#     names, emails = get_contacts('mycontacts.txt') # read contacts
#     message_template = read_template('message.txt')

#     # set up the SMTP server
#     s = smtplib.SMTP(host='smtp.gmail.com', port=587)
#     s.starttls()
#     s.login(MY_ADDRESS, PASSWORD)

#     # For each contact, send the email:
#     for name, email in zip(names, emails):
#         msg = MIMEMultipart()       # create a message

#         # add in the actual person name to the message template
#         message = message_template.substitute(PERSON_NAME=name.title())

#         # Prints out the message body for our sake
#         print(message)

#         send_mail(MY_ADDRESS, email, SUBJECT, message, s, ATTACHMENT)

#         del msg
        
#     # Terminate the SMTP session and close the connection
#     s.quit()

def run_excel_version():
    contacts = Contacts() # read contacts
    recruiters = contacts.readfiles()
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    for recruiter in recruiters:
        print recruiter.emailid
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=recruiter.firstname)

        # Prints out the message body for our sake
        print(message)

        send_mail(MY_ADDRESS, recruiter.emailid, SUBJECT, message, s, ATTACHMENT)

        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit() 

def run_test_version():
    contacts = Contacts() # read contacts
    recruiters = contacts.readfiles()
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    for recruiter in recruiters:
        print recruiter.emailid
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=recruiter.firstname, COMPANY_NAME=recruiter.org)

        # Prints out the message body for our sake
        print(message)

        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit() 


if __name__ == '__main__':
    run_test_version()
