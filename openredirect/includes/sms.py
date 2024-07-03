from twilio.rest import Client

# account_sid = 'ACd984f45e2006d275aeb6c0d0cd799bf6'
# auth_token = '09fd7c1cd5ad6236a7c06145e52c8fbd'

client = Client(account_sid, auth_token)
def send_msg(mesg):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'Open redirect: {mesg}',
            to='whatsapp:+91enter_number'
        )
        print(f"Message sent successfully: {message.sid} {mesg}")
    except Exception as e:
        print(f"Failed to send message: {e}")
