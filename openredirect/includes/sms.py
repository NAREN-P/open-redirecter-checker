from twilio.rest import Client

 account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)
def send_msg(mesg):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+',
            body=f'Open redirect: {mesg}',
            to='whatsapp:+91enter_number'
        )
        print(f"Message sent successfully: {message.sid} {mesg}")
    except Exception as e:
        print(f"Failed to send message: {e}")

#go and create you twillo account and then use you acc_id and  auth_tocken ,whats app number ,twillo whatsapp number
