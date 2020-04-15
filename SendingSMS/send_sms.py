from config import config 
from twilio.rest import Client

# This is Account Sid and Auth Token from Twilio Account
account_sid = config['account_sid']
auth_token = config['auth_token']
client = Client(account_sid, auth_token)
sender_number = config['phone_number']
receiver_number = config['receiver_number']

# This s aws credential to retrive pdf file
aws_access_key_id = config['aws_access_key_id'],
aws_secret_access_key = config['aws_secret_access_key']

# Text Body
text_body = 'your SARS-CoV2 (COVID-19) test results is now ready. Please call xxx-xxx-xxxx between the hours of 10am-5pm CST to get your results'


def sendSMS(body, senderPhoneNumber, receiverPhoneNumber):
  message = client.messages.create(
    body= body,
    from_= senderPhoneNumber,
    to= receiverPhoneNumber
  )
  print(message.sid)

sendSMS(text_body, sender_number, receiver_number)
