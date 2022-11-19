import configparser
import sendgrid
from sendgrid.helpers.mail import Mail
config = configparser.ConfigParser()
import base64

config.read('mail.env')
APIKEY = config.get('API', 'APIKEY')
api = sendgrid.SendGridAPIClient(APIKEY)
FROM_EMAIL = config.get('API','FROM_EMAIL')
def sendemail(user,content):
    TO_EMAIL = user
    mail = Mail(from_email=FROM_EMAIL,to_emails=TO_EMAIL,subject='Hey there! We heard from you!',html_content=f'<strong>{content}</strong>')
    response = api.send(mail)
    print(response.status_code)
    print(response.headers)

